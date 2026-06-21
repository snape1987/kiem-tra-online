"""Apply HSG Anh 6 listening + writing essay fixes from audit JSON files.

Rewrite questions.py listening sections + thêm entries type='essay' cho 36 đề HSG Anh 6
dựa trên DOC gốc trên Drive.

Schema JSON (mới):
  {
    "listening_parts": [
      {"part_label", "instruction", "context_or_table", "type" (fill/true_false/choice/match), "items": [...]},
    ],
    "writing_essays": [
      {"label", "prompt_text", "word_min", "word_max", "suggested_lines", "marking_notes"},
    ],
  }

Cách dùng:
    python -m tools.apply_anh6_listening --dry-run
    python -m tools.apply_anh6_listening
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
    os.path.join(ROOT, "tools/anh6_audit_de_28_36.json"),
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
    raw = raw.strip()
    m = _OPT_START_RE.search(raw)
    if not m:
        return raw, [], answer_letter
    split_pos = m.start(1)
    q_text = raw[:split_pos].rstrip(" ?:—-").strip()
    if not q_text.endswith(("?", ".", ":")):
        q_text += "?"
    rest = raw[split_pos:]
    parts = re.split(r'(?:^|\s)([A-F])[.\)]\s+', rest)
    options = []
    for i in range(1, len(parts) - 1, 2):
        letter = parts[i]
        content = parts[i + 1].strip().rstrip(",;").strip()
        options.append(f"{letter}. {content}")
    al = answer_letter.strip().upper()
    if al and al[0] in "ABCDEF":
        idx = ord(al[0]) - ord("A")
        if 0 <= idx < len(options):
            return q_text, options, options[idx]
    return q_text, options, answer_letter


def parse_match_options(context):
    if not context:
        return []
    m = re.search(r'[A-F][.\)]', context)
    if not m:
        return []
    rest = context[m.start():]
    parts = re.split(r'(?:^|\s|/|;)([A-F])[.\)]\s+', rest)
    options = []
    for i in range(1, len(parts) - 1, 2):
        letter = parts[i]
        content = parts[i + 1].strip().rstrip(" /;,")
        if " / " in content:
            content = content.split(" / ")[0].strip()
        if "; " in content:
            content = content.split("; ")[0].strip()
        options.append(f"{letter}. {content}")
    return options


def _calc_essay_lines(word_min, word_max, suggested):
    if suggested:
        return int(suggested)
    target = word_max or word_min or 120
    # ~8 từ/dòng cho học sinh lớp 6
    return max(10, (target // 8) + 4)


def build_listening_entries(de_no, listening_parts):
    """Build list of dict entries cho phần listening của 1 đề."""
    entries = []
    for part_idx, part in enumerate(listening_parts):
        part_label = part["part_label"]
        instruction = part["instruction"]
        context = part.get("context_or_table") or ""
        ptype = part["type"]
        items = part["items"]

        section_instruction = f"{part_label}. {instruction}".strip()
        section_start_val = "SECTION 1. LISTENING" if part_idx == 0 else None
        passage_text = context.strip() if context and len(context.strip()) > 20 else None

        match_options = parse_match_options(context) if ptype == "match" else []

        # Cho choice không có options text trong câu hỏi (picture-based / tick-box)
        max_letter_idx = 1
        for it in items:
            a = str(it.get("answer_from_doc_key", "")).strip()
            if a and a[0].upper() in "ABCDEFGH":
                max_letter_idx = max(max_letter_idx, ord(a[0].upper()) - ord("A"))
        placeholder_opts = [f"{chr(65+i)}. (xem audio)" for i in range(max_letter_idx + 1)]

        for item_idx, item in enumerate(items):
            num = item["num"]
            raw_q = (item.get("question_text_from_doc") or "").strip()
            raw_ans = str(item.get("answer_from_doc_key", "")).strip()
            # Picture-only items có raw_q=null hoặc rỗng
            if not raw_q:
                raw_q = f"Câu {num} (nghe audio)"
            # Bỏ prefix "(N) " hoặc "N." nếu raw_q đã có
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
                # Phân loại theo dạng đáp án
                ans_stripped = raw_ans.strip()
                is_tick = (ans_stripped in ("✔", "✘") or
                           "tick" in ans_stripped.lower() or
                           "không" in ans_stripped.lower())
                is_letter = (len(ans_stripped) <= 2 and ans_stripped
                             and ans_stripped[0].upper() in "ABCDEF")
                if is_tick:
                    entry["options"] = ["A. ✔ (Có)", "B. ✘ (Không có)"]
                    if "✔" in ans_stripped or ans_stripped.lower() in ("tick", "ticked", "yes", "có"):
                        entry["answer"] = "A. ✔ (Có)"
                    else:
                        entry["answer"] = "B. ✘ (Không có)"
                elif is_letter:
                    opts = match_options or placeholder_opts
                    entry["options"] = opts
                    idx = ord(ans_stripped[0].upper()) - ord("A")
                    entry["answer"] = opts[idx] if 0 <= idx < len(opts) else ans_stripped
                else:
                    # Value-based match (vd speaker names Phong/Vy/Mai/Duy)
                    candidates = []
                    for it in items:
                        a = (it.get("answer_from_doc_key") or "").strip()
                        if a and a not in candidates:
                            candidates.append(a)
                    # Bổ sung từ context (vd "Speakers: Phong, Vy, Mai, Duy")
                    if context:
                        ctx_m = re.search(r"(?:Speakers?|Names?|People|People list)[:\s]+([^\.\n]+)",
                                          context, re.IGNORECASE)
                        if ctx_m:
                            for n in ctx_m.group(1).split(","):
                                n = n.strip().rstrip(".").rstrip(";")
                                if n and n not in candidates and 0 < len(n) < 25:
                                    candidates.append(n)
                    candidates = sorted(set(candidates))
                    opts = [f"{chr(65+i)}. {v}" for i, v in enumerate(candidates)]
                    entry["options"] = opts
                    matched = None
                    for opt in opts:
                        if opt.split(".", 1)[1].strip().lower() == ans_stripped.lower():
                            matched = opt
                            break
                    entry["answer"] = matched or (opts[0] if opts else ans_stripped)
            else:  # fill
                entry["type"] = "fill"
                entry["q"] = f"({num}) {raw_q}"
                entry["answer"] = raw_ans

            entries.append(entry)
    return entries


def build_essay_entries(writing_essays):
    """Build list of dict entries cho phần viết luận (type='essay')."""
    entries = []
    for idx, essay in enumerate(writing_essays):
        prompt = (essay.get("prompt_text") or "").strip()
        if not prompt:
            continue
        word_min = essay.get("word_min")
        word_max = essay.get("word_max")
        lines = _calc_essay_lines(word_min, word_max, essay.get("suggested_lines"))
        label = essay.get("label") or f"Essay {idx + 1}"

        if word_min and word_max:
            hint = f"Viết khoảng {word_min}-{word_max} từ"
        elif word_max:
            hint = f"Viết tối đa {word_max} từ"
        elif word_min:
            hint = f"Viết ít nhất {word_min} từ"
        else:
            hint = "Viết một đoạn văn theo gợi ý"

        section_start = "SECTION 5. WRITING (Essay)" if idx == 0 else None
        section_instr = f"Phần viết luận. {hint}." if idx == 0 else None

        entry = {
            "type": "essay",
            "topic": "Writing",
            "section_start": section_start,
            "section_instruction": section_instr,
            "passage_text": None,
            "q": f"{label}. {prompt}",
            "essay_lines": lines,
            "essay_word_min": word_min,
            "essay_word_max": word_max,
            "answer": "(Bài viết tự do — tự chấm tay)",
        }
        entries.append(entry)
    return entries


# ── render: dict → Python code string khớp style code hiện tại ───────────────
def jrepr(v):
    return json.dumps(v, ensure_ascii=False)


def render_entry(d):
    key_order = ["type", "topic", "section_start", "section_instruction",
                 "passage_text", "q", "options", "essay_lines",
                 "essay_word_min", "essay_word_max", "answer"]
    pairs = []
    for k in key_order:
        if k not in d:
            continue
        v = d[k]
        if v is None:
            sv = "None"
        elif isinstance(v, list):
            sv = "[" + ", ".join(jrepr(x) for x in v) + "]"
        elif isinstance(v, (int, float)):
            sv = str(v)
        else:
            sv = jrepr(v)
        pairs.append((k, sv))

    if not pairs:
        return ""

    type_sv = dict(pairs)["type"]
    out = f'    {{"type": {type_sv}, "topic": {dict(pairs).get("topic", chr(34)+"Unknown"+chr(34))},\n'
    middle = [p for p in pairs if p[0] not in ("type", "topic")]
    if not middle:
        return out.rstrip(",\n") + "},\n"
    *mid, last = middle
    for k, sv in mid:
        out += f'     "{k}": {sv},\n'
    out += f'     "{last[0]}": {last[1]}}},\n'
    return out


# ── patch questions.py ──────────────────────────────────────────────────────
def split_entries(block_body):
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


def patch_de(src, de_no, data):
    """Replace listening prefix + remove existing essay + append new essay entries."""
    listening_parts = data.get("listening_parts", [])
    writing_essays = data.get("writing_essays", [])

    new_listening = build_listening_entries(de_no, listening_parts)
    new_essays = build_essay_entries(writing_essays)
    new_listening_text = "".join(render_entry(e) for e in new_listening)
    new_essays_text = "".join(render_entry(e) for e in new_essays)

    pat = re.compile(
        rf"^(_HSG_ANH_DE_{de_no} = \[\n)(.*?)(^\]\n)",
        re.MULTILINE | re.DOTALL,
    )
    m = pat.search(src)
    if not m:
        return src, 0, 0, 0, "not_found"

    block_body = m.group(2)
    entries = split_entries(block_body)

    listening_count = 0
    essay_count_removed = 0
    keep_entries = []
    in_listening_prefix = True
    for e in entries:
        if in_listening_prefix and '"topic": "Listening"' in e:
            listening_count += 1
            continue
        in_listening_prefix = False
        if '"type": "essay"' in e or '"topic": "Writing"' in e and '"type": "essay"' in e:
            essay_count_removed += 1
            continue
        keep_entries.append(e)

    new_block = (
        m.group(1)
        + new_listening_text
        + "".join(keep_entries)
        + new_essays_text
        + m.group(3)
    )
    new_src = src[: m.start()] + new_block + src[m.end():]
    return new_src, listening_count, essay_count_removed, len(new_essays), "ok"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", type=int, default=0)
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
        new_src, lst_n, ess_rem, ess_add, status = patch_de(src, de_no, data)
        report.append((de_no, status, lst_n, ess_rem, ess_add))
        if status == "ok":
            src = new_src

    print(f"{'De':>3} {'Status':>10} {'L_repl':>7} {'E_rm':>5} {'E_add':>6}")
    for de_no, status, lst_n, ess_rem, ess_add in report:
        print(f"{de_no:>3} {status:>10} {lst_n:>7} {ess_rem:>5} {ess_add:>6}")

    if not args.dry_run:
        with open(QFILE, "w", encoding="utf-8") as f:
            f.write(src)
        print(f"\n✓ Wrote {QFILE}")
    else:
        print("\n(dry-run, không ghi file)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
