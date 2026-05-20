"""Cấu trúc đề Tiếng Anh: chia theo Part (Phonetics, Language, Reading, Writing)."""
import random

_ENGLISH_SECTIONS = [
    ("Pronunciation",              "PART I – PHONETICS",  "Choose the word whose underlined part is pronounced differently from the others."),
    (("Grammar", "Vocabulary", "Communication"), "PART II – LANGUAGE",  "Choose the best answer A, B, C, or D to complete each sentence."),
    (("Reading", "Reading T/F"),   "PART III – READING",  "Read and choose the correct answer (T/F) or the best option."),
    ("Word Form",                  "PART IV – WRITING",   "Write the correct form of the word given in brackets."),
]

_ENGLISH_TARGETS = [3, 10, 5, 4]  # phonetics, language, reading, writing


def _keep_passages_together(qs, rng):
    """Shuffle question groups but keep same passage_id consecutive."""
    by_pid = {}
    no_pid = []
    for q in qs:
        pid = q.get("passage_id")
        if pid:
            by_pid.setdefault(pid, []).append(q)
        else:
            no_pid.append(q)
    groups = list(by_pid.values()) + [[q] for q in no_pid]
    rng.shuffle(groups)
    result = []
    for g in groups:
        result.extend(g)
    return result


def gen_english_structured(pool, n, seed):
    """Return a structured English exam with Part headers (section_start field)."""
    rng = random.Random(seed)

    groups = []
    for topics, *_ in _ENGLISH_SECTIONS:
        if isinstance(topics, str):
            bucket = [q for q in pool if q.get("topic") == topics]
        else:
            bucket = [q for q in pool if q.get("topic") in topics]
        bucket = _keep_passages_together(bucket, rng)
        groups.append(bucket)

    available = [len(g) for g in groups]
    total_available = sum(available)
    actual_n = min(n, total_available)
    if actual_n == 0:
        return []

    # Scale targets proportionally; sections with 0 available get 0
    total_default = sum(_ENGLISH_TARGETS)
    targets = []
    for avail, t in zip(available, _ENGLISH_TARGETS):
        if avail == 0:
            targets.append(0)
        else:
            targets.append(max(1, round(t * actual_n / total_default)))
    targets = [min(t, avail) for t, avail in zip(targets, available)]

    # Redistribute to hit actual_n exactly
    while sum(targets) > actual_n:
        i = max((i for i in range(len(targets)) if targets[i] > 0),
                key=lambda i: targets[i])
        targets[i] -= 1
    while sum(targets) < actual_n:
        headroom = [avail - t for avail, t in zip(available, targets)]
        i = max(range(len(headroom)), key=lambda i: headroom[i])
        if headroom[i] <= 0:
            break
        targets[i] += 1

    result = []
    for bucket, (_, title, instruction), target in zip(groups, _ENGLISH_SECTIONS, targets):
        if target == 0:
            continue
        picked = bucket[:target]
        if not picked:
            continue
        first = dict(picked[0])
        first["section_start"] = title
        first["section_instruction"] = instruction
        result.append(first)
        result.extend(picked[1:])
    return result
