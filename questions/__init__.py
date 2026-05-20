"""Pool câu hỏi theo môn / chế độ.

Public API:
    - gen_exam, folder_display, folder_capacity
    - CONTENT_TREE
    - STUDENT_SUBJECTS, SUBJECT_ICONS, get_subjects
    - HSG_EXAM_NQ, HSG_EXAM_DURATIONS
    - HSG_ANH_EXAM_NQ, HSG_ANH_EXAM_DURATIONS

Cấu trúc mở rộng: thêm môn mới = thêm vào STUDENT_SUBJECTS + viết pool/generator riêng.
Thêm đề mới: thả vào module dữ liệu tương ứng (bao_meo / minh_khanh / nhat_khoi
/ hsg_toan_6 / hsg_anh_6) và (nếu cần) cập nhật _FOLDER_POOLS trong _core.py.
"""

from .subjects import STUDENT_SUBJECTS, SUBJECT_ICONS, get_subjects
from .content_tree import CONTENT_TREE
from .hsg_toan_6 import HSG_EXAM_DURATIONS, HSG_EXAM_NQ
from .hsg_anh_6 import HSG_ANH_EXAM_DURATIONS, HSG_ANH_EXAM_NQ
from ._core import (
    gen_exam,
    folder_display,
    folder_capacity,
    gen_hs_gioi,
    gen_mixed,
    gen_olympic,
)

__all__ = [
    "gen_exam",
    "folder_display",
    "folder_capacity",
    "gen_hs_gioi",
    "gen_mixed",
    "gen_olympic",
    "CONTENT_TREE",
    "STUDENT_SUBJECTS",
    "SUBJECT_ICONS",
    "get_subjects",
    "HSG_EXAM_DURATIONS",
    "HSG_EXAM_NQ",
    "HSG_ANH_EXAM_DURATIONS",
    "HSG_ANH_EXAM_NQ",
]
