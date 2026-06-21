"""Apply HSG Anh 6 listening fixes from audit JSON files.

Rewrite questions.py listening sections (entries có topic='Listening') cho 35 đề HSG Anh 6
dựa trên DOC gốc trên Drive (đã được agents extract ra JSON).

Cách dùng:
    python -m tools.apply_anh6_listening --dry-run     # preview, không ghi file
    python -m tools.apply_anh6_listening               # apply + ghi questions.py
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QFILE = os.path.join(ROOT, "questions.py")
JSON_FILES = [
    os.path.join(ROOT, "tools/anh6_audit_de_1_9.json"),
    os.path.join(ROOT, "tools/anh6_audit_de_10_18.json"),
    os.path.join(ROOT, "tools/anh6_audit_de_19_27.json"),
    os.path.join(ROOT, "tools/anh6_audit_de_28_35.json"),
]


def load_audit():
    audit = {}
    for f in JSON_FILES:
        with open(f, encoding="utf-8") as fp:
            audit.update(json.load(fp))
    return audit


# ── parse_choice: tách câu hỏi MC dạng "Q? A. opt1 B. opt2 C. opt3" ──────────
_OPT_START_RE = re.compile(r'(?:^|\s|\?|:|—)([A-F])[.\)]\s+')


def parse_choice(raw, answer_letter):
    """Parse 'Q? A. opt1 B. opt2 C. opt3' → (q_text, [A. opt1, B. opt2, ...], full_ans)."""
    raw = raw.strip()
    m = _OPT_START_RE.search(raw)
    if not m:
        return raw, [], answer_letter
    # Question text = mọi thứ trước marker
    split_pos = m.start(1)
    q_text = raw[:split_pos].rstrip(" ?:—-").strip()
    if not q_text.endswith(("?", ".", ":")):
        q_text += "?"
    rest = raw[split_pos:]
    # Split rest into options
    parts = re.split(r'(?:^|\s)([A-F])[.\)]\s+', rest)
    options = []
    # parts: ['', 'A', 'opt1...', 'B', 'opt2...', ...]
    for i in range(1, len(parts) - 1, 2):
        letter = parts[i]
        content = parts[i + 1].strip()
        # Trim trailing junk
        content = content.rstrip(",;").strip()
        options.append(f"{letter}. {content}")
    al = answer_letter.strip().upper()
    if al and al[0] in "ABCDEF":
        idx = ord(al[0]) - ord("A")
        if 0 <= idx < len(options):
            return q_text, options, options[idx]
    return q_text, options, answer_letter


def parse_match_options(context):
    """Parse 'Activities: A. opt1 / B. opt2 / ...' → list of options A. ... B. ..."""
    if not context:
        return []
    m = re.search(r'[A-F][.\)]', context)
    if not m:
        return []
    rest = context[m.start():]
    parts = re.split(r'(?:^|\s|/)([A-F])[.\)]\s+', rest)
    options = []
    for i in range(1, len(parts) - 1, 2):
        letter = parts[i]
        content = parts[i + 1].strip().rstrip(" /;,")
        # Cắt tại slash đầu tiên nếu options join bằng /
        if " / " in content:
            content = content.split(" / ")[0].strip()
        options.append(f"{letter}. {content}")
    return options


def build_listening_entries(de_no, parts):
    """Build list of dict entries cho phần listening của 1 đề."""
    entries = []
    for part_idx, part in enumerate(parts):
        part_label = part["part_label"]
        instruction = part["instruction"]
        context = part.get("context") or ""
        ptype = part["type"]
        items = part["items"]

        section_instruction = f"{part_label}. {instruction}".strip()
        section_start_val = "SECTION 1. LISTENING" if part_idx == 0 else None

        # passage_text giữ context nếu có và đáng kể
        passage_text = context.strip() if context and len(context.strip()) > 20 else None

        match_options = parse_match_options(context) if ptype == "match" else []

        # Cho part choice không có options text trong câu hỏi (picture-based / tick-box),
        # build placeholder A. (xem audio), B. (xem audio), ... đủ cho letter cao nhất trong items
        max_letter_idx = 1  # ít nhất A/B
        for it in items:
            a = str(it["answer"]).strip()
            if a and a[0].upper() in "ABCDEFGH":
                max_letter_idx = max(max_letter_idx, ord(a[0].upper()) - ord("A"))
        placeholder_opts = [f"{chr(65+i)}. (xem audio)" for i in range(max_letter_idx + 1)]

        for item_idx, item in enumerate(items):
            num = item["num"]
            raw_q = item["question_or_blank_text"].strip()
            raw_ans = str(item["answer"]).strip()
            # Bỏ prefix "(N) ", "(N): " nếu raw_q đã có sẵn để tránh "(1) ... (1) ___"
            raw_q = re.sub(rf"^\(?{num}\)?\s*[.:]?\s*", "", raw_q).strip()

            entry = {
                "type": "fill",
                "topic": "Listening",
                "section_start": section_start_val if (part_idx == 0 and item_idx == 0) else None,
                "section_instruction": section_instruction if item_idx == 0 else None,
                "passage_text": passage_text if item_idx == 0 else None,
                "q": "",
                "answer": "",
            }

            if ptype == "true_false":
                entry["type"] = "choice"
                entry["q"] = f"({num}) {raw_q}"
                entry["options"] = ["A. True", "B. False"]
                ans_norm = raw_ans.upper()[:1]
                entry["answer"] = "A. True" if ans_norm == "T" else "B. False"
            elif ptype == "choice":
                q_text, options, full_ans = parse_choice(raw_q, raw_ans)
                if not options:
                    options = placeholder_opts
                    al = raw_ans.strip().upper()[:1]
                    if al in "ABCDEFGH":
                        idx = ord(al) - ord("A")
                        if 0 <= idx < len(options):
                            full_ans = options[idx]
                entry["type"] = "choice"
                entry["q"] = f"({num}) {q_text}"
                entry["options"] = options
                entry["answer"] = full_ans
            elif ptype == "match":
                entry["type"] = "choice"
                entry["q"] = f"({num}) {raw_q}"
                entry["options"] = match_options
                al = raw_ans.strip().upper()[:1]
                if al and al in "ABCDEF":
                    idx = ord(al) - ord("A")
                    if 0 <= idx < len(match_options):
                        entry["answer"] = match_options[idx]
                    else:
                        entry["answer"] = raw_ans
                else:
                    entry["answer"] = raw_ans
            else:  # fill
                entry["type"] = "fill"
                entry["q"] = f"({num}) {raw_q}"
                entry["answer"] = raw_ans

            entries.append(entry)
    return entries


# ── render: dict → Python code string khớp style code hiện tại ───────────────
def jrepr(v):
    """JSON-style repr (double quotes, unicode preserved)."""
    return json.dumps(v, ensure_ascii=False)


def render_entry(d):
    """Multi-line Python dict literal, khớp style code hiện tại của HSG Anh 6."""
    key_order = ["type", "topic", "section_start", "section_instruction",
                 "passage_text", "q", "options", "answer"]
    pairs = []
    for k in key_order:
        if k not in d:
            continue
        v = d[k]
        if v is None:
            sv = "None"
        elif isinstance(v, list):
            sv = "[" + ", ".join(jrepr(x) for x in v) + "]"
        else:
            sv = jrepr(v)
        pairs.append((k, sv))

    if not pairs:
        return ""

    type_sv = dict(pairs)["type"]
    out = f'    {{"type": {type_sv}, "topic": "Listening",\n'
    middle = [p for p in pairs if p[0] not in ("type", "topic")]
    *mid, last = middle
    for k, sv in mid:
        out += f'     "{k}": {sv},\n'
    out += f'     "{last[0]}": {last[1]}}},\n'
    return out


# ── patch questions.py ──────────────────────────────────────────────────────
def split_entries(block_body):
    """Tách block (giữa `[` và `]`) thành list các entry string.

    Mỗi entry là 1 dict literal bắt đầu bằng `    {` và kết thúc bằng `    },`."""
    entries = []
    cur = []
    depth = 0
    for line in block_body.splitlines(keepends=True):
        cur.append(line)
        depth += line.count("{") - line.count("}")
        if depth == 0 and line.rstrip().endswith("},"):
            entries.append("".join(cur))
            cur = []
    if cur and "".join(cur).strip():
        entries.append("".join(cur))
    return entries


_DE_RE = re.compile(
    r"^(_HSG_ANH_DE_(\d+) = \[\n)(.*?)(^\]\n)",
    re.MULTILINE | re.DOTALL,
)


def patch_de(src, de_no, parts):
    """Patch listening section của 1 đề trong src. Return (new_src, replaced_n, kept_n)."""
    new_entries = build_listening_entries(de_no, parts)
    new_listening_text = "".join(render_entry(e) for e in new_entries)

    pat = re.compile(
        rf"^(_HSG_ANH_DE_{de_no} = \[\n)(.*?)(^\]\n)",
        re.MULTILINE | re.DOTALL,
    )
    m = pat.search(src)
    if not m:
        return src, 0, 0, "not_found"

    block_body = m.group(2)
    entries = split_entries(block_body)
    # Xác định prefix listening (đầu list) — giữ entries không phải Listening
    listening_count = 0
    keep_entries = []
    in_listening = True
    for e in entries:
        if in_listening and '"topic": "Listening"' in e:
            listening_count += 1
            continue
        in_listening = False
        keep_entries.append(e)

    new_block = m.group(1) + new_listening_text + "".join(keep_entries) + m.group(3)
    new_src = src[: m.start()] + new_block + src[m.end():]
    return new_src, listening_count, len(keep_entries), "ok"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="Không ghi questions.py, chỉ in report.")
    parser.add_argument("--only", type=int, default=0,
                        help="Chỉ patch đề số N (0 = all)")
    args = parser.parse_args()

    audit = load_audit()
    with open(QFILE, encoding="utf-8") as f:
        src = f.read()

    report = []
    for de_str in sorted(audit, key=int):
        de_no = int(de_str)
        if args.only and de_no != args.only:
            continue
        data = audit[de_str]
        parts = data.get("parts", [])
        if not parts:
            report.append((de_no, "no_parts", 0, 0))
            continue
        new_src, replaced, kept, status = patch_de(src, de_no, parts)
        report.append((de_no, status, replaced, kept))
        if status == "ok":
            src = new_src

    print(f"{'De':>3} {'Status':>10} {'Replaced':>10} {'Kept':>5}")
    for de_no, status, replaced, kept in report:
        print(f"{de_no:>3} {status:>10} {replaced:>10} {kept:>5}")

    if not args.dry_run:
        with open(QFILE, "w", encoding="utf-8") as f:
            f.write(src)
        print(f"\n✓ Wrote {QFILE}")
    else:
        print("\n(dry-run, không ghi file)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
