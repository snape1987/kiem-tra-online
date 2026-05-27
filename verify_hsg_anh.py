# -*- coding: utf-8 -*-
"""Kiem tra dap an HSG Anh 6: moi cau 'choice' phai co answer khop 1 option.
Chuan hoa giong app.py: lower() + bo khoang trang. In ra cau FAIL."""
import sys
sys.path.insert(0, ".")
import questions as Q


def norm(s):
    return str(s).lower().replace(" ", "")


def main():
    exams = Q._HSG_ANH_6_EXAMS
    total = 0
    fails = []
    for no in range(1, 37):
        items = exams[no]
        for idx, it in enumerate(items):
            if it.get("type") != "choice":
                continue
            total += 1
            opts = it.get("options", [])
            ans = it.get("answer", "")
            normopts = {norm(o) for o in opts}
            if norm(ans) not in normopts:
                fails.append((no, idx, it.get("topic", ""),
                              it.get("q", "")[:60], ans, opts))
    print(f"Tong cau choice: {total}")
    print(f"FAIL (answer khong khop option): {len(fails)}")
    for no, idx, topic, q, ans, opts in fails:
        print(f"  DE {no} [{idx}] ({topic}): q='{q}' | answer='{ans}' | options={opts}")
    return len(fails)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
