"""Môn học, icon, placeholder cho mỗi học sinh."""

STUDENT_SUBJECTS = {
    "bao_meo":    ["Toán"],
    "minh_khanh": ["Toán", "Tiếng Anh"],
    "nhat_khoi":  ["Toán", "Tiếng Anh"],
}

SUBJECT_ICONS = {
    "Toán":       "📐",
    "Tiếng Việt": "📖",
    "Tiếng Anh":  "🇬🇧",
    "Vật Lý":     "⚡",
    "Hóa Học":    "🧪",
}


def get_subjects(student_key):
    return STUDENT_SUBJECTS.get(student_key, ["Toán"])


_STUDENT_NAMES = {
    "bao_meo":    "Bảo Mèo (Lớp 1D)",
    "minh_khanh": "Minh Khanh (Lớp 6A3)",
    "nhat_khoi":  "Nhật Khôi (Lớp 8A1)",
}


def _placeholder(n, student_key, subject, mode_name):
    """Trả về placeholder khi chưa có đề thực."""
    name = _STUDENT_NAMES.get(student_key, student_key)
    return [{
        "type": "fill",
        "q": f"[{subject} — {mode_name}] Chưa có câu hỏi cho {name}. Thêm vào questions.py!",
        "answer": "0",
        "topic": subject,
    }]
