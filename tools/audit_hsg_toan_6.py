"""Audit đề HSG Toán 6 — phát hiện câu nào đáp án PDF có thể sai.

Cách dùng:
    pip install anthropic                       # (đã cài rồi)
    $env:ANTHROPIC_API_KEY = "sk-ant-..."       # PowerShell
    python -m tools.audit_hsg_toan_6 --max 20   # test trên 20 câu trước
    python -m tools.audit_hsg_toan_6            # full ~178 câu

Output: audit_hsg_toan_6_report.json
    [
      {
        "q":              "...đề bài...",
        "pdf_answer":     "...đáp án trong code...",
        "claude_answer":  "...Claude giải ra...",
        "claude_reasoning": "...full step-by-step...",
        "topic":          "Số học | Đại số | Hình học | ..."
      },
      ...
    ]

Sau khi có report, Su:
1. Đọc từng câu mismatch.
2. Verify lại bằng Gemini web nếu nghi ngờ.
3. Fill `answer_overrides.json` với những câu đáp án PDF SAI thật.
   Format: { "<đề bài>": "đáp án đúng" }
4. App tự nạp override lúc startup → không cần sửa questions.py.

Chi phí ước tính (Haiku 4.5, ~178 câu): ~$0.30.
"""
import argparse
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import questions as Q  # noqa: E402

REPORT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "audit_hsg_toan_6_report.json"
)
OVERRIDES_PATH = os.path.join(
    os.path.dirname(__file__), "..", "answer_overrides.json"
)

MODEL = os.environ.get("AUDIT_MODEL", "claude-haiku-4-5")

SYS_PROMPT = (
    "Bạn là giám khảo Toán HSG lớp 6 Việt Nam. Giải đề độc lập, KHÔNG nhìn "
    "đáp án có sẵn (không có sẵn).\n"
    "Yêu cầu trả lời:\n"
    "1. Trình bày từng BƯỚC ngắn gọn, có phép tính cụ thể.\n"
    "2. Tiếng Việt, KHÔNG dùng LaTeX. Dùng ký hiệu: ×, ÷, ², √, /.\n"
    "3. DÒNG CUỐI CÙNG (bắt buộc, không thêm gì sau): ĐÁPÁN: <giá trị>\n"
    "   Ví dụ: ĐÁPÁN: 2036  /  ĐÁPÁN: 1/1013  /  ĐÁPÁN: x = 6  /  ĐÁPÁN: 0,5 cm\n"
    "4. Nếu đề thiếu thông tin / không giải được → ghi: ĐÁPÁN: KHÔNG ĐỦ DỮ KIỆN\n"
)


def collect_questions() -> list[tuple[str, str, str]]:
    """Trả list (q_text, pdf_answer, topic) duy nhất trong HSG Toán 6.

    Lấy từ _HSG_TOAN_6_EXAMS (dict {exam_no: list}) — đã bao gồm 11 đề.
    Loại trùng theo q_text (vì nhiều đề share pool).
    """
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    hsg6 = getattr(Q, "_HSG_TOAN_6_EXAMS", {})
    if not isinstance(hsg6, dict):
        print("ERROR: _HSG_TOAN_6_EXAMS không phải dict.")
        return out
    for exam_no in sorted(hsg6.keys()):
        pool = hsg6[exam_no]
        for q in pool:
            if not isinstance(q, dict):
                continue
            qt = (q.get("q") or "").strip()
            if not qt or qt in seen:
                continue
            seen.add(qt)
            ans = q.get("answer", "")
            if isinstance(ans, list):
                ans = "; ".join(str(a) for a in ans)
            out.append((qt, str(ans), q.get("topic", "")))
    return out


_NORM_RE = re.compile(r"\s+")


def normalize(s: str) -> str:
    """Chuẩn hóa đáp án để so sánh: lowercase, strip, dấu trừ unicode → -,
    dấu phẩy thập phân → ., bỏ space thừa, bỏ 'cm'/'m'/đơn vị cuối."""
    if not s:
        return ""
    s = s.strip().lower()
    s = s.replace("−", "-").replace("–", "-").replace("—", "-")
    s = s.replace(",", ".")  # 0,5 → 0.5
    s = _NORM_RE.sub(" ", s)
    # Bỏ đơn vị thông dụng cuối câu
    for unit in (" cm", " m", " kg", " g", " phút", " giờ", " giây",
                 " (cm)", " học sinh", " bạn", " câu"):
        if s.endswith(unit):
            s = s[: -len(unit)].strip()
    # Số có dấu = → bỏ 'x =' / 'a =' prefix
    s = re.sub(r"^[a-z]\s*=\s*", "", s)
    return s.strip()


def extract_claude_answer(text: str) -> str:
    """Tách dòng cuối 'ĐÁPÁN: ...' khỏi response Claude."""
    if not text:
        return ""
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    for ln in reversed(lines):
        m = re.match(r"^Đ[ÁA]P\s*[ÁA]N\s*:?\s*(.*)$", ln, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    # Fallback: dòng cuối
    return lines[-1] if lines else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", type=int, default=0,
                        help="Giới hạn số câu (0 = full)")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--include-match", action="store_true",
                        help="Ghi cả câu match (để debug). Mặc định: chỉ mismatch.")
    args = parser.parse_args()

    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: chưa cài SDK. Chạy: python -m pip install anthropic",
              file=sys.stderr)
        return 1

    client = Anthropic()

    # Skip những câu đã có trong answer_overrides.json (Su đã verify rồi)
    overrides: dict = {}
    if os.path.exists(OVERRIDES_PATH):
        try:
            with open(OVERRIDES_PATH, encoding="utf-8") as f:
                overrides = json.load(f)
        except json.JSONDecodeError:
            pass
    print(f"Đã có {len(overrides)} câu trong answer_overrides.json — sẽ skip.")

    questions = collect_questions()
    questions = [q for q in questions if q[0] not in overrides]
    if args.max:
        questions = questions[: args.max]
    print(f"Audit: {len(questions)} câu (model={args.model})")
    if not questions:
        return 0

    report: list[dict] = []
    n_mismatch = 0

    for i, (qt, pdf_ans, topic) in enumerate(questions, 1):
        user_msg = f"Đề bài:\n{qt}\n\nGiải đi:"
        try:
            resp = client.messages.create(
                model=args.model,
                max_tokens=900,
                system=SYS_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            full = "".join(b.text for b in resp.content if hasattr(b, "text")).strip()
        except Exception as exc:
            print(f"[{i}/{len(questions)}] FAIL: {exc}")
            time.sleep(2)
            continue

        claude_ans = extract_claude_answer(full)
        match = normalize(pdf_ans) == normalize(claude_ans)
        tag = "OK " if match else "DIFF"
        print(f"[{i}/{len(questions)}] {tag}  PDF={pdf_ans!r:20.20}  CLAUDE={claude_ans!r:20.20}")

        if not match:
            n_mismatch += 1
        if (not match) or args.include_match:
            report.append({
                "q": qt,
                "pdf_answer": pdf_ans,
                "claude_answer": claude_ans,
                "claude_reasoning": full,
                "topic": topic,
                "match": match,
            })

        # Checkpoint mỗi 20 câu
        if i % 20 == 0:
            with open(REPORT_PATH, "w", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            print(f"  → checkpoint ({len(report)} entry)")

    # Final save
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nXong. Mismatch: {n_mismatch}/{len(questions)} câu.")
    print(f"Report: {REPORT_PATH}")
    print("\nBước tiếp theo:")
    print("  1. Đọc report, verify lại bằng Gemini web cho từng câu DIFF.")
    print(f"  2. Fill {OVERRIDES_PATH} dạng:")
    print('     { "<đề bài>": "đáp án đúng", ... }')
    print("  3. Commit & push — app tự nạp lúc startup.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
