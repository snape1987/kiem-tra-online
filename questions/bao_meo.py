"""Bảo Mèo — Lớp 1: generators + pools đề HK + Violympic."""
import random

# ─── Generators (định nghĩa sớm để _BAO_MEO_GENERATORS bắt được) ──────────
def _gen_cong_khong_nho():
    a = random.randint(10, 80)
    b = random.randint(1, 99 - a)
    while (a % 10 + b % 10) >= 10:
        b = random.randint(1, 99 - a)
    ans = a + b
    return {
        "type": "fill",
        "q": f"{a} + {b} = ?",
        "answer": str(ans),
        "topic": "Cộng không nhớ",
    }


def _gen_tru_khong_nho():
    a = random.randint(20, 99)
    b = random.randint(1, a)
    while (a % 10) < (b % 10):
        b = random.randint(1, a)
    ans = a - b
    return {
        "type": "fill",
        "q": f"{a} − {b} = ?",
        "answer": str(ans),
        "topic": "Trừ không nhớ",
    }


def _gen_so_sanh():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    while a == b:
        b = random.randint(10, 99)
    ans = "<" if a < b else (">" if a > b else "=")
    return {
        "type": "choice",
        "q": f"Điền dấu thích hợp: {a} ___ {b}",
        "options": ["<", ">", "="],
        "answer": ans,
        "topic": "So sánh số",
    }


def _gen_doc_so():
    chuc = random.randint(2, 9)
    donvi = random.randint(0, 9)
    n = chuc * 10 + donvi
    cach_doc = {
        0: "không", 1: "một", 2: "hai", 3: "ba", 4: "tư",
        5: "lăm" if donvi == 5 and chuc != 1 else "năm",
        6: "sáu", 7: "bảy", 8: "tám", 9: "chín",
    }
    chuc_doc = {
        2: "Hai", 3: "Ba", 4: "Bốn", 5: "Năm",
        6: "Sáu", 7: "Bảy", 8: "Tám", 9: "Chín",
    }
    if donvi == 0:
        correct = f"{chuc_doc[chuc]} mươi"
    elif donvi == 1:
        correct = f"{chuc_doc[chuc]} mươi mốt"
    elif donvi == 5:
        correct = f"{chuc_doc[chuc]} mươi lăm"
    else:
        correct = f"{chuc_doc[chuc]} mươi {cach_doc[donvi]}"

    distractors = []
    for _ in range(3):
        d = random.randint(10, 99)
        distractors.append(str(d))
    options = [str(n)] + [str(abs(n + random.choice([-9, -1, 1, 9, 11]))) for _ in range(3)]
    options = [o for o in options if o.isdigit() and 10 <= int(o) <= 99]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        cand = str(random.randint(10, 99))
        if cand not in options:
            options.append(cand)
    options = options[:4]
    random.shuffle(options)
    return {
        "type": "choice",
        "q": f'Số "{correct}" được viết là:',
        "options": options,
        "answer": str(n),
        "topic": "Đọc - viết số",
    }


def _gen_tron_chuc():
    nums = random.sample(range(11, 99), 4)
    pos = random.randint(0, 3)
    nums[pos] = random.choice([20, 30, 40, 50, 60, 70, 80, 90])
    options = [str(x) for x in nums]
    return {
        "type": "choice",
        "q": "Trong các số sau, số nào là số tròn chục?",
        "options": options,
        "answer": str(nums[pos]),
        "topic": "Số tròn chục",
    }


def _gen_do_dai_cm():
    a = random.randint(10, 80)
    b = random.randint(1, 19)
    op = random.choice(["+", "-"])
    if op == "+":
        ans = a + b
    else:
        ans = a - b
    return {
        "type": "fill",
        "q": f"{a}cm {op} {b}cm = ? cm",
        "answer": str(ans),
        "topic": "Đo độ dài cm",
    }


def _gen_so_lon_nhat():
    nums = random.sample(range(10, 100), 4)
    return {
        "type": "choice",
        "q": f"Trong các số {', '.join(map(str, nums))}, số lớn nhất là:",
        "options": [str(x) for x in nums],
        "answer": str(max(nums)),
        "topic": "Tìm số lớn nhất",
    }


def _gen_so_be_nhat():
    nums = random.sample(range(10, 100), 4)
    return {
        "type": "choice",
        "q": f"Trong các số {', '.join(map(str, nums))}, số bé nhất là:",
        "options": [str(x) for x in nums],
        "answer": str(min(nums)),
        "topic": "Tìm số bé nhất",
    }


def _gen_loi_van_cong():
    a = random.randint(10, 50)
    b = random.randint(5, 49 - (a % 10))
    while (a % 10 + b % 10) >= 10:
        b = random.randint(1, 49 - (a % 10))
    ans = a + b
    objs = random.choice(["quả táo", "viên kẹo", "cái bút", "bông hoa", "con cá"])
    return {
        "type": "fill",
        "q": f"An có {a} {objs}, Bình cho An thêm {b} {objs}. Hỏi An có tất cả bao nhiêu {objs}?",
        "answer": str(ans),
        "topic": "Toán lời văn (cộng)",
    }


def _gen_loi_van_tru():
    a = random.randint(20, 90)
    b = random.randint(5, a - 1)
    while (a % 10) < (b % 10):
        b = random.randint(1, a - 1)
    ans = a - b
    objs = random.choice(["quả cam", "cái bánh", "viên bi", "tờ giấy"])
    return {
        "type": "fill",
        "q": f"Mai có {a} {objs}, Mai cho bạn {b} {objs}. Hỏi Mai còn lại bao nhiêu {objs}?",
        "answer": str(ans),
        "topic": "Toán lời văn (trừ)",
    }


def _gen_dem_chuc_donvi():
    chuc = random.randint(2, 9)
    donvi = random.randint(1, 9)
    n = chuc * 10 + donvi
    distractors = [donvi * 10 + chuc, n + 9, n - 9]
    options = [str(n)] + [str(x) for x in distractors]
    options = list(dict.fromkeys(options))[:4]
    while len(options) < 4:
        options.append(str(random.randint(10, 99)))
    random.shuffle(options)
    return {
        "type": "choice",
        "q": f"Số gồm {chuc} chục và {donvi} đơn vị được viết là:",
        "options": options,
        "answer": str(n),
        "topic": "Cấu tạo số",
    }


def _gen_xem_gio():
    h = random.randint(1, 12)
    options = list({h, (h % 12) + 1, ((h - 2) % 12) + 1, ((h + 5) % 12) + 1})[:4]
    while len(options) < 4:
        x = random.randint(1, 12)
        if x not in options:
            options.append(x)
    options_str = [f"{x} giờ" for x in options]
    random.shuffle(options_str)
    return {
        "type": "choice",
        "q": f"Kim ngắn chỉ vào số {h}, kim dài chỉ vào số 12. Đồng hồ chỉ mấy giờ?",
        "options": options_str,
        "answer": f"{h} giờ",
        "topic": "Xem giờ đúng",
    }


_BAO_MEO_GENERATORS = [
    lambda: _gen_cong_khong_nho(),
    lambda: _gen_tru_khong_nho(),
    lambda: _gen_so_sanh(),
    lambda: _gen_doc_so(),
    lambda: _gen_tron_chuc(),
    lambda: _gen_do_dai_cm(),
    lambda: _gen_so_lon_nhat(),
    lambda: _gen_so_be_nhat(),
    lambda: _gen_loi_van_cong(),
    lambda: _gen_loi_van_tru(),
    lambda: _gen_dem_chuc_donvi(),
    lambda: _gen_xem_gio(),
]

def _gen_bao_meo_pool(n, seed=None):
    """Sinh n câu từ generators lớp 1 của Bảo Mèo."""
    if seed is not None:
        random.seed(seed)
    pool = []
    while len(pool) < n:
        g = random.choice(_BAO_MEO_GENERATORS)
        q = g()
        if q and q not in pool:
            pool.append(q)
    return pool

# === ĐỀ BẢO MÈO (lấy từ PDF Chân Trời Sáng Tạo) ===
BAO_MEO_DE_1 = [
    {
        "type": "choice",
        "q": "Trong các số: 35, 98, 74, 69 — số nào lớn nhất?",
        "options": ["35", "74", "98", "69"],
        "answer": "98",
        "topic": "So sánh",
    },
    {
        "type": "choice",
        "q": "Trong các số: 69, 74, 98, 35 — số nào bé nhất?",
        "options": ["69", "98", "74", "35"],
        "answer": "35",
        "topic": "So sánh",
    },
    {
        "type": "choice",
        "q": "Phép tính 20 + 29 có kết quả là:",
        "options": ["49", "12", "87", "48"],
        "answer": "49",
        "topic": "Cộng",
    },
    {
        "type": "choice",
        "q": "Phép tính 99 − 12 có kết quả là:",
        "options": ["49", "12", "87", "48"],
        "answer": "87",
        "topic": "Trừ",
    },
    {
        "type": "choice",
        "q": "Đẳng thức nào ĐÚNG?",
        "options": ["77 − 7 − 0 = 77", "90 + 5 < 94", "65 − 33 < 33", "63 = 36"],
        "answer": "65 − 33 < 33",
        "topic": "So sánh biểu thức",
    },
    {
        "type": "choice",
        "q": "Trong các số 25; 46; 60; 07; 90 — các số tròn chục là:",
        "options": ["25; 60", "46; 90", "60; 90", "07; 60"],
        "answer": "60; 90",
        "topic": "Số tròn chục",
    },
    {
        "type": "choice",
        "q": "Đồng hồ kim ngắn chỉ số 4, kim dài chỉ số 12 — đồng hồ chỉ mấy giờ?",
        "options": ["6 giờ", "7 giờ", "4 giờ", "12 giờ"],
        "answer": "4 giờ",
        "topic": "Xem giờ",
    },
    {"type": "fill", "q": "Tính nhẩm: 3 + 36 = ?", "answer": "39", "topic": "Cộng nhẩm"},
    {"type": "fill", "q": "Tính nhẩm: 45 − 20 = ?", "answer": "25", "topic": "Trừ nhẩm"},
    {
        "type": "fill",
        "q": "Lớp 1A trồng được 14 cây, lớp 1B trồng được 22 cây. Hỏi cả hai lớp trồng được bao nhiêu cây?",
        "answer": "36",
        "topic": "Toán lời văn",
    },
]

BAO_MEO_DE_2 = [
    {
        "type": "choice",
        "q": "Số gồm 5 đơn vị và 4 chục được viết là:",
        "options": ["54", "45", "50", "40"],
        "answer": "45",
        "topic": "Cấu tạo số",
    },
    {
        "type": "choice",
        "q": "Các số 79, 81, 18 viết theo thứ tự từ lớn đến bé là:",
        "options": ["79, 18, 81", "81, 79, 18", "18, 79, 81", "81, 18, 79"],
        "answer": "81, 79, 18",
        "topic": "Sắp xếp số",
    },
    {
        "type": "choice",
        "q": "Số gồm 4 chục và 8 đơn vị đọc là:",
        "options": ["tám tư", "bốn tám", "Bốn mươi tám", "Tám mươi tư"],
        "answer": "Bốn mươi tám",
        "topic": "Đọc số",
    },
    {
        "type": "choice",
        "q": "Trong các số 13, 63, 9, 24 — số lớn nhất là:",
        "options": ["13", "63", "9", "24"],
        "answer": "63",
        "topic": "So sánh",
    },
    {"type": "fill", "q": "Đặt tính rồi tính: 20 + 35 = ?", "answer": "55", "topic": "Cộng"},
    {"type": "fill", "q": "Đặt tính rồi tính: 73 − 21 = ?", "answer": "52", "topic": "Trừ"},
    {
        "type": "choice",
        "q": "Trong các số từ 25 đến 95 có bao nhiêu số tròn chục?",
        "options": ["6", "5", "7", "8"],
        "answer": "7",
        "topic": "Số tròn chục",
    },
    {
        "type": "choice",
        "q": "Số lớn hơn 17 và bé hơn 20 là:",
        "options": ["15 và 16", "15 và 18", "16 và 18", "18 và 19"],
        "answer": "18 và 19",
        "topic": "Khoảng số",
    },
    {"type": "fill", "q": "Tính: 32 + 5 − 13 = ?", "answer": "24", "topic": "Tính dãy"},
    {
        "type": "fill",
        "q": "Nga có 22 bút chì, Lan có 1 chục bút mực, Hoa có 15 bút sáp. Cả ba bạn có bao nhiêu cái bút?",
        "answer": "47",
        "topic": "Toán lời văn",
    },
]

BAO_MEO_VIOLYMPIC = [
    # ===== CỘNG TRỪ TRONG PHẠM VI 10 =====
    {"type": "fill", "q": "5 - 3 = ?", "answer": "2", "topic": "Cộng trừ"},
    {"type": "fill", "q": "4 - 3 = ?", "answer": "1", "topic": "Cộng trừ"},
    {"type": "fill", "q": "2 - 1 + 4 = ?", "answer": "5", "topic": "Cộng trừ"},
    {"type": "fill", "q": "3 + 1 = ?", "answer": "4", "topic": "Cộng trừ"},
    {"type": "fill", "q": "5 - 2 = ?", "answer": "3", "topic": "Cộng trừ"},
    {"type": "fill", "q": "3 + 5 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "2 + 6 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "7 + 1 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "6 - 4 = ?", "answer": "2", "topic": "Cộng trừ"},
    {"type": "fill", "q": "5 - 2 + 3 = ?", "answer": "6", "topic": "Cộng trừ"},
    {"type": "fill", "q": "4 + 4 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "5 + 3 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "9 - 4 = ?", "answer": "5", "topic": "Cộng trừ"},
    {"type": "fill", "q": "8 - 5 + 3 = ?", "answer": "6", "topic": "Cộng trừ"},
    {"type": "fill", "q": "9 - 3 - 2 = ?", "answer": "4", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 - 6 + 3 = ?", "answer": "7", "topic": "Cộng trừ"},
    {"type": "fill", "q": "1 + 4 + 5 = ?", "answer": "10", "topic": "Cộng trừ"},
    {"type": "fill", "q": "1 + 2 + 7 = ?", "answer": "10", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 - 5 = ?", "answer": "5", "topic": "Cộng trừ"},
    {"type": "fill", "q": "1 + 3 + 5 = ?", "answer": "9", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 - 5 - 3 = ?", "answer": "2", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 - 4 - 3 = ?", "answer": "3", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 - 7 + 2 = ?", "answer": "5", "topic": "Cộng trừ"},
    # ===== CỘNG TRỪ TRONG PHẠM VI 20 =====
    {"type": "choice", "q": "16 - 6 = ?", "options": ["11", "10", "12", "9"], "answer": "10", "topic": "Cộng trừ"},
    {"type": "choice", "q": "19 - 6 - 1 = ?", "options": ["13", "12", "11", "14"], "answer": "12", "topic": "Cộng trừ"},
    {"type": "choice", "q": "19 - 7 = ?", "options": ["12", "2", "13", "11"], "answer": "12", "topic": "Cộng trừ"},
    {"type": "choice", "q": "13 + 4 - 6 = ?", "options": ["15", "10", "11", "12"], "answer": "11", "topic": "Cộng trừ"},
    {"type": "fill", "q": "11 + 3 = ?", "answer": "14", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 + 7 = ?", "answer": "17", "topic": "Cộng trừ"},
    {"type": "fill", "q": "16 + 2 = ?", "answer": "18", "topic": "Cộng trừ"},
    {"type": "fill", "q": "11 + 6 = ?", "answer": "17", "topic": "Cộng trừ"},
    {"type": "fill", "q": "16 - 4 = ?", "answer": "12", "topic": "Cộng trừ"},
    {"type": "fill", "q": "18 - 2 = ?", "answer": "16", "topic": "Cộng trừ"},
    {"type": "fill", "q": "19 - 3 = ?", "answer": "16", "topic": "Cộng trừ"},
    {"type": "fill", "q": "17 - 3 = ?", "answer": "14", "topic": "Cộng trừ"},
    {"type": "choice", "q": "18 - 8 - 2 = ?", "options": ["10", "9", "8", "12"], "answer": "8", "topic": "Cộng trừ"},
    {"type": "choice", "q": "15 - 5 - 7 = ?", "options": ["13", "4", "3", "2"], "answer": "3", "topic": "Cộng trừ"},
    # ===== CỘNG TRỪ TRONG PHẠM VI 100 =====
    {"type": "fill", "q": "50 + 40 - 10 = ?", "answer": "80", "topic": "Cộng trừ"},
    {"type": "fill", "q": "70 - 40 + 30 = ?", "answer": "60", "topic": "Cộng trừ"},
    {"type": "choice", "q": "30 + 60 - ? = 40 + 20 - 10", "options": ["30", "40", "10", "20"], "answer": "40", "topic": "Cộng trừ"},
    {"type": "choice", "q": "50 - ? + 10 = 30", "options": ["10", "20", "30", "40"], "answer": "30", "topic": "Cộng trừ"},
    {"type": "choice", "q": "60 - 40 + ? = 30 + 40 - 20", "options": ["10", "30", "50", "80"], "answer": "30", "topic": "Cộng trừ"},
    {"type": "fill", "q": "60 + 30 - 40 = ?", "answer": "50", "topic": "Cộng trừ"},
    {"type": "choice", "q": "80 - 30 + 10 = ?", "options": ["60", "40", "50", "30"], "answer": "60", "topic": "Cộng trừ"},
    {"type": "choice", "q": "Tính: 12 + 7 - 4 = ?", "options": ["17", "15", "14", "16"], "answer": "15", "topic": "Cộng trừ"},
    {"type": "choice", "q": "Tính: 30 + 10 = ?", "options": ["40", "30", "60", "50"], "answer": "40", "topic": "Cộng trừ"},
    {"type": "choice", "q": "Số thích hợp điền vào chỗ chấm: 47 + 31 - 36 = ?", "options": ["72", "42", "62", "52"], "answer": "42", "topic": "Cộng trừ"},
    # ===== SO SÁNH SỐ =====
    {"type": "choice", "q": "Điền dấu thích hợp: 2 + 5 ___ (4 - 2 - 1)", "options": [">", "<", "=", "không xác định"], "answer": ">", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 2 + 2 ___ 5", "options": ["<", ">", "=", "không xác định"], "answer": "<", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 7 - 3 ___ (6 - 6)", "options": [">", "<", "=", "không xác định"], "answer": ">", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 8 - 2 - 1 ___ (3 + 4)", "options": ["<", ">", "=", "không xác định"], "answer": "<", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 3 + 4 ___ (5 + 2)", "options": ["<", ">", "=", "không xác định"], "answer": "=", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 12 ___ 14", "options": ["<", ">", "=", "không xác định"], "answer": "<", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 11 ___ 10", "options": [">", "<", "=", "không xác định"], "answer": ">", "topic": "So sánh"},
    {"type": "choice", "q": "Điền dấu thích hợp: 6 + 3 - 2 ___ (5 + 2)", "options": ["=", "<", ">", "không xác định"], "answer": "=", "topic": "So sánh"},
    # ===== SỐ HỌC =====
    {"type": "fill", "q": "Số liền sau số 45 là số nào?", "answer": "46", "topic": "Số học"},
    {"type": "fill", "q": "Số liền sau số 9 là số nào?", "answer": "10", "topic": "Số học"},
    {"type": "fill", "q": "Số liền trước số 8 là số nào?", "answer": "7", "topic": "Số học"},
    {"type": "fill", "q": "Số liền trước số 79 là số nào?", "answer": "78", "topic": "Số học"},
    {"type": "fill", "q": "Số 46 là số liền sau số nào?", "answer": "45", "topic": "Số học"},
    {"type": "fill", "q": "Số 12 gồm 1 chục và bao nhiêu đơn vị?", "answer": "2", "topic": "Số học"},
    {"type": "fill", "q": "Số mười một được viết là?", "answer": "11", "topic": "Số học"},
    {"type": "fill", "q": "Số mười hai được viết là?", "answer": "12", "topic": "Số học"},
    {"type": "fill", "q": "Số lớn nhất trong các số 1, 7, 12, 4, 9, 3, 2, 11 là số nào?", "answer": "12", "topic": "Số học"},
    {"type": "fill", "q": "Số tự nhiên lớn hơn 5 và nhỏ hơn 7 là số nào?", "answer": "6", "topic": "Số học"},
    {"type": "fill", "q": "Số tự nhiên nhỏ hơn 8 và lớn hơn 6 là số nào?", "answer": "7", "topic": "Số học"},
    {"type": "fill", "q": "Số lớn nhất trong các số 3, 9, 5, 11, 1, 7 là số nào?", "answer": "11", "topic": "Số học"},
    {"type": "fill", "q": "Có tất cả bao nhiêu số tự nhiên lớn hơn 7 và nhỏ hơn 12?", "answer": "4", "topic": "Số học"},
    {"type": "fill", "q": "Có bao nhiêu số tự nhiên từ 0 đến 9?", "answer": "10", "topic": "Số học"},
    {"type": "fill", "q": "Số lớn hơn 8 nhưng nhỏ hơn 10 là số nào?", "answer": "9", "topic": "Số học"},
    {"type": "fill", "q": "Số lớn nhất có 2 chữ số mà 2 chữ số của số đó cộng lại bằng 10 là số nào?", "answer": "91", "topic": "Số học"},
    {"type": "fill", "q": "Hãy cho biết có tất cả bao nhiêu số có 2 chữ số mà 2 chữ số của mỗi số đó giống nhau?", "answer": "9", "topic": "Số học"},
    {"type": "fill", "q": "Số lớn nhất có 2 chữ số mà 2 chữ số của số đó cộng lại bằng 9 là số nào?", "answer": "90", "topic": "Số học"},
    {"type": "fill", "q": "Số nhỏ nhất có 2 chữ số mà 2 chữ số của số đó trừ cho nhau bằng 0 là số nào?", "answer": "11", "topic": "Số học"},
    {"type": "fill", "q": "Có tất cả bao nhiêu số có 2 chữ số lớn hơn 65?", "answer": "34", "topic": "Số học"},
    {"type": "fill", "q": "Có tất cả bao nhiêu số có 2 chữ số mà các số đó đều có chữ số 7?", "answer": "18", "topic": "Số học"},
    {"type": "fill", "q": "Khi lấy một số trừ đi số liền trước của số đó thì được kết quả bằng bao nhiêu?", "answer": "1", "topic": "Số học"},
    {"type": "choice", "q": "Tất cả các số tự nhiên nhỏ hơn 5 là?", "options": ["0,1,2,3,4 và 5", "0,1,2,3 và 4", "2,3,4 và 5", "1,2,3 và 4"], "answer": "0,1,2,3 và 4", "topic": "Số học"},
    {"type": "choice", "q": "Có bao nhiêu số lớn hơn 12 và nhỏ hơn 19?", "options": ["12", "8", "6", "7"], "answer": "6", "topic": "Số học"},
    {"type": "choice", "q": "Tìm số lớn nhất có 2 chữ số mà 2 chữ số của số đó lớn hơn nhau 2 đơn vị?", "options": ["13", "64", "97", "75"], "answer": "97", "topic": "Số học"},
    {"type": "fill", "q": "Số tròn chục liền sau của số 30 cộng với 40 bằng bao nhiêu?", "answer": "80", "topic": "Số học"},
    {"type": "fill", "q": "Từ 30 đến 80 có bao nhiêu số tròn chục?", "answer": "6", "topic": "Số học"},
    {"type": "fill", "q": "Có tất cả bao nhiêu số có 2 chữ số nhỏ hơn 68?", "answer": "58", "topic": "Số học"},
    {"type": "fill", "q": "Có bao nhiêu số tự nhiên lớn hơn 12 và nhỏ hơn 18?", "answer": "5", "topic": "Số học"},
    {"type": "fill", "q": "Số liền trước của số lớn nhất có một chữ số cộng với số bé nhất có hai chữ số bằng bao nhiêu?", "answer": "18", "topic": "Số học"},
    {"type": "fill", "q": "Có tất cả bao nhiêu số lớn hơn 42 nhưng nhỏ hơn 76?", "answer": "33", "topic": "Số học"},
    {"type": "fill", "q": "Biết số A = 78 - 14. Vậy số liền sau số A là số bao nhiêu?", "answer": "65", "topic": "Số học"},
    # ===== TOÁN LỜI VĂN =====
    {"type": "fill", "q": "Năm nay bố 38 tuổi, con 12 tuổi. Hỏi bố hơn con bao nhiêu tuổi?", "answer": "26", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Năm nay mẹ 59 tuổi, mẹ hơn con 25 tuổi. Hỏi năm nay con bao nhiêu tuổi?", "answer": "34", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Trong lớp 1A, tổ một có 13 bạn. Nếu tổ một thêm 2 bạn nữa thì số bạn ở tổ một bằng số bạn ở tổ hai. Hỏi cả hai tổ có bao nhiêu bạn?", "answer": "28", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Linh có 17 quả bóng bay. Linh cho Hà và Ngọc mỗi bạn 3 quả. Vậy Linh còn lại bao nhiêu quả bóng bay?", "answer": "11", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Mẹ Lan mua 3 chục quả trứng gà và 2 chục quả trứng vịt. Vậy mẹ Lan mua tất cả bao nhiêu quả trứng?", "answer": "50", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Hoa có 19 con tem. Hoa cho bạn Mai 4 con tem, cho bạn Linh 3 con tem. Hỏi Hoa còn bao nhiêu con tem?", "answer": "12", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Quân có 30 cái bánh. Quân cho Hoàng 20 cái bánh. Mẹ cho Quân thêm 7 cái bánh. Vậy Quân còn lại bao nhiêu cái bánh?", "answer": "17", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Hiện nay tuổi của hai anh em cộng lại là 14 tuổi. Hỏi 2 năm nữa tuổi 2 anh em cộng lại là bao nhiêu?", "answer": "18", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Hùng vẽ được 10 hình tròn. Tâm vẽ được 4 hình tròn. Hỏi cả hai bạn vẽ được bao nhiêu hình tròn?", "answer": "14", "topic": "Toán lời văn"},
    {"type": "fill", "q": "An có 50 viên bi. An cho Tùng 40 viên. Hỏi An còn bao nhiêu viên bi?", "answer": "10", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Lớp 1A có 40 học sinh, lớp 1B có 30 học sinh, lớp 1C có 20 học sinh. Hỏi cả ba lớp có tất cả bao nhiêu học sinh?", "answer": "90", "topic": "Toán lời văn"},
    {"type": "fill", "q": "An có 65 con tem. An cho Hòa và Bình mỗi bạn 10 con tem. Hỏi An còn lại bao nhiêu con tem?", "answer": "45", "topic": "Toán lời văn"},
    {"type": "choice", "q": "Lớp 1A có 20 học sinh nam và 10 học sinh nữ. Lớp 1B có 10 học sinh nam và 20 học sinh nữ. Cả hai lớp có bao nhiêu học sinh?", "options": ["80", "70", "60", "50"], "answer": "60", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Linh mua 4 quả cà chua. Vy mua nhiều hơn Linh 1 quả. Hỏi cả hai bạn mua bao nhiêu quả cà chua?", "answer": "9", "topic": "Toán lời văn"},
    {"type": "choice", "q": "Nam có 19 viên bi. Nam cho Thành và Long mỗi bạn 4 viên bi. Lúc này Nam có bao nhiêu viên bi?", "options": ["11", "12", "14", "13"], "answer": "11", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Tuấn làm được 20 bài toán, Nhung làm được 10 bài toán, Hạnh làm được 10 bài toán. Hỏi cả ba bạn làm được bao nhiêu bài toán?", "answer": "40", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Mai có 50 cái kẹo. Sau khi Mai cho Hồng một số cái kẹo thì Mai còn 40 cái kẹo. Hỏi Mai cho Hồng bao nhiêu cái kẹo?", "answer": "10", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Lan có 19 quyển vở. Lan cho Hoa và Bình mỗi bạn 4 quyển vở. Vậy Lan còn lại bao nhiêu quyển vở?", "answer": "11", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Hiện nay con 5 tuổi, mẹ hơn con 30 tuổi, bố hơn mẹ 10 tuổi. Hỏi bố hơn con bao nhiêu tuổi?", "answer": "40", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Năm nay anh hơn em 12 tuổi. Hỏi 7 năm nữa anh hơn em bao nhiêu tuổi?", "answer": "12", "topic": "Toán lời văn"},
    {"type": "fill", "q": "Hòa nghĩ ra một số mà khi lấy số đó trừ đi 14 thì cũng được kết quả bằng với kết quả khi lấy 20 cộng với 11. Hỏi Hòa nghĩ ra số nào?", "answer": "45", "topic": "Toán lời văn"},
    # ===== ĐO LƯỜNG =====
    {"type": "choice", "q": "Tính: 30cm - 20cm + 8cm = ?", "options": ["10cm", "18cm", "18", "10"], "answer": "18cm", "topic": "Đo lường"},
    {"type": "choice", "q": "Tính: 30cm - 20cm + 6cm = ?", "options": ["10", "16cm", "18cm", "10cm"], "answer": "16cm", "topic": "Đo lường"},
    {"type": "choice", "q": "Tính: 12cm + 5cm = 19cm - ?", "options": ["5cm", "12cm", "2cm", "2"], "answer": "2cm", "topic": "Đo lường"},
    {"type": "fill", "q": "80cm - 60cm + 60cm = 50cm + ? cm", "answer": "30", "topic": "Đo lường"},
    {"type": "fill", "q": "70cm - 50cm + 20cm = 30cm + ? cm", "answer": "10", "topic": "Đo lường"},
    {"type": "fill", "q": "Đoạn thẳng thứ nhất và thứ hai mỗi đoạn dài 10cm, đoạn thứ ba dài 20cm. Hỏi cả ba đoạn thẳng đó dài bao nhiêu xăng-ti-mét?", "answer": "40", "topic": "Đo lường"},
    {"type": "choice", "q": "Một mảnh vải dài 84m. Lan cắt bỏ đi 23m. Hỏi mảnh vải còn lại dài bao nhiêu mét?", "options": ["41", "61", "51", "71"], "answer": "61", "topic": "Đo lường"},
    # ===== ĐIỀN SỐ VÀO PHÉP TÍNH =====
    {"type": "choice", "q": "6 - ? = 2", "options": ["5", "4", "8", "3"], "answer": "4", "topic": "Cộng trừ"},
    {"type": "choice", "q": "3 + 4 + 2 = ?", "options": ["7", "8", "6", "9"], "answer": "9", "topic": "Cộng trừ"},
    {"type": "choice", "q": "6 - 5 = ?", "options": ["3", "2", "4", "1"], "answer": "1", "topic": "Cộng trừ"},
    {"type": "choice", "q": "6 + 1 = 8 - ?", "options": ["3", "2", "1", "7"], "answer": "1", "topic": "Cộng trừ"},
    {"type": "choice", "q": "9 - 6 + ? = 5", "options": ["4", "2", "3", "1"], "answer": "2", "topic": "Cộng trừ"},
    {"type": "choice", "q": "4 + 4 - ? = 2", "options": ["5", "6", "4", "3"], "answer": "6", "topic": "Cộng trừ"},
    {"type": "choice", "q": "5 + ? = 7 - 3 + 2", "options": ["1", "4", "3", "2"], "answer": "1", "topic": "Cộng trừ"},
    {"type": "choice", "q": "3 + 1 + 2 + 4 = 1 + ?", "options": ["7", "9", "8", "5"], "answer": "9", "topic": "Cộng trừ"},
    {"type": "fill", "q": "6 = 10 - ?", "answer": "4", "topic": "Cộng trừ"},
    {"type": "fill", "q": "5 - ? = 7 - 6 + 3", "answer": "1", "topic": "Cộng trừ"},
    {"type": "fill", "q": "9 - 6 + ? = 7", "answer": "4", "topic": "Cộng trừ"},
    {"type": "fill", "q": "10 = 5 + ? + 3", "answer": "2", "topic": "Cộng trừ"},
    {"type": "fill", "q": "3 + 6 = 4 + ?", "answer": "5", "topic": "Cộng trừ"},
    {"type": "fill", "q": "7 + 2 - ? = 6", "answer": "3", "topic": "Cộng trừ"},
    {"type": "fill", "q": "4 + 6 - 2 = ?", "answer": "8", "topic": "Cộng trừ"},
    {"type": "fill", "q": "Số nào cộng với 30 thì bằng 70?", "answer": "40", "topic": "Cộng trừ"},
    {"type": "fill", "q": "Số nào cộng với 20 rồi cộng với 30 thì bằng 90?", "answer": "40", "topic": "Cộng trừ"},
    # ===== DÃY SỐ =====
    {"type": "fill", "q": "Các số 3, 6, 7, 1, 9, 2 được viết theo thứ tự từ lớn đến bé là: 9, ?, 6, 3, 2, 1", "answer": "7", "topic": "Dãy số"},
]

BAO_MEO_POOL = BAO_MEO_DE_1 + BAO_MEO_DE_2  # đề thi HK
# Toàn bộ pool bao gồm đề thi + Violympic
BAO_MEO_FULL_POOL = BAO_MEO_POOL + BAO_MEO_VIOLYMPIC
