"""Trích xuất câu hỏi trắc nghiệm từ markdown.

Layer 1: Regex (nhanh, miễn phí) — nhận diện format chuẩn A/B/C/D.
Layer 2: Claude API fallback — khi regex trả < 5 câu.
"""
import json
import re

from agent.config import ANTHROPIC_API_KEY, CLAUDE_MODEL, NQ_BY_TYPE

# ── Regex parser ──────────────────────────────────────────────────────────────
# Nhận diện các pattern:
#   "Câu 1: ..." hoặc "1." hoặc "Bài 1."
#   "A. ..." "B. ..." "C. ..." "D. ..."
#   "Đáp án: A" hoặc "ĐÁP ÁN: B" hoặc "Đ/A: C"

_Q_START   = re.compile(
    r"^(?:câu|bài|question)?\s*\d+[\.\)]\s*(.+)", re.I | re.M
)
_OPT       = re.compile(r"^([A-D])[\.\)]\s*(.+)", re.M)
_ANSWER_LINE = re.compile(
    r"(?:đáp\s*án|answer|đ/a)[:\s]+([A-D])", re.I
)
_ANSWER_KEY_BLOCK = re.compile(
    r"(?:đáp\s*án|answer key)[^\n]*\n((?:\d+[\.\)]\s*[A-D]\s*\n?)+)", re.I
)


def _parse_answer_key(text: str) -> dict[int, str]:
    """Tách bảng đáp án cuối trang: '1. A  2. B  3. C ...' → {1:'A', 2:'B', ...}"""
    key_map: dict[int, str] = {}
    block_m = _ANSWER_KEY_BLOCK.search(text)
    block = block_m.group(1) if block_m else text
    for m in re.finditer(r"(\d+)[\.\)]\s*([A-D])", block):
        key_map[int(m.group(1))] = m.group(2)
    return key_map


def _regex_extract(markdown: str, folder_type: str) -> list[dict]:
    """Trích xuất câu hỏi trắc nghiệm bằng regex."""
    lines   = markdown.split("\n")
    results = []
    answer_key = _parse_answer_key(markdown)

    i        = 0
    q_index  = 0
    while i < len(lines):
        line = lines[i].strip()
        qm = re.match(r"^(?:câu|bài|question)?\s*(\d+)[\.\)]\s*(.+)", line, re.I)
        if not qm:
            i += 1
            continue

        q_no   = int(qm.group(1))
        q_text = qm.group(2).strip()
        # Tiếp tục nếu câu hỏi kéo nhiều dòng (chưa gặp A.)
        i += 1
        while i < len(lines):
            peek = lines[i].strip()
            if re.match(r"^[A-D][\.\)]", peek) or re.match(r"^(?:câu|bài|\d+[\.\)])", peek, re.I):
                break
            q_text += " " + peek
            i += 1

        q_text = q_text.strip()
        if len(q_text) < 5:
            continue

        # Đọc options A B C D
        options = {}
        while i < len(lines):
            peek = lines[i].strip()
            om = re.match(r"^([A-D])[\.\)]\s*(.+)", peek)
            if om:
                options[om.group(1)] = om.group(2).strip()
                i += 1
            else:
                break

        if len(options) < 2:
            continue   # không phải câu trắc nghiệm

        # Tìm đáp án
        answer_letter = answer_key.get(q_no)
        if not answer_letter:
            # Tìm inline "Đáp án: A"
            look_ahead = "\n".join(lines[i:i+3])
            am = _ANSWER_LINE.search(look_ahead)
            if am:
                answer_letter = am.group(1).upper()

        if not answer_letter or answer_letter not in options:
            # Đáp án không xác định — bỏ qua câu này
            continue

        opts_list = [f"{k}. {v}" for k, v in sorted(options.items())]
        answer_full = f"{answer_letter}. {options[answer_letter]}"

        results.append({
            "type":       "choice",
            "q":          q_text,
            "options":    opts_list,
            "answer":     answer_full,
            "topic":      _guess_topic(q_text, folder_type),
            "confidence": 0.9,
        })
        q_index += 1

    return results


def _guess_topic(q_text: str, folder_type: str) -> str:
    """Đoán chủ đề đơn giản từ text."""
    lower = q_text.lower()
    if any(w in lower for w in ("hình", "tam giác", "vuông", "chu vi", "diện tích")):
        return "Hình học"
    if any(w in lower for w in ("phân số", "chia", "nhân", "cộng", "trừ", "tính")):
        return "Số học"
    if any(w in lower for w in ("bài toán", "có", "hỏi", "tổng", "hiệu")):
        return "Toán đố"
    if any(w in lower for w in ("grammar", "tense", "verb", "noun", "adj")):
        return "Grammar"
    if any(w in lower for w in ("đọc", "reading", "passage")):
        return "Reading"
    return ""


# ── Claude API fallback ───────────────────────────────────────────────────────

_EXTRACT_PROMPT = """\
Bạn là trợ lý trích xuất đề thi. Đọc nội dung markdown dưới đây (đề thi Việt Nam),
trích xuất TẤT CẢ câu hỏi trắc nghiệm có đủ 4 lựa chọn A/B/C/D VÀ đáp án đúng.

Trả về JSON array, mỗi phần tử gồm:
{
  "q": "<nội dung câu hỏi, không có số thứ tự>",
  "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
  "answer": "<đáp án đúng, vd: A. Hà Nội>",
  "topic": "<chủ đề nếu biết, vd: Hình học, Grammar, Reading>"
}

Quy tắc:
- Chỉ lấy câu có đủ options A B C D VÀ đáp án rõ ràng.
- Không bịa đáp án. Nếu không tìm được đáp án, bỏ câu đó.
- Không lấy câu tự luận, câu điền số không có lựa chọn.
- Trả về JSON thuần túy, không markdown, không giải thích.

MARKDOWN:
"""


def _claude_extract(markdown: str) -> list[dict]:
    """Gọi Claude API để extract câu hỏi. Trả [] nếu lỗi."""
    if not ANTHROPIC_API_KEY:
        return []
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        # Cắt markdown nếu quá dài (tiết kiệm token)
        text = markdown[:12000]
        msg  = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=4096,
            messages=[{"role": "user", "content": _EXTRACT_PROMPT + text}],
        )
        raw = msg.content[0].text.strip()
        # Tìm JSON array trong response
        m = re.search(r"\[.*\]", raw, re.S)
        if not m:
            return []
        data = json.loads(m.group())
        results = []
        for item in data:
            if not isinstance(item, dict):
                continue
            if not item.get("q") or not item.get("answer") or not item.get("options"):
                continue
            item["type"]       = "choice"
            item["confidence"] = 0.85
            item.setdefault("topic", "")
            results.append(item)
        return results
    except Exception:
        return []


# ── Public interface ──────────────────────────────────────────────────────────

def extract_questions(markdown: str, folder_type: str,
                      target_n: int | None = None) -> list[dict]:
    """Trích xuất câu hỏi từ markdown — regex trước, Claude fallback.

    Args:
        markdown:    Nội dung markdown của đề thi.
        folder_type: hk1 / hk2 / hsg / violympic (để đoán topic).
        target_n:    Số câu cần (từ NQ_BY_TYPE). None = lấy hết.

    Returns:
        List câu hỏi dạng dict tương thích với questions_pool.
    """
    if target_n is None:
        target_n = NQ_BY_TYPE.get(folder_type, 20)

    # Layer 1: Regex
    questions = _regex_extract(markdown, folder_type)

    # Layer 2: Claude fallback nếu regex ra quá ít
    if len(questions) < 5:
        questions = _claude_extract(markdown)

    # Deduplicate theo q text
    seen = set()
    unique = []
    for q in questions:
        norm = q["q"].strip().lower()
        if norm not in seen:
            seen.add(norm)
            unique.append(q)

    return unique
