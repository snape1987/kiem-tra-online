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
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import questions as Q  # noqa: E402
from tools.audit_hsg_toan_6 import normalize, extract_claude_answer  # noqa: E402

DEFAULT_REPORT = "audit_hsg_toan_6_report.json"

# Pool toán quét cho options lookup (bất kỳ pool nào có câu trắc nghiệm)
_LOOKUP_POOLS = (
    "NHAT_KHOI_TOAN_LOP7", "_TOAN_8_HK1", "NHAT_KHOI_TOAN",
    "MINH_KHANH_TOAN", "MINH_KHANH_TOAN_HSG",
    "BAO_MEO_DE_1", "BAO_MEO_DE_2", "BAO_MEO_POOL", "BAO_MEO_VIOLYMPIC",
    "_TOAN_1_HK2", "_HK2_TOAN_1_NC",
    "_HSG_TOAN_1_NEW", "_HSG_TOAN_1_HARD_POOL", "_OLYMPIC_TOAN_1_POOL",
    "_TOAN_2_HK1", "_TOAN_2_HK2", "_HSG_TOAN_2", "_VIOLYMPIC_TOAN_2",
)


def lookup_options(q_text: str) -> list:
    """Tìm options của 1 câu trong tất cả pool toán dựa vào q_text."""
    if not q_text:
        return []
    target = q_text.strip()
    for name in _LOOKUP_POOLS:
        pool = getattr(Q, name, None)
        if not isinstance(pool, list):
            continue
        for q in pool:
            if not isinstance(q, dict):
                continue
            if (q.get("q") or "").strip() == target:
                opts = q.get("options") or []
                if isinstance(opts, list):
                    return opts
    # HSG Toán 6 (dict-of-list)
    hsg6 = getattr(Q, "_HSG_TOAN_6_EXAMS", {})
    if isinstance(hsg6, dict):
        for pool in hsg6.values():
            for q in pool:
                if isinstance(q, dict) and (q.get("q") or "").strip() == target:
                    opts = q.get("options") or []
                    if isinstance(opts, list):
                        return opts
    return []


_LETTER_RE = re.compile(r"^([A-D])\.?$")


def expand_letter_to_option(claude_ans: str, q_text: str) -> str:
    """Nếu claude_ans chỉ là 1 chữ A-D → lookup option content trong pool."""
    s = claude_ans.strip()
    m = _LETTER_RE.match(s)
    if not m:
        return claude_ans
    idx = ord(m.group(1)) - ord("A")
    opts = lookup_options(q_text)
    if 0 <= idx < len(opts):
        return str(opts[idx])
    return claude_ans


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default=DEFAULT_REPORT,
                        help="Tên file report cần lọc (vd: audit_nhat_khoi_toan_lop7_report.json)")
    args = parser.parse_args()

    root = os.path.join(os.path.dirname(__file__), "..")
    report_path = os.path.join(root, args.report)
    # Tự suy ra clean path: <name>_report.json → <name>_clean.json
    clean_name = args.report.replace("_report.json", "_clean.json")
    if clean_name == args.report:
        clean_name = args.report.replace(".json", "_clean.json")
    clean_path = os.path.join(root, clean_name)

    if not os.path.exists(report_path):
        print(f"ERROR: chưa có {report_path}. Chạy audit trước.")
        return 1
    with open(report_path, encoding="utf-8") as f:
        report = json.load(f)
    print(f"Đọc {len(report)} entry từ {args.report}.")

    clean: list[dict] = []
    promoted_to_match = 0
    for entry in report:
        reasoning = entry.get("claude_reasoning", "")
        pdf_ans = entry.get("pdf_answer", "")
        q_text = entry.get("q", "")
        # Re-extract bằng code mới (đã fix bold/prefix/multi-pattern)
        new_claude_ans = extract_claude_answer(reasoning)
        # Nếu chỉ là 1 chữ A-D → map sang option content
        new_claude_ans = expand_letter_to_option(new_claude_ans, q_text)
        match = normalize(pdf_ans) == normalize(new_claude_ans)
        if match:
            promoted_to_match += 1
            continue
        clean.append({
            "q":                q_text,
            "pdf_answer":       pdf_ans,
            "claude_answer":    new_claude_ans,
            "claude_reasoning": reasoning,
            "topic":            entry.get("topic", ""),
        })

    with open(clean_path, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

    print(f"Mismatch CŨ:    {len(report)}")
    print(f"Mismatch SẠCH:  {len(clean)}  (lọc bỏ {promoted_to_match} false positive cosmetic)")
    print(f"Output: {clean_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
