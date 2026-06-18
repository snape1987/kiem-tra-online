"""Rescore audit_hsg_toan_6_report.json với extract+normalize MỚI.

Run trước khi merge PR fix: report.json có chứa full claude_reasoning,
script này re-extract đáp án + re-compare để LỌC ra mismatch THẬT, bỏ
các false positive cosmetic (bold marker, unit, prefix biến tên).

KHÔNG gọi API — chỉ xử lý file local.

Cách dùng:
    python -m tools.rescore_audit

Output:
- audit_hsg_toan_6_clean.json: chỉ chứa câu mismatch THẬT (sau khi normalize lại)
- In stat: trước/sau bao nhiêu mismatch
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tools.audit_hsg_toan_6 import normalize, extract_claude_answer  # noqa: E402

REPORT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "audit_hsg_toan_6_report.json"
)
CLEAN_PATH = os.path.join(
    os.path.dirname(__file__), "..", "audit_hsg_toan_6_clean.json"
)


def main() -> int:
    if not os.path.exists(REPORT_PATH):
        print(f"ERROR: chưa có {REPORT_PATH}. Chạy audit trước.")
        return 1
    with open(REPORT_PATH, encoding="utf-8") as f:
        report = json.load(f)
    print(f"Đọc {len(report)} entry từ report cũ.")

    clean: list[dict] = []
    promoted_to_match = 0
    for entry in report:
        reasoning = entry.get("claude_reasoning", "")
        pdf_ans = entry.get("pdf_answer", "")
        # Re-extract bằng code mới (đã fix bold/prefix/multi-pattern)
        new_claude_ans = extract_claude_answer(reasoning)
        match = normalize(pdf_ans) == normalize(new_claude_ans)
        if match:
            promoted_to_match += 1
            continue
        # Update với answer extracted mới (sạch hơn) trước khi giữ
        clean.append({
            "q":                entry.get("q", ""),
            "pdf_answer":       pdf_ans,
            "claude_answer":    new_claude_ans,
            "claude_reasoning": reasoning,
            "topic":            entry.get("topic", ""),
        })

    with open(CLEAN_PATH, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

    print(f"Mismatch CŨ:    {len(report)}")
    print(f"Mismatch SẠCH:  {len(clean)}  (lọc bỏ {promoted_to_match} false positive cosmetic)")
    print(f"Output: {CLEAN_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
