"""Engine: gen_exam, gen_hs_gioi/mixed/olympic, folder_capacity/display, _FOLDER_POOLS."""
import random

from .subjects import _placeholder
from ._english import gen_english_structured
from .bao_meo import (
    _gen_bao_meo_pool,
    BAO_MEO_POOL,
    BAO_MEO_FULL_POOL,
    BAO_MEO_VIOLYMPIC,
)
from .minh_khanh import MINH_KHANH_TOAN, MINH_KHANH_TIENG_ANH
from .nhat_khoi import NHAT_KHOI_TOAN, NHAT_KHOI_TIENG_ANH, NHAT_KHOI_TOAN_LOP7
from .hsg_toan_6 import MINH_KHANH_TOAN_HSG, _HSG_TOAN_6_EXAMS
from .hsg_anh_6 import _HSG_ANH_6_EXAMS
from .content_tree import CONTENT_TREE


def _get_pool(student_key, subject):
    """Trả về pool câu hỏi của bé theo môn."""
    if student_key == "minh_khanh":
        return MINH_KHANH_TOAN if subject == "Toán" else MINH_KHANH_TIENG_ANH
    if student_key == "nhat_khoi":
        return NHAT_KHOI_TOAN if subject == "Toán" else NHAT_KHOI_TIENG_ANH
    return []  # bao_meo dùng generators, không dùng pool tĩnh


def folder_capacity(lop_key, folder_key):
    """Max questions achievable for this folder (used to filter duration options in UI)."""
    if lop_key == "lop_1" and folder_key == "de_hk2_toan_1":
        return 9999  # generator-based, unlimited
    if folder_key in ("de_hsg_toan_6", "de_hsg_anh_6"):
        return 9999  # UI hides dur-row for HSG; capacity unused
    pool = _FOLDER_POOLS.get((lop_key, folder_key), [])
    if not pool:
        return 0
    return len(pool)


def gen_hs_gioi(n=10, seed=None, student_key="bao_meo", subject="Toán"):
    """Sinh n câu HS Giỏi theo từng bé."""
    if seed is not None:
        random.seed(seed)
    if student_key == "bao_meo":
        gen_n = max(1, n // 2)
        static_n = n - gen_n
        gen_part = _gen_bao_meo_pool(gen_n)
        static_pool = list(BAO_MEO_FULL_POOL)
        random.shuffle(static_pool)
        combined = gen_part + static_pool[:static_n]
        random.shuffle(combined)
        return combined
    pool = _get_pool(student_key, subject)
    if not pool:
        return _placeholder(n, student_key, subject, "HS Giỏi")
    if subject == "Tiếng Anh":
        return gen_english_structured(pool, n, seed)
    result = list(pool)
    random.shuffle(result)
    return result[:n]


def gen_mixed(n=15, seed=None, student_key="bao_meo", subject="Toán"):
    """Kết hợp HS Giỏi + câu khó hơn theo từng bé."""
    if seed is not None:
        random.seed(seed)
    if student_key == "bao_meo":
        gen_n = n // 3
        static_n = n - gen_n
        part1 = _gen_bao_meo_pool(gen_n)
        part2 = list(BAO_MEO_FULL_POOL)
        random.shuffle(part2)
        combined = part1 + part2[:static_n]
        random.shuffle(combined)
        return combined
    pool = _get_pool(student_key, subject)
    if not pool:
        return _placeholder(n, student_key, subject, "HS Giỏi + Olympic")
    if subject == "Tiếng Anh":
        return gen_english_structured(pool, n, seed)
    result = list(pool)
    random.shuffle(result)
    return result[:n]


def gen_olympic(n=10, seed=None, student_key="bao_meo", subject="Toán"):
    """Đề Thi Olympic theo từng bé — thêm câu hỏi khi có nội dung."""
    pool = _get_pool(student_key, subject)
    if student_key == "bao_meo":
        pool = list(BAO_MEO_VIOLYMPIC)
    if not pool:
        return _placeholder(n, student_key, subject, "Olympic")
    if seed is not None:
        random.seed(seed)
    if subject == "Tiếng Anh":
        return gen_english_structured(pool, n, seed)
    result = list(pool)
    random.shuffle(result)
    return result[:n]


_TIENG_ANH_FOLDERS = {"de_tieng_anh_6_hk2", "tieng_anh_7_hk1"}

_FOLDER_POOLS = {
    ("lop_1", "toan_violympic_1"):    BAO_MEO_VIOLYMPIC,
    ("lop_6", "de_toan_6_hk2"):       MINH_KHANH_TOAN,
    ("lop_6", "de_olympic_toan_6"):   MINH_KHANH_TOAN,
    ("lop_6", "de_hsg_toan_6"):       MINH_KHANH_TOAN_HSG,
    ("lop_6", "de_tieng_anh_6_hk2"):  MINH_KHANH_TIENG_ANH,
    ("lop_7", "toan_7_hk1"):          NHAT_KHOI_TOAN_LOP7,
    ("lop_7", "tieng_anh_7_hk1"):     NHAT_KHOI_TIENG_ANH,
    ("lop_8", "toan_8_hk2"):          NHAT_KHOI_TOAN,
}


def folder_display(lop_key, folder_key):
    for lk, _, folders in CONTENT_TREE:
        if lk == lop_key:
            for fk, fname in folders:
                if fk == folder_key:
                    return fname
    return folder_key


def gen_exam(lop_key, folder_key, n=15, seed=None, exam_no=1):
    """Sinh n câu cho lop_key + folder_key."""
    if seed is not None:
        random.seed(seed)

    # HSG Toán 6: mỗi đề_no = toàn bộ câu của 1 PDF (không random subset)
    if folder_key == "de_hsg_toan_6":
        pool = _HSG_TOAN_6_EXAMS.get(exam_no or 1, [])
        result = list(pool)
        random.shuffle(result)
        return result

    # HSG Anh 6: giữ nguyên thứ tự (Listening → Phonetics → Grammar → Reading)
    if folder_key == "de_hsg_anh_6":
        pool = _HSG_ANH_6_EXAMS.get(exam_no or 1, [])
        if not pool:
            return _placeholder(1, "", "Tiếng Anh", f"Đề HSG Anh 6 — Đề {exam_no or 1}")
        return list(pool)

    # Lớp 1 — HK2: mix generators + static pool
    if lop_key == "lop_1" and folder_key == "de_hk2_toan_1":
        gen_n = max(1, n // 3)
        static_n = n - gen_n
        part1 = _gen_bao_meo_pool(gen_n, seed=seed)
        part2 = list(BAO_MEO_POOL)
        random.shuffle(part2)
        result = part1 + part2[:static_n]
        random.shuffle(result)
        return result

    pool = _FOLDER_POOLS.get((lop_key, folder_key), [])

    if not pool:
        name = folder_display(lop_key, folder_key)
        return _placeholder(1, "", name, name)

    if folder_key in _TIENG_ANH_FOLDERS:
        return gen_english_structured(pool, n, seed)

    result = list(pool)
    random.shuffle(result)
    return result[:n]
