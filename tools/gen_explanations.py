"""Generate lời giải chi tiết Gemini-style cho TẤT CẢ câu toán còn thiếu.

Cài đặt 1 lần:
    pip install anthropic

Chạy:
    export ANTHROPIC_API_KEY=sk-ant-...
    python -m tools.gen_explanations            # gen toàn bộ
    python -m tools.gen_explanations --max 50   # test 50 câu rồi commit

Lưu trực tiếp vào ../explanations.json (auto-save mỗi 20 câu để chống crash).
App tự nạp file này lúc startup qua _apply_explanations_override() trong
questions.py.

Chi phí ước tính (Haiku 4.5):
    ~500 input + ~400 output token/câu × ~1500 câu ≈ 1.35M token.
    Pricing 1$/1M input + 5$/1M output ≈ $3-4 cho toàn bộ.

Pool được scan (chỉ TOÁN, không gồm Tiếng Anh):
    BAO_MEO_DE_1/2, _TOAN_1_HK2, _HSG_TOAN_1_NEW, _HSG_TOAN_1_HARD_POOL,
    _OLYMPIC_TOAN_1_POOL, BAO_MEO_VIOLYMPIC, _TOAN_2_HK1/HK2, _HSG_TOAN_2,
    _VIOLYMPIC_TOAN_2, MINH_KHANH_TOAN, NHAT_KHOI_TOAN_LOP7, NHAT_KHOI_TOAN,
    _TOAN_8_HK1, _HSG_TOAN_6_EXAMS.
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import questions as Q  # noqa: E402

POOL_NAMES = (
    "BAO_MEO_DE_1", "BAO_MEO_DE_2", "BAO_MEO_VIOLYMPIC",
    "_TOAN_1_HK2", "_HK2_TOAN_1_NC",
    "_HSG_TOAN_1_NEW", "_HSG_TOAN_1_HARD_POOL", "_OLYMPIC_TOAN_1_POOL",
    "_TOAN_2_HK1", "_TOAN_2_HK2", "_HSG_TOAN_2", "_VIOLYMPIC_TOAN_2",
    "MINH_KHANH_TOAN", "MINH_KHANH_TOAN_HSG",
    "NHAT_KHOI_TOAN_LOP7",
    "NHAT_KHOI_TOAN", "_TOAN_8_HK1",
)

MODEL = os.environ.get("EXPL_GEN_MODEL", "claude-haiku-4-5")
EXPLANATIONS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "explanations.json"
)

SYS_PROMPT = (
    "Bạn là gia sư Toán giỏi, viết lời giải chi tiết cho học sinh tiểu học/THCS "
    "Việt Nam. Phong cách phải:\n"
    "1. Nêu hướng đi/phương pháp NGẮN GỌN ở đầu (nếu cần).\n"
    "2. Trình bày từng BƯỚC rõ ràng, đánh số (Bước 1, Bước 2…).\n"
    "3. Mỗi bước có công thức/phép tính cụ thể, không nói chung chung.\n"
    "4. Kết thúc bằng dòng \"Đáp án: …\" khớp đáp án đã cho.\n"
    "5. Tiếng Việt, KHÔNG dùng LaTeX (\\frac…). Dùng ký hiệu thường: ×, ÷, ², √.\n"
    "6. Phân cách bước bằng xuống dòng \\n. Không markdown, không bullet, "
    "không in nghiêng/đậm.\n"
    "7. CHỈ trả về lời giải, không lặp lại đề bài, không thêm tiêu đề "
    "\"Lời giải:\".\n"
)


def collect_todo(existing: dict) -> list[tuple[str, str, str]]:
    """Trả list (pool_name, q_text, answer) cần gen."""
    todo: list[tuple[str, str, str]] = []
    seen_q: set[str] = set()
    for name in POOL_NAMES:
        pool = getattr(Q, name, [])
        if not isinstance(pool, list):
            continue
        for q in pool:
            if not isinstance(q, dict):
                continue
            qt = (q.get("q") or "").strip()
            if not qt or qt in seen_q:
                continue
            seen_q.add(qt)
            if qt in existing:
                continue
            if (q.get("explanation") or "").strip():
                continue  # đã có exp inline trong code → skip
            ans = q.get("answer", "")
            if isinstance(ans, list):
                ans = "; ".join(str(a) for a in ans)
            todo.append((name, qt, str(ans)))
    # HSG Toán 6 nằm trong dict {exam_no: list}
    hsg6 = getattr(Q, "_HSG_TOAN_6_EXAMS", {})
    if isinstance(hsg6, dict):
        for pool in hsg6.values():
            for q in pool:
                if not isinstance(q, dict):
                    continue
                qt = (q.get("q") or "").strip()
                if not qt or qt in seen_q:
                    continue
                seen_q.add(qt)
                if qt in existing:
                    continue
                if (q.get("explanation") or "").strip():
                    continue
                ans = q.get("answer", "")
                if isinstance(ans, list):
                    ans = "; ".join(str(a) for a in ans)
                todo.append(("_HSG_TOAN_6_EXAMS", qt, str(ans)))
    return todo


def save(explanations: dict) -> None:
    tmp = EXPLANATIONS_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(explanations, f, ensure_ascii=False, indent=2, sort_keys=True)
    os.replace(tmp, EXPLANATIONS_PATH)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", type=int, default=0,
                        help="Giới hạn số câu (0 = không giới hạn)")
    parser.add_argument("--model", default=MODEL)
    args = parser.parse_args()

    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: chưa cài SDK. Chạy: pip install anthropic", file=sys.stderr)
        return 1

    client = Anthropic()

    existing: dict = {}
    if os.path.exists(EXPLANATIONS_PATH):
        with open(EXPLANATIONS_PATH, encoding="utf-8") as f:
            existing = json.load(f)
    print(f"Đã có sẵn: {len(existing)} câu trong explanations.json")

    todo = collect_todo(existing)
    if args.max:
        todo = todo[: args.max]
    print(f"Cần gen: {len(todo)} câu (model={args.model})")
    if not todo:
        return 0

    for i, (pool_name, qt, ans) in enumerate(todo, 1):
        user_msg = f"Đề bài:\n{qt}\n\nĐáp án đúng: {ans}\n\nViết lời giải chi tiết:"
        try:
            resp = client.messages.create(
                model=args.model,
                max_tokens=900,
                system=SYS_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            exp = "".join(b.text for b in resp.content if hasattr(b, "text")).strip()
            if exp:
                existing[qt] = exp
                print(f"[{i}/{len(todo)}] {pool_name} OK ({len(exp)}B)")
            else:
                print(f"[{i}/{len(todo)}] {pool_name} TRỐNG")
        except Exception as exc:
            print(f"[{i}/{len(todo)}] {pool_name} FAIL: {exc}")
            time.sleep(2)
            continue
        if i % 20 == 0:
            save(existing)
            print(f"  → Đã lưu checkpoint ({len(existing)} câu)")

    save(existing)
    print(f"Xong. Tổng: {len(existing)} câu trong explanations.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
