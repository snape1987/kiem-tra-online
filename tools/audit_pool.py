"""Audit GENERIC cho bất kỳ pool toán nào — phát hiện đáp án PDF có thể sai.

Cách dùng:
    # Lớp 7
    python -m tools.audit_pool --pool NHAT_KHOI_TOAN_LOP7

    # Lớp 8 HK1
    python -m tools.audit_pool --pool _TOAN_8_HK1

    # Lớp 8 HK2 (HSG/Olympic)
    python -m tools.audit_pool --pool NHAT_KHOI_TOAN

    # Nhiều pool cùng lúc → 1 report chung
    python -m tools.audit_pool --pool NHAT_KHOI_TOAN_LOP7,_TOAN_8_HK1

    # Test giới hạn
    python -m tools.audit_pool --pool NHAT_KHOI_TOAN_LOP7 --max 10

Output: audit_<pool>_report.json (chỉ chứa mismatch + full reasoning Claude).

Logic giống tools/audit_hsg_toan_6.py — reuse extract_claude_answer + normalize.
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import questions as Q  # noqa: E402
from tools.audit_hsg_toan_6 import (  # noqa: E402
    SYS_PROMPT, extract_claude_answer, normalize,
)

MODEL = os.environ.get("AUDIT_MODEL", "claude-haiku-4-5")


def collect_from_pool(pool_name: str) -> list[tuple[str, str, str, list]]:
    """Trả list (q_text, pdf_answer, topic, options) duy nhất từ pool name.

    options: list các đáp án A/B/C/D (rỗng nếu câu fill)."""
    pool = getattr(Q, pool_name, None)
    if not isinstance(pool, list):
        print(f"WARNING: {pool_name} không phải list (type={type(pool).__name__}), skip.")
        return []
    out: list[tuple[str, str, str, list]] = []
    seen: set[str] = set()
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
        opts = q.get("options") or []
        if not isinstance(opts, list):
            opts = []
        out.append((qt, str(ans), q.get("topic", ""), opts))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", required=True,
                        help="Tên pool toán (vd: NHAT_KHOI_TOAN_LOP7). "
                             "Comma-separated cho nhiều pool.")
    parser.add_argument("--max", type=int, default=0)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--include-match", action="store_true")
    args = parser.parse_args()

    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: chưa cài SDK. Chạy: python -m pip install anthropic",
              file=sys.stderr)
        return 1

    client = Anthropic()

    pool_names = [n.strip() for n in args.pool.split(",") if n.strip()]
    # Output path: nếu 1 pool → audit_<name>_report.json, nhiều pool → audit_multi_<hash>.json
    if len(pool_names) == 1:
        report_path = os.path.join(
            os.path.dirname(__file__), "..",
            f"audit_{pool_names[0].lstrip('_').lower()}_report.json"
        )
    else:
        joined = "_".join(p.lstrip("_").lower() for p in pool_names)[:40]
        report_path = os.path.join(
            os.path.dirname(__file__), "..", f"audit_{joined}_report.json"
        )

    # Skip những câu đã có trong answer_overrides.json
    overrides_path = os.path.join(
        os.path.dirname(__file__), "..", "answer_overrides.json"
    )
    overrides: dict = {}
    if os.path.exists(overrides_path):
        try:
            with open(overrides_path, encoding="utf-8") as f:
                overrides = json.load(f)
        except json.JSONDecodeError:
            pass
    print(f"Đã có {len(overrides)} câu trong answer_overrides.json — sẽ skip.")

    # Collect từ tất cả pool, dedup chéo
    all_questions: list[tuple[str, str, str, list]] = []
    seen: set[str] = set()
    for name in pool_names:
        items = collect_from_pool(name)
        new = 0
        for qt, ans, topic, opts in items:
            if qt in seen or qt in overrides:
                continue
            seen.add(qt)
            all_questions.append((qt, ans, topic, opts))
            new += 1
        print(f"  {name}: +{new} câu (tổng {len(items)} trong pool)")

    if args.max:
        all_questions = all_questions[: args.max]
    print(f"Audit: {len(all_questions)} câu (model={args.model})")
    print(f"Output: {report_path}")
    if not all_questions:
        return 0

    report: list[dict] = []
    n_mismatch = 0

    for i, (qt, pdf_ans, topic, opts) in enumerate(all_questions, 1):
        if opts:
            opts_text = "\n".join(f"  {chr(65+j)}. {o}" for j, o in enumerate(opts))
            user_msg = (
                f"Đề bài (TRẮC NGHIỆM, chọn 1 phương án ĐÚNG NHẤT):\n{qt}\n\n"
                f"Các phương án:\n{opts_text}\n\n"
                "Giải đi. Dòng ĐÁPÁN: phải khớp NGUYÊN VĂN 1 trong các phương án trên."
            )
        else:
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
            print(f"[{i}/{len(all_questions)}] FAIL: {exc}")
            time.sleep(2)
            continue

        claude_ans = extract_claude_answer(full)
        match = normalize(pdf_ans) == normalize(claude_ans)
        tag = "OK  " if match else "DIFF"
        print(f"[{i}/{len(all_questions)}] {tag}  PDF={pdf_ans!r:20.20}  CLAUDE={claude_ans!r:25.25}")

        if not match:
            n_mismatch += 1
        if (not match) or args.include_match:
            report.append({
                "q": qt,
                "pdf_answer": pdf_ans,
                "claude_answer": claude_ans,
                "claude_reasoning": full,
                "topic": topic,
            })

        if i % 20 == 0:
            with open(report_path, "w", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            print(f"  → checkpoint ({len(report)} entry)")

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nXong. Mismatch: {n_mismatch}/{len(all_questions)} câu.")
    print(f"Report: {report_path}")
    print("\nBước tiếp theo:")
    print(f"  1. python -m tools.rescore_audit --report {os.path.basename(report_path)}")
    print("  2. Đọc clean report, verify từng câu DIFF bằng Gemini web.")
    print("  3. Fill answer_overrides.json: { \"<đề bài>\": \"đáp án đúng\" }")
    return 0


if __name__ == "__main__":
    sys.exit(main())
