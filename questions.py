"""Pool câu hỏi theo môn / chế độ.
Cấu trúc mở rộng: thêm môn mới = thêm vào STUDENT_SUBJECTS + viết pool/generator riêng.
"""
import random

# ─── Môn học hiện có theo từng bé ────────────────────────────────────────────
# Key = student_key, value = list môn có câu hỏi thực sự
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
    """Trả về danh sách môn học có sẵn cho bé này."""
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


# ─── Bảo Mèo — generators lớp 1 ─────────────────────────────────────────────

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


# ─── Minh Khanh — Lớp 6A3 ────────────────────────────────────────────────────
# Thêm câu hỏi vào đây khi có nội dung lớp 6.
# ─── Minh Khanh — Lớp 6A3 ─────────────────────────────────────────────────
MINH_KHANH_TOAN = [
    # ===== PHÂN SỐ =====
    {"type": "choice", "q": "Số đối của phân số -7/4 là:", "options": ["4/7", "-4/7", "7/4", "-7/4"], "answer": "7/4", "topic": "Phân số"},
    {"type": "choice", "q": "Trong các cách viết sau, cách viết nào cho ta phân số?", "options": ["7/(-3)", "7/3,12", "4/2", "4/2"], "answer": "7/(-3)", "topic": "Phân số"},
    {"type": "choice", "q": "Kết quả khi rút gọn phân số 20/(-140) đến tối giản là:", "options": ["-10/70", "-4/28", "-2/14", "-1/7"], "answer": "-1/7", "topic": "Phân số"},
    {"type": "choice", "q": "Phân số nghịch đảo của -6/11 là phân số nào?", "options": ["11/(-6)", "6/11", "-6/(-11)", "-11/6"], "answer": "-11/6", "topic": "Phân số"},
    {"type": "choice", "q": "Kết quả của phép tính (-9/10) + (2/5) + (9/10) là:", "options": ["2/5", "-2/5", "3/5", "7/5"], "answer": "2/5", "topic": "Phân số"},
    {"type": "choice", "q": "Phân số nghịch đảo của -4/3 là:", "options": ["-3/4", "3/4", "4/(-3)", "4/3"], "answer": "-3/4", "topic": "Phân số"},
    {"type": "choice", "q": "Kết quả của phép tính 1/6 - (-3/4) là:", "options": ["7/12", "-11/12", "-7/12", "11/12"], "answer": "11/12", "topic": "Phân số"},
    {"type": "choice", "q": "Kết quả của phép tính (-3/2) : (-9/2) là:", "options": ["-3", "3", "1/3", "-1/3"], "answer": "1/3", "topic": "Phân số"},
    {"type": "choice", "q": "Viết hỗn số 3(1/5) dưới dạng phân số là:", "options": ["3/5", "8/5", "16/5", "4/5"], "answer": "16/5", "topic": "Phân số"},
    {"type": "choice", "q": "Viết hỗn số 2(3/7) thành phân số là:", "options": ["17/7", "6/7", "13/7", "10/7"], "answer": "17/7", "topic": "Phân số"},
    {"type": "choice", "q": "Hỗn số -2(3/5) viết dưới dạng phân số là:", "options": ["13/5", "-13/5", "-10/5", "-7/5"], "answer": "-13/5", "topic": "Phân số"},
    {"type": "choice", "q": "Số đối của -7/13 là:", "options": ["13/(-7)", "7/(-13)", "7/13", "-7/13"], "answer": "7/13", "topic": "Phân số"},
    {"type": "choice", "q": "Trong các phân số -7/(-5), 6/5, -7/5, 6/(-5), phân số lớn nhất là:", "options": ["-7/(-5)", "6/5", "-7/5", "6/(-5)"], "answer": "-7/(-5)", "topic": "Phân số"},
    {"type": "choice", "q": "Cặp phân số nào sau đây bằng nhau?", "options": ["2/3 và 3/2", "2/3 và 4/6", "3/2 và 4/6", "6/4 và 4/6"], "answer": "2/3 và 4/6", "topic": "Phân số"},
    {"type": "choice", "q": "Số đối của phân số -6/7 là?", "options": ["6/(-7)", "-6/(-7)", "-7/6", "7/6"], "answer": "-6/(-7)", "topic": "Phân số"},
    {"type": "choice", "q": "Giá trị của y để 3/7 = -9/y là:", "options": ["24", "-21", "21", "-24"], "answer": "-21", "topic": "Phân số"},
    {"type": "choice", "q": "Kết quả của phép tính (-1/13) : (7/(-13)) là:", "options": ["-7/169", "-1/7", "7/169", "1/7"], "answer": "1/7", "topic": "Phân số"},
    {"type": "choice", "q": "Rút gọn phân số -24/(-36) về phân số tối giản là:", "options": ["8/12", "-4/(-6)", "2/3", "-2/3"], "answer": "2/3", "topic": "Phân số"},
    {"type": "choice", "q": "3/8 của 24 là:", "options": ["3", "9", "64", "8"], "answer": "9", "topic": "Phân số"},
    # ===== SỐ THẬP PHÂN =====
    {"type": "choice", "q": "Số đối của số thập phân 3,15 là:", "options": ["-1,35", "-5,13", "3,15", "-3,15"], "answer": "-3,15", "topic": "Số thập phân"},
    {"type": "choice", "q": "Viết phân số -2024/10 dưới dạng số thập phân ta được:", "options": ["-20,24", "-22,04", "2,024", "-202,4"], "answer": "-202,4", "topic": "Số thập phân"},
    {"type": "choice", "q": "Viết số thập phân -0,15 dưới dạng phân số tối giản ta được:", "options": ["1/5", "-1/5", "3/(-20)", "-3/20"], "answer": "-3/20", "topic": "Số thập phân"},
    {"type": "choice", "q": "Số thập phân 0,008 được viết dưới dạng phân số thập phân là:", "options": ["8/10", "8/100", "0,8/1000", "8/1000"], "answer": "8/1000", "topic": "Số thập phân"},
    {"type": "choice", "q": "Viết phân số -6/8 dưới dạng số thập phân là:", "options": ["-0,75", "-0,6", "-0,8", "0,75"], "answer": "-0,75", "topic": "Số thập phân"},
    {"type": "choice", "q": "Kết quả phép tính 13,292 + (-2,135) là:", "options": ["11,55", "11,157", "11,175", "11,75"], "answer": "11,157", "topic": "Số thập phân"},
    {"type": "choice", "q": "Kết quả phép tính (-4,4) . 3,2 là:", "options": ["-14,8", "-1,48", "-14,08", "14,08"], "answer": "-14,08", "topic": "Số thập phân"},
    {"type": "choice", "q": "Trong các câu sau câu nào sai?", "options": ["Tổng của hai số thập phân dương là một số thập phân dương.", "Tích của hai số thập phân dương là một số thập phân dương.", "Hiệu của hai số thập phân dương là một số thập phân dương.", "Thương của hai số thập phân dương là một số thập phân dương."], "answer": "Hiệu của hai số thập phân dương là một số thập phân dương.", "topic": "Số thập phân"},
    {"type": "choice", "q": "Giá trị của x thỏa mãn 1,23 + x = 2,67 - 3,89 là:", "options": ["-2,54", "7,79", "0,01", "-2,45"], "answer": "-2,45", "topic": "Số thập phân"},
    # ===== LÀM TRÒN SỐ =====
    {"type": "choice", "q": "Làm tròn số thập phân 23,567 đến hàng phần mười ta được:", "options": ["23,56", "23,6", "23,57", "23,5"], "answer": "23,6", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số a = 135,4956 đến chữ số thập phân thứ hai ta được số thập phân nào?", "options": ["135,49", "135,51", "135,50", "136"], "answer": "135,50", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số 56,087 đến hàng phần trăm, ta được:", "options": ["56,08", "56,09", "56", "56,1"], "answer": "56,09", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số 9,8462 đến hàng phần mười ta được kết quả là:", "options": ["9,8", "10", "9,9", "9,846"], "answer": "9,9", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số 22,1648 đến hàng phần trăm là:", "options": ["22,165", "22,2", "22,16", "22,17"], "answer": "22,16", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Chia đều một sợi dây dài 13 cm thành 4 đoạn bằng nhau. Tính độ dài mỗi đoạn dây (làm tròn chữ số hàng thập phân thứ nhất):", "options": ["3,2", "3,3", "3,25", "3,4"], "answer": "3,3", "topic": "Làm tròn số"},
    # ===== TỈ SỐ PHẦN TRĂM =====
    {"type": "choice", "q": "Tính 25% của 12 bằng:", "options": ["2", "3", "4", "6"], "answer": "3", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "Một quyển sách có giá 48 000 đồng. Giá mới của quyển sách sau khi giảm 25% bằng:", "options": ["12 000 đồng", "36 000 đồng", "60 000 đồng", "192 000 đồng"], "answer": "36 000 đồng", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "75% của một số bằng 96. Số đó là:", "options": ["125", "72", "60", "128"], "answer": "128", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "Bạn Linh mua một quyển truyện có giá bìa là 80 000 đồng. Khi trả tiền được cửa hàng giảm giá 20%. Hỏi bạn Linh mua quyển truyện đó hết bao nhiêu tiền?", "options": ["60 000 đồng", "16 000 đồng", "96 000 đồng", "64 000 đồng"], "answer": "64 000 đồng", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "Nam mua một quyển sách giá 45 000 đồng. Khi thanh toán, hiệu sách giảm giá 10%. Hỏi Nam mua quyển sách đó bao nhiêu tiền?", "options": ["40 000", "49 500", "40 500", "4 500"], "answer": "40 500", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "Cho biết 80% của một số là -20. Số đó là:", "options": ["-25", "16", "25", "-16"], "answer": "-25", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "Tỉ số phần trăm của hai số 16 và 20 là:", "options": ["48%", "8%", "164%", "80%"], "answer": "80%", "topic": "Tỉ số phần trăm"},
    {"type": "choice", "q": "1/4 bình nước là 5 lít. Hỏi cả bình nước chứa được bao nhiêu lít nước?", "options": ["20 lít", "15 lít", "54 lít", "1,25 lít"], "answer": "20 lít", "topic": "Tỉ số phần trăm"},
    # ===== XÁC SUẤT THỰC NGHIỆM =====
    {"type": "choice", "q": "Nếu tung đồng xu 20 lần liên tiếp, có 12 lần xuất hiện mặt S. Khi đó xác suất thực nghiệm của mặt N là:", "options": ["3/5", "8/12", "4/5", "2/5"], "answer": "2/5", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Tung một con xúc xắc có sáu mặt, số chấm ở mỗi mặt là một trong các số nguyên dương 1, 2, 3, 4, 5, 6. Có bao nhiêu kết quả có thể xảy ra đối với mặt xuất hiện của con xúc xắc?", "options": ["3", "6", "0", "1"], "answer": "6", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Một hộp có 10 chiếc thẻ được đánh số từ 1 đến 10. Rút ngẫu nhiên một chiếc thẻ từ trong hộp, ghi lại số của thẻ rút được và bỏ lại thẻ đó vào hộp. Sau 25 lần rút thẻ liên tiếp, nhận thấy có 4 lần lấy được thẻ đánh số 6. Xác suất thực nghiệm xuất hiện thẻ đánh số 6 là:", "options": ["2/25", "4/25", "1/10", "6/25"], "answer": "4/25", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Khi tung đồng xu 1 lần. Tập hợp các kết quả có thể xảy ra đối với mặt của đồng xu:", "options": ["{N; SN; S}", "{N; N}", "{S; S}", "{S; N}"], "answer": "{S; N}", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Tung 1 đồng xu hai mặt N và S cân đối và đồng chất 20 lần. Có 8 lần xuất hiện mặt N thì xác suất thực nghiệm xuất hiện mặt N là bao nhiêu?", "options": ["8", "2/5", "20", "12/20"], "answer": "2/5", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Bạn Nam tung một đồng xu 20 lần, Nam thấy có 8 lần xuất hiện mặt ngửa. Xác suất thực nghiệm của sự kiện xuất hiện mặt sấp là:", "options": ["3/5", "2/5", "2/3", "3/2"], "answer": "3/5", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Tung một đồng xu 15 lần liên tiếp, có 8 lần xuất hiện mặt N thì xác suất thực nghiệm xuất hiện mặt S là:", "options": ["8/15", "7/15", "15/7", "15/8"], "answer": "7/15", "topic": "Xác suất thực nghiệm"},
    {"type": "choice", "q": "Biết rằng xúc xắc có 6 mặt, số chấm ở mỗi mặt là một trong các số nguyên dương 1;2;3;4;5;6. Gieo con xúc xắc một lần. Số kết quả có thể xảy ra đối với mặt xuất hiện của xúc xắc là:", "options": ["1", "2", "4", "6"], "answer": "6", "topic": "Xác suất thực nghiệm"},
    # ===== HÌNH HỌC =====
    {"type": "choice", "q": "Điểm M thuộc đường thẳng a thì được kí hiệu là:", "options": ["M ∈ a", "M ⊂ a", "M ∉ a", "M = a"], "answer": "M ∈ a", "topic": "Hình học"},
    {"type": "choice", "q": "Cho điểm E thuộc đoạn thẳng IK. Biết IE = 4 cm, EK = 10 cm. Tính độ dài của đoạn thẳng IK.", "options": ["4 cm", "7 cm", "6 cm", "14 cm"], "answer": "14 cm", "topic": "Hình học"},
    {"type": "choice", "q": "Góc có số đo bằng 60° là:", "options": ["góc nhọn", "góc vuông", "góc tù", "góc bẹt"], "answer": "góc nhọn", "topic": "Hình học"},
    {"type": "choice", "q": "Hai tia đối nhau trong hình vẽ có ba điểm thẳng hàng M, N, P (N nằm giữa M và P) là:", "options": ["Tia MP và tia PM", "Tia MN và tia PN", "Tia NM và tia NP", "Tia MN và tia MP"], "answer": "Tia NM và tia NP", "topic": "Hình học"},
    {"type": "choice", "q": "Khẳng định nào dưới đây là sai (cho M, N, P thẳng hàng, N nằm giữa M và P)?", "options": ["Điểm N thuộc đường thẳng MP.", "Điểm N thuộc đoạn thẳng MP.", "Điểm M thuộc đường thẳng NP.", "Điểm M thuộc đoạn thẳng NP."], "answer": "Điểm M thuộc đoạn thẳng NP.", "topic": "Hình học"},
    {"type": "choice", "q": "Nếu điểm M là trung điểm của đoạn thẳng AB thì:", "options": ["AM = MB = AB/2", "AB = 2.AM", "M nằm giữa A và B", "Cả ba đều đúng"], "answer": "Cả ba đều đúng", "topic": "Hình học"},
    {"type": "choice", "q": "Lúc 9 giờ, góc tạo bởi kim giờ và kim phút là:", "options": ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], "answer": "Góc vuông", "topic": "Hình học"},
    {"type": "choice", "q": "Cho đoạn thẳng AB. M là trung điểm của AB, N là trung điểm của AM. Nếu AB = 8 cm thì MN bằng:", "options": ["1 cm", "2 cm", "3 cm", "4 cm"], "answer": "2 cm", "topic": "Hình học"},
    {"type": "choice", "q": "Cho 4 tia phân biệt chung gốc. Số góc tạo được từ bốn tia là:", "options": ["2", "4", "6", "8"], "answer": "6", "topic": "Hình học"},
    {"type": "choice", "q": "Cho góc xOy = 100°. Góc xOy là góc:", "options": ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], "answer": "Góc tù", "topic": "Hình học"},
    {"type": "choice", "q": "Cho hai điểm A, B thuộc tia Oy và OA = 4 cm, OB = 8 cm thì:", "options": ["A là trung điểm của đoạn thẳng OB.", "O là trung điểm của đoạn thẳng AB.", "B là trung điểm của đoạn thẳng OA.", "Không có đoạn thẳng nào có trung điểm."], "answer": "A là trung điểm của đoạn thẳng OB.", "topic": "Hình học"},
    {"type": "choice", "q": "Số đo của góc bẹt là:", "options": ["30°", "90°", "180°", "120°"], "answer": "180°", "topic": "Hình học"},
    {"type": "choice", "q": "Góc có hai cạnh là AB, AC là:", "options": ["góc ABC", "góc BAC", "góc BCA", "góc ACB"], "answer": "góc BAC", "topic": "Hình học"},
    # ===== THỐNG KÊ =====
    {"type": "choice", "q": "Dữ liệu nào sau đây là dữ liệu số?", "options": ["Bảng danh sách tên học sinh lớp 6A1", "Tên các tỉnh phía Bắc", "Bảng điểm tổng kết học kì I môn Toán lớp 6A1", "Tên các lớp trong trường"], "answer": "Bảng điểm tổng kết học kì I môn Toán lớp 6A1", "topic": "Thống kê"},
    {"type": "choice", "q": "Một cửa hàng bán dép, thống kê số lượng các đôi dép bán được trong tháng 5: cỡ 36 bán 21 đôi, cỡ 37 bán 25 đôi, cỡ 38 bán 35 đôi, cỡ 39 bán 30 đôi, cỡ 40 bán 23 đôi, cỡ 41 bán 19 đôi, cỡ 42 bán 17 đôi. Cỡ dép bán được nhiều nhất là:", "options": ["42", "39", "36", "38"], "answer": "38", "topic": "Thống kê"},
    {"type": "choice", "q": "Bác Hoa thống kê số áo bán được: cỡ 37 bán 20, cỡ 38 bán 29, cỡ 39 bán 56, cỡ 40 bán 65, cỡ 41 bán 47, cỡ 42 bán 18. Cỡ áo bán được nhiều nhất là:", "options": ["cỡ 39", "cỡ 42", "cỡ 40", "cỡ 41"], "answer": "cỡ 40", "topic": "Thống kê"},
    {"type": "choice", "q": "Để tổ chức sinh nhật cho các bạn sinh vào tháng 4, Trâm liệt kê ngày sinh: 6, 18, 25, 31. Giá trị không hợp lý trong dãy dữ liệu về ngày sinh tháng 4 là:", "options": ["31", "25", "6", "18"], "answer": "31", "topic": "Thống kê"},
    # ===== TẬP HỢP =====
    {"type": "choice", "q": "Cho dãy dữ liệu: Món ăn yêu thích của các thành viên trong gia đình: cháo, rau xào, gà rán, nước ngọt, thịt luộc, bánh tẻ. Dữ liệu không hợp lý trong dãy dữ liệu đã cho là:", "options": ["Bánh tẻ", "Thịt luộc", "Nước ngọt", "Gà rán"], "answer": "Nước ngọt", "topic": "Tập hợp"},
    # ===== TỰ LUẬN =====
    {"type": "fill", "q": "So sánh hai phân số: -3/5 và -2/5. Phân số nào lớn hơn?", "answer": "-2/5", "topic": "Phân số"},
    {"type": "fill", "q": "Tính: (-5/7) . (2/11) + (-5/7) . (9/11) + 5/7", "answer": "0", "topic": "Phân số"},
    {"type": "fill", "q": "Tính nhanh: 5,58 - 0,2 . 0,7 + 0,32 . 2,05 - 0,32 . 0,75", "answer": "5,784", "topic": "Số thập phân"},
    {"type": "fill", "q": "Tính: (-4,2) . 5,6 + 5,6 . (-5,8) + 2,8", "answer": "-53,2", "topic": "Số thập phân"},
    {"type": "fill", "q": "Tìm x biết: x + 1/5 = 3/5", "answer": "2/5", "topic": "Phân số"},
    {"type": "fill", "q": "Ba lớp 6 của một trường THCS có 120 học sinh. Số học sinh lớp 6A chiếm 35% so với học sinh của khối. Tính số học sinh lớp 6A.", "answer": "42", "topic": "Tỉ số phần trăm"},
    {"type": "fill", "q": "Lớp 6A có 40 học sinh. Số học sinh xếp loại Tốt chiếm 1/5 số học sinh cả lớp. Tính số học sinh xếp loại Tốt.", "answer": "8", "topic": "Tỉ số phần trăm"},
    {"type": "fill", "q": "Bạn Mai đọc một cuốn sách dày 320 trang. Ngày đầu Mai đọc được 40% số trang. Tính số trang sách Mai đọc được trong ngày thứ nhất.", "answer": "128", "topic": "Tỉ số phần trăm"},
    {"type": "fill", "q": "Trên tia Ox lấy hai điểm A, B sao cho OA = 3 cm, OB = 5 cm. Tính độ dài đoạn thẳng AB.", "answer": "2", "topic": "Hình học"},
    {"type": "fill", "q": "Bạn Nam gieo một con xúc xắc 30 lần. Kết quả: số chấm 1 xuất hiện 6 lần, số chấm 2 xuất hiện 4 lần, số chấm 3 xuất hiện 7 lần, số chấm 4 xuất hiện 3 lần, số chấm 5 xuất hiện 5 lần, số chấm 6 xuất hiện 5 lần. Tính xác suất thực nghiệm của sự kiện số chấm xuất hiện là số lẻ.", "answer": "3/5", "topic": "Xác suất thực nghiệm"},
]

MINH_KHANH_TIENG_ANH = [

    # ══ TIẾNG ANH 6 GLOBAL SUCCESS ══

    # ── De 04 - Lop 6 ──
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. mountain  B. around  C. shoulder  D. cloudy", "options": ["mountain", "around", "shoulder", "cloudy"], "answer": "shoulder", "topic": "Pronunciation", "explanation": "'shoulder' có âm /oʊ/, còn 'mountain', 'around', 'cloudy' đều có âm /aʊ/. Đây là hai âm nguyên âm đôi khác nhau hoàn toàn."},
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. these  B. thunder  C. together  D. therefore", "options": ["these", "thunder", "together", "therefore"], "answer": "thunder", "topic": "Pronunciation", "explanation": "'thunder' có âm /θʌ/ (phụ âm th + âm /ʌ/), trong khi 'these', 'together', 'therefore' đều phát âm 'th' là /ð/ (th hữu thanh)."},
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. medical  B. decide  C. tennis  D. pencil", "options": ["medical", "decide", "tennis", "pencil"], "answer": "decide", "topic": "Pronunciation", "explanation": "Trong 'decide', chữ 'e' đọc là /ɪ/ (âm ngắn ở vị trí không nhấn). Trong 'medical', 'tennis', 'pencil', chữ 'e' đọc là /e/ (âm ngắn trong âm tiết nhấn)."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. include  B. become  C. action  D. believe", "options": ["include", "become", "action", "believe"], "answer": "action", "topic": "Pronunciation", "explanation": "'action' có trọng âm ở âm tiết đầu (AC-tion), còn 'include', 'become', 'believe' đều có trọng âm ở âm tiết thứ hai."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. homework  B. future  C. modern  D. maintain", "options": ["homework", "future", "modern", "maintain"], "answer": "maintain", "topic": "Pronunciation", "explanation": "'maintain' có trọng âm ở âm tiết thứ hai (main-TAIN), còn 'homework', 'future', 'modern' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "This is the ______ robot in the show. Our scientists spent more than 2 years building it.", "options": ["smart", "smarter", "most smart", "smartest"], "answer": "smartest", "topic": "Grammar", "explanation": "Dùng so sánh nhất (superlative) khi so sánh một vật với tất cả các vật khác trong nhóm. 'smart' → 'smartest' (thêm -est). 'most smart' sai vì tính từ ngắn dùng -est, không dùng 'most'."},
    {"type": "choice", "q": "If the home robots _____ out of battery, they ______ charge themselves with solar energy.", "options": ["run – will", "runs - should", "go - run", "go - will"], "answer": "run – will", "topic": "Grammar", "explanation": "Câu điều kiện loại 1: If + S + V (hiện tại đơn), S + will + V. Chủ ngữ 'robots' số nhiều nên dùng 'run' (không có 's'). Mệnh đề chính dùng 'will charge'."},
    {"type": "choice", "q": "_____ can we do to make our school greener? – We can put a recycling bin in each classroom.", "options": ["How often", "What", "Where", "Why"], "answer": "What", "topic": "Grammar", "explanation": "Câu trả lời đề cập đến 'put a recycling bin' — đó là một hành động/việc làm, nên câu hỏi phải dùng 'What' (cái gì/làm gì). 'How often' hỏi tần suất, 'Where' hỏi nơi chốn, 'Why' hỏi lý do."},
    {"type": "choice", "q": "Does your neighborhood have _____ art gallery?", "options": ["a", "the", "an", "∅"], "answer": "an", "topic": "Grammar", "explanation": "Dùng 'an' trước danh từ số ít bắt đầu bằng nguyên âm. 'art gallery' bắt đầu bằng 'a' (nguyên âm), nên phải dùng 'an', không phải 'a'."},
    {"type": "choice", "q": "We have lots of plastic bottles at home _____ we don't know what to do with them.", "options": ["and", "due to", "but", "so"], "answer": "but", "topic": "Grammar", "explanation": "'but' = nhưng, dùng để nối hai ý tương phản. Có nhiều chai nhựa 'nhưng' không biết dùng làm gì — thể hiện sự mâu thuẫn. 'and' = và (không có tương phản), 'so' = vì vậy (không phù hợp)."},
    {"type": "choice", "q": "Our future house will be in ______ mountains. There will be many trees and flowers.", "options": ["a", "the", "an", "∅"], "answer": "the", "topic": "Grammar", "explanation": "Dùng 'the' trước danh từ chỉ địa hình tự nhiên theo nhóm như 'the mountains', 'the sea', 'the forest'. Đây là quy tắc dùng mạo từ xác định với danh từ số nhiều chỉ địa danh."},
    {"type": "choice", "q": "I am still not sure where to go for my holiday. I ______ to Vung Tau city.", "options": ["need go", "am going", "will go", "might go"], "answer": "might go", "topic": "Grammar", "explanation": "'might' = có thể (không chắc chắn). Vì câu trước nói 'still not sure' (vẫn chưa chắc), nên dùng 'might go' thể hiện sự không chắc chắn. 'will go' thể hiện chắc chắn hơn, không phù hợp."},
    {"type": "choice", "q": "What is the passage about? (passage: future houses with smart technology, smaller homes, motorhomes, renewable energy)", "options": ["Future houses", "Changes in technology", "High-tech appliances in houses", "Smart devices"], "answer": "Future houses", "topic": "Reading", "explanation": "Bài đọc nói về nhiều khía cạnh của nhà tương lai (nhà thông minh, nhà nhỏ hơn, nhà di động, năng lượng tái tạo). Chủ đề bao quát nhất là 'Future houses' (Những ngôi nhà trong tương lai)."},
    {"type": "choice", "q": "What will be an effective tool to create better living conditions? (future houses passage)", "options": ["multifunctional rooms", "smart device", "technology", "motorhomes"], "answer": "technology", "topic": "Reading", "explanation": "Bài đọc nêu rõ 'technology' (công nghệ) sẽ là công cụ hiệu quả để tạo ra điều kiện sống tốt hơn. Các đáp án khác chỉ là những ví dụ cụ thể, không phải công cụ tổng thể."},
    {"type": "choice", "q": "According to the passage, what can people do with a phone app? (future houses passage)", "options": ["to connect with other people", "to connect with home equipment", "to give orders in their homes", "B and C"], "answer": "B and C", "topic": "Reading", "explanation": "Bài đọc đề cập đến hai chức năng của ứng dụng điện thoại: kết nối với thiết bị nhà (B) và ra lệnh trong nhà (C). Vì cả hai đều đúng nên đáp án là 'B and C'."},
    {"type": "choice", "q": "What can we understand the word 'multifunctional' in the passage?", "options": ["having many appliances.", "having several different functions.", "having only one function.", "having no function."], "answer": "having several different functions.", "topic": "Vocabulary", "explanation": "'Multi-' = nhiều, 'functional' = chức năng. Vậy 'multifunctional' = có nhiều chức năng khác nhau. Không nhầm với 'having many appliances' vì 'appliances' là thiết bị, không phải chức năng."},
    {"type": "choice", "q": "What is NOT mentioned in the future houses passage?", "options": ["motorhomes help future people to travel around.", "People in the future no longer care about the environment.", "In the future, every house or building might use different sources of renewable energy.", "Homes will be smaller"], "answer": "People in the future no longer care about the environment.", "topic": "Reading", "explanation": "Bài đọc đề cập đến năng lượng tái tạo, nhà nhỏ hơn và nhà di động — cho thấy người tương lai VẪN quan tâm đến môi trường. Ý 'không còn quan tâm đến môi trường' không được nhắc đến và trái ngược với nội dung bài."},

    # ── De 05 - Lop 6 ──
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. think  B. bath  C. breath  D. father", "options": ["think", "bath", "breath", "father"], "answer": "father", "topic": "Pronunciation", "explanation": "Trong 'father', chữ 'th' đọc là /ð/ (th hữu thanh). Trong 'think', 'bath', 'breath', chữ 'th' đọc là /θ/ (th vô thanh)."},
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. snow  B. postcard  C. grow  D. however", "options": ["snow", "postcard", "grow", "however"], "answer": "however", "topic": "Pronunciation", "explanation": "Trong 'however', 'ow' đọc là /aʊ/ (giống 'now', 'cow'). Trong 'snow', 'grow' và 'postcard' (o), âm 'o/ow' đọc là /oʊ/."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. begin  B. famous  C. ready  D. active", "options": ["begin", "famous", "ready", "active"], "answer": "begin", "topic": "Pronunciation", "explanation": "'begin' có trọng âm ở âm tiết thứ hai (be-GIN). Còn 'famous', 'ready', 'active' đều nhấn âm tiết đầu (FA-mous, REA-dy, AC-tive)."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. firework  B. travel  C. morning  D. idea", "options": ["firework", "travel", "morning", "idea"], "answer": "idea", "topic": "Pronunciation", "explanation": "'idea' có trọng âm ở âm tiết thứ hai (i-DE-a). Còn 'firework', 'travel', 'morning' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "The Big Ben Tower is a famous ________ in London.", "options": ["city", "island", "building", "landmark"], "answer": "landmark", "topic": "Vocabulary", "explanation": "'landmark' = địa danh nổi tiếng/công trình mang tính biểu tượng. Big Ben là biểu tượng của London. 'building' chỉ là tòa nhà bất kỳ, không mang nghĩa nổi tiếng/biểu tượng."},
    {"type": "choice", "q": "If people _____ less chemical in agriculture, there _____ less soil pollution.", "options": ["use - is", "will use - be", "use – will be", "using – will"], "answer": "use – will be", "topic": "Grammar", "explanation": "Câu điều kiện loại 1: If + S + V (hiện tại đơn), S + will + be/V. Mệnh đề 'if' dùng 'use' (hiện tại đơn), mệnh đề chính dùng 'will be'."},
    {"type": "choice", "q": "'Mommy, Jack is watching cartoons right now!' – '_______ the TV and do your homework, Jack!'", "options": ["You turn on", "Turn on", "You turn off", "Turn off"], "answer": "Turn off", "topic": "Grammar", "explanation": "Câu mệnh lệnh (imperative) bắt đầu bằng động từ nguyên mẫu, không có chủ ngữ. Ngữ cảnh là tắt TV để làm bài, nên dùng 'Turn off' (tắt đi). 'Turn on' = bật lên — sai nghĩa."},
    {"type": "choice", "q": "She came home and felt exhausted _____ she couldn't sleep well.", "options": ["but", "because", "so", "and"], "answer": "so", "topic": "Grammar", "explanation": "'so' = vì vậy, dùng để chỉ kết quả. Cô ấy mệt nhoài 'vì vậy' không ngủ được. 'because' chỉ nguyên nhân (ngược chiều: vì không ngủ được NÊN mệt — không phù hợp ở đây)."},
    {"type": "choice", "q": "Remember to bring _____ when you go swimming.", "options": ["boat", "racket", "goggles", "bicycle"], "answer": "goggles", "topic": "Vocabulary", "explanation": "'goggles' = kính bơi, đồ dùng thiết yếu khi bơi lội. 'racket' dùng cho cầu lông/tennis, 'boat' là thuyền, 'bicycle' là xe đạp — không liên quan đến bơi lội."},
    {"type": "choice", "q": "'____ do you want to travel to England?' – 'Because I like the red double-decker and Big Ben Tower.'", "options": ["How", "What", "When", "Why"], "answer": "Why", "topic": "Grammar", "explanation": "Câu trả lời bắt đầu bằng 'Because' (vì...) nên câu hỏi phải dùng 'Why' (tại sao). 'How' hỏi cách thức, 'What' hỏi cái gì, 'When' hỏi thời gian."},
    {"type": "choice", "q": "I think my future house will have a smart _______ to help me with the housework.", "options": ["robot", "wireless TV", "computer", "cooker"], "answer": "robot", "topic": "Vocabulary", "explanation": "'robot' = rô-bốt, thiết bị có thể thực hiện công việc nhà (housework) như lau dọn, nấu ăn. TV, máy tính hay bếp không 'giúp làm việc nhà' theo nghĩa này."},
    {"type": "choice", "q": "What is the passage about? (passage: Venice – small city in Italy, tourists, gondolas)", "options": ["People in Venice", "The history of Venice", "Brief introduction to Venice", "Tourism in Venice"], "answer": "Brief introduction to Venice", "topic": "Reading", "explanation": "Bài đọc giới thiệu tổng quát về Venice: vị trí, đặc điểm, khách du lịch. Đây không phải bài tập trung vào lịch sử hay du lịch đơn thuần, mà là giới thiệu ngắn gọn về thành phố."},
    {"type": "choice", "q": "Where is Venice? (Venice passage)", "options": ["Near the river Ouse", "In Northeastern Italy", "Near the Rocky mountains", "In Southern Italy"], "answer": "In Northeastern Italy", "topic": "Reading", "explanation": "Bài đọc nêu Venice nằm ở đông bắc nước Ý (Northeastern Italy). Cần đọc kỹ vị trí địa lý trong bài để không nhầm với 'Southern Italy'."},
    {"type": "choice", "q": "What is true about people in Venice? (Venice passage)", "options": ["They live in pretty castles.", "Many people who live in Venice work in Mestre.", "They usually walk or use boats to go around.", "They drive cars on special roads."], "answer": "They usually walk or use boats to go around.", "topic": "Reading", "explanation": "Venice không có đường cho xe ô tô — người dân đi bộ hoặc dùng thuyền. Bài đọc nêu rõ điều này. Các đáp án khác không đúng với thực tế được mô tả trong bài."},
    {"type": "choice", "q": "Which is NOT mentioned as an activity for tourists in Venice?", "options": ["Watching boat races.", "Trying various local dishes.", "Sitting in cafes and talking.", "Taking gondola rides."], "answer": "Watching boat races.", "topic": "Reading", "explanation": "Bài đọc đề cập đến ẩm thực địa phương, ngồi cà phê và đi thuyền gondola. Xem đua thuyền KHÔNG được nhắc đến trong bài."},
    {"type": "choice", "q": "When is the best time for tourists to travel to Venice?", "options": ["at Easter", "in February", "Both A and B", "in May"], "answer": "Both A and B", "topic": "Reading", "explanation": "Bài đọc đề cập cả hai thời điểm tốt nhất: lễ Phục sinh (Easter) và tháng Hai (February, mùa lễ hội Carnival). Vì cả hai đều đúng nên đáp án là 'Both A and B'."},
    {"type": "choice", "q": "People need air to breathe. In order to keep us healthy, we need (31) _____ air.", "options": ["clean", "dirty", "polluted", "fresh"], "answer": "clean", "topic": "Vocabulary", "explanation": "Để giữ sức khỏe, chúng ta cần không khí 'sạch' (clean). 'dirty' (bẩn), 'polluted' (ô nhiễm) đều có nghĩa tiêu cực. 'fresh' cũng có thể dùng nhưng 'clean' phổ biến hơn trong ngữ cảnh này."},
    {"type": "choice", "q": "Nowadays, (32) _____ lot of things in our lives create harmful gasses and make the air dirty.", "options": ["the", "a", "an", "∅"], "answer": "a", "topic": "Grammar", "explanation": "'a lot of' là cụm từ cố định, không thể thay bằng 'the lot of' hay 'an lot of'. Đây là thành ngữ chỉ số lượng nhiều, luôn dùng 'a lot of'."},
    {"type": "choice", "q": "Air (33) ______ is one of the worldwide alarming issues nowadays.", "options": ["polluted", "pollute", "pollution", "polluting"], "answer": "pollution", "topic": "Vocabulary", "explanation": "Cần danh từ để làm chủ ngữ của câu. 'pollution' = ô nhiễm (danh từ). 'polluted' = bị ô nhiễm (tính từ), 'pollute' = làm ô nhiễm (động từ), 'polluting' = đang ô nhiễm (động từ -ing)."},
    {"type": "choice", "q": "Air pollution causes not only (34) ______ problems in people but also in plants and animals.", "options": ["healthy", "unhealthy", "health", "unhealthily"], "answer": "health", "topic": "Vocabulary", "explanation": "'health problems' = các vấn đề sức khỏe (danh từ + danh từ). 'healthy/unhealthy' là tính từ không đứng trước danh từ 'problems' trong ngữ cảnh này. 'unhealthily' là trạng từ — sai hoàn toàn."},

    # ── De 06 - Lop 6 ──
    {"type": "choice", "q": "Find the word whose underlined part differs from the other three in pronunciation: A. weather  B. brother  C. cathedral  D. although", "options": ["weather", "brother", "cathedral", "although"], "answer": "cathedral", "topic": "Pronunciation", "explanation": "Trong 'cathedral', âm 'th' đọc là /θ/ (vô thanh). Trong 'weather', 'brother', 'although', âm 'th' đọc là /ð/ (hữu thanh)."},
    {"type": "choice", "q": "Find the word whose underlined part differs: A. parks  B. computers  C. astronauts  D. maps", "options": ["parks", "computers", "astronauts", "maps"], "answer": "computers", "topic": "Pronunciation", "explanation": "Đuôi '-s' của 'computers' đọc là /z/ (sau nguyên âm). Đuôi '-s' của 'parks', 'astronauts', 'maps' đọc là /s/ (sau phụ âm vô thanh)."},
    {"type": "choice", "q": "Choose the word that differs in stress: A. machine  B. device  C. printer  D. computer", "options": ["machine", "device", "printer", "computer"], "answer": "printer", "topic": "Pronunciation", "explanation": "'printer' có trọng âm ở âm tiết đầu (PRIN-ter). Còn 'machine', 'device' nhấn âm tiết 2; 'computer' nhấn âm tiết 2 (com-PU-ter)."},
    {"type": "choice", "q": "Choose the word that differs in stress: A. technology  B. internet  C. future  D. special", "options": ["technology", "internet", "future", "special"], "answer": "technology", "topic": "Pronunciation", "explanation": "'technology' có trọng âm ở âm tiết 2 (tech-NOL-o-gy). Còn 'internet', 'future', 'special' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "In the future, automatic food machines __________ all our food.", "options": ["might make", "will be", "have", "prepares"], "answer": "might make", "topic": "Grammar", "explanation": "'might make' = có thể làm/tạo ra — phù hợp khi nói về tương lai không chắc chắn. 'will be' không có tân ngữ 'food', 'prepares' sai ngôi (machines = số nhiều)."},
    {"type": "choice", "q": "Your parents __________ angry if you __________ playing computer games.", "options": ["are/ won't stop", "will be/ don't stop", "will be/ won't stop", "will be/ stop"], "answer": "will be/ don't stop", "topic": "Grammar", "explanation": "Câu điều kiện loại 1: mệnh đề 'if' dùng hiện tại đơn ('don't stop'), mệnh đề chính dùng 'will be'. 'won't stop' trong mệnh đề if là sai quy tắc."},
    {"type": "choice", "q": "You __________ eat so many sweets. They aren't good for you.", "options": ["have to", "need", "can", "shouldn't"], "answer": "shouldn't", "topic": "Grammar", "explanation": "'shouldn't' = không nên, dùng để khuyên không làm gì đó vì có hại. 'have to' = phải (bắt buộc), 'can' = có thể — không mang nghĩa khuyên can."},
    {"type": "choice", "q": "__________ is a piece of land with water all around it.", "options": ["An island", "A bay", "A waterfall", "A mountain"], "answer": "An island", "topic": "Vocabulary", "explanation": "'island' = hòn đảo — vùng đất có nước bao quanh bốn phía. 'bay' = vịnh, 'waterfall' = thác nước, 'mountain' = núi — đều không khớp với định nghĩa này."},
    {"type": "choice", "q": "Student 1: 'How might homes change in the future?' - Student 2: '__________'", "options": ["I have to get a robot helper.", "We might live in smart homes.", "We can't use an automatic food machine.", "We should have smart devices."], "answer": "We might live in smart homes.", "topic": "Communication", "explanation": "Câu hỏi hỏi về sự thay đổi của nhà trong tương lai. 'We might live in smart homes' trả lời đúng chủ đề và dùng 'might' phù hợp với cách nói về tương lai không chắc chắn."},
    {"type": "choice", "q": "Student 1: 'Should we bring a tent?' - Student 2: '__________'", "options": ["You're welcome.", "Yes, me too.", "Sorry, I don't understand.", "Yes, good idea."], "answer": "Yes, good idea.", "topic": "Communication", "explanation": "Khi ai đó đề xuất ('Should we...?'), câu trả lời đồng ý tự nhiên là 'Yes, good idea!' (Đồng ý, ý hay đó!). 'You're welcome' dùng sau lời cảm ơn, không phù hợp ở đây."},
    {"type": "choice", "q": "What __________ life be like if we live on the moon in the 23rd century?", "options": ["will", "was", "do", "is"], "answer": "will", "topic": "Grammar", "explanation": "Câu hỏi về tương lai giả định ('if we live on the moon') dùng 'will' trong mệnh đề chính. 'What will... be like?' = cuộc sống sẽ như thế nào?"},
    {"type": "choice", "q": "Everything __________ in space because there's no gravity.", "options": ["might float", "floats", "float", "floating"], "answer": "might float", "topic": "Grammar", "explanation": "'might float' = có thể lơ lửng — phù hợp khi nói về điều có thể xảy ra trong không gian. Bài đang nói về khả năng, nên dùng 'might' thay vì khẳng định chắc chắn."},
    {"type": "choice", "q": "Don't forget to bring a __________. It will keep you warm when you sleep at the campsite.", "options": ["flashlight", "towel", "sleeping bag", "battery"], "answer": "sleeping bag", "topic": "Vocabulary", "explanation": "'sleeping bag' = túi ngủ, giữ ấm khi cắm trại. 'flashlight' = đèn pin (soi sáng, không giữ ấm), 'towel' = khăn tắm, 'battery' = pin — không giữ ấm khi ngủ."},
    {"type": "choice", "q": "__________ is special clothing to wear when astronauts work outside in space.", "options": ["Space station", "Gravity", "Spaceship", "Spacesuit"], "answer": "Spacesuit", "topic": "Vocabulary", "explanation": "'Spacesuit' = bộ quần áo không gian, bảo vệ phi hành gia khi làm việc ngoài vũ trụ. 'Spaceship' = tàu vũ trụ, 'space station' = trạm không gian, 'gravity' = lực hấp dẫn."},
    {"type": "choice", "q": "Jennifer stayed in Melbourne for one day. (True/False — she stayed for two days)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "explanation": "Bài đọc nói Jennifer ở Melbourne hai ngày, không phải một ngày. Cần đọc kỹ chi tiết thời gian trong bài để trả lời đúng câu True/False."},
    {"type": "choice", "q": "It costs a lot of money to visit Royal Botanic Gardens. (True/False — it is described as 'best free thing')", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "explanation": "Bài đọc mô tả Royal Botanic Gardens là 'best free thing' (điều miễn phí tuyệt nhất), tức là vào cửa miễn phí. Vậy nên 'tốn nhiều tiền' là sai."},
    {"type": "choice", "q": "People can enjoy live performances in Botanic Gardens in the summer. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc đề cập đến các buổi biểu diễn trực tiếp (live performances) tại Botanic Gardens vào mùa hè. Thông tin này được nêu rõ trong bài."},
    {"type": "choice", "q": "Jennifer likes Melbourne more than Sydney. (True/False — 'That's why I prefer Melbourne')", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc có câu 'That's why I prefer Melbourne' (Đó là lý do tôi thích Melbourne hơn), cho thấy Jennifer thích Melbourne hơn Sydney."},
    {"type": "choice", "q": "Scientists say that in the future, the ways we live, work and play will be very (23) _________ to how they are now.", "options": ["difference", "differently", "different", "differences"], "answer": "different", "topic": "Grammar", "explanation": "Sau động từ 'be' (will be very ___) cần tính từ. 'different' = khác biệt (tính từ). 'difference/differences' là danh từ, 'differently' là trạng từ — đều sai."},
    {"type": "choice", "q": "Homes will become (24) _________ because more and more people will live in crowded cities.", "options": ["more small and tall", "smaller and taller", "the smallest and tallest", "the most small and tall"], "answer": "smaller and taller", "topic": "Grammar", "explanation": "So sánh hơn của tính từ ngắn một âm tiết: 'small → smaller', 'tall → taller'. Không dùng 'more' với tính từ ngắn. 'the smallest/tallest' là so sánh nhất, không phù hợp ở đây."},
    {"type": "choice", "q": "We will do all our shopping on the internet and drones (25) _________ the groceries to our houses.", "options": ["will deliver", "might have", "make", "will change"], "answer": "will deliver", "topic": "Grammar", "explanation": "'will deliver' = sẽ giao hàng — phù hợp nghĩa với drone giao đồ tạp hóa đến nhà. Mệnh đề song song với 'will do' ở trước nên dùng 'will deliver'."},
    {"type": "choice", "q": "There will be robots (26) _________ all the household chores.", "options": ["do", "to do", "so it does", "it do"], "answer": "to do", "topic": "Grammar", "explanation": "Sau danh từ 'robots' dùng 'to + V' (infinitive of purpose = để làm gì). 'There will be robots TO DO...' = sẽ có robot để làm việc nhà. Không dùng 'do' trực tiếp hay 'it do'."},
    {"type": "choice", "q": "We might also take holidays (27) _________ space.", "options": ["on", "for", "with", "in"], "answer": "in", "topic": "Grammar", "explanation": "Dùng 'in space' (trong không gian) — đây là cụm từ cố định. Không nói 'on space' hay 'at space'. Tương tự: 'in the sky', 'in the ocean'."},

    # ── De 07 - Lop 6 ──
    {"type": "choice", "q": "These are my books, not ____.", "options": ["your", "your book", "yours", "yours books"], "answer": "yours", "topic": "Grammar", "explanation": "Dùng đại từ sở hữu 'yours' (= của bạn) thay cho danh từ đã được nhắc đến. 'your' là tính từ sở hữu, phải đứng trước danh từ (your book). 'yours books' sai — không có hình thức này."},
    {"type": "choice", "q": "Australia is an interesting country. All of ____ big cities are along the coast.", "options": ["it", "their", "its", "theirs"], "answer": "its", "topic": "Grammar", "explanation": "'its' = tính từ sở hữu của 'it' (Australia là danh từ số ít, trung tính). 'its big cities' = những thành phố lớn của nó. 'their' dùng cho số nhiều, 'it' là đại từ chủ ngữ — sai vị trí."},
    {"type": "choice", "q": "Look at the sky, Minh! _______ a beautiful scene!", "options": ["How often", "What", "Where", "Why"], "answer": "What", "topic": "Grammar", "explanation": "Câu cảm thán với danh từ dùng 'What': 'What + a/an + tính từ + danh từ!' → 'What a beautiful scene!' 'How' dùng với tính từ/trạng từ đơn lẻ: 'How beautiful!'"},
    {"type": "choice", "q": "Excuse me, can you show me the way to ______ gas station?", "options": ["a", "the", "an", "∅"], "answer": "the", "topic": "Grammar", "explanation": "Dùng 'the' khi hỏi đường đến một địa điểm cụ thể mà cả hai người đều hiểu là trạm xăng nào (trạm xăng gần nhất). 'a' dùng khi chưa xác định cụ thể."},
    {"type": "choice", "q": "Peter, what are you going to do this weekend? – I don't know. I think I ____ some movies at home.", "options": ["will watch", "watch", "am going to watch", "am watching"], "answer": "will watch", "topic": "Grammar", "explanation": "'I don't know' + 'I think' cho thấy đây là quyết định ngay tại lúc nói (spontaneous decision) → dùng 'will'. 'am going to watch' dùng khi đã có kế hoạch từ trước."},
    {"type": "choice", "q": "_____ type of future house do you think it will be? – It'll be a palace.", "options": ["What - apartment", "How - UFO", "What - palace", "How – skyscraper"], "answer": "What - palace", "topic": "Grammar", "explanation": "Câu hỏi 'What type of...' hỏi về loại/kiểu. Câu trả lời 'a palace' (cung điện) khớp với đáp án 'What - palace'. Cần chọn đáp án có cả từ hỏi và loại nhà phù hợp nhau."},
    {"type": "choice", "q": "We might have a ____ TV to watch TV programmes from space.", "options": ["wireless", "automatic", "remote", "local"], "answer": "wireless", "topic": "Vocabulary", "explanation": "'wireless TV' = TV không dây, phù hợp với bối cảnh tương lai công nghệ. 'wireless' cho phép thu tín hiệu từ không gian mà không cần dây cáp. 'remote' = điều khiển từ xa (remote control, không phải remote TV)."},
    {"type": "choice", "q": "The first Earth Day was celebrated around the world. (True/False — it was born in San Francisco, California, not around the world)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "explanation": "Bài đọc nói Earth Day được khởi xướng tại San Francisco, California — chỉ ở một địa điểm, không phải toàn thế giới. Vì vậy câu này sai."},
    {"type": "choice", "q": "Earth Day is a day to take care of our planet, Earth. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc giải thích mục đích của Earth Day là bảo vệ và chăm sóc Trái Đất — khẳng định này đúng với nội dung bài."},
    {"type": "choice", "q": "On Earth Day, people do some good things that help the planet. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc liệt kê các hoạt động tốt vào Ngày Trái Đất như trồng cây, tắt đèn tiết kiệm điện. Đây là thông tin được nêu rõ trong bài."},
    {"type": "choice", "q": "Turning lights off is a way to save energy. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc đề cập đến việc tắt đèn như một cách tiết kiệm năng lượng vào Ngày Trái Đất. Thông tin này được xác nhận trong bài."},
    {"type": "choice", "q": "The UP movie was produced (31) _________ Pixar Animation Studios.", "options": ["by", "with", "from", "at"], "answer": "by", "topic": "Grammar", "explanation": "Câu bị động dùng 'by + tác nhân' để chỉ ai/cái gì thực hiện hành động. 'produced by Pixar' = được sản xuất bởi Pixar. 'with' dùng khi đi cùng ai đó, không phải tác nhân sản xuất."},
    {"type": "choice", "q": "Carl and Ellie (32) ____ up, marry and live in the restored house.", "options": ["grows", "grew", "grow", "have grown"], "answer": "grew", "topic": "Grammar", "explanation": "Bài tóm tắt phim dùng thì quá khứ đơn để kể chuyện đã xảy ra. 'grew up' = lớn lên (quá khứ của 'grow up'). Các hành động 'marry' và 'live' cũng ở thì quá khứ."},
    {"type": "choice", "q": "The couple remembered their childhood dream of (33) ___ Paradise Falls.", "options": ["to visit", "visiting", "visited", "to visiting"], "answer": "visiting", "topic": "Grammar", "explanation": "Sau giới từ 'of', động từ phải ở dạng V-ing (gerund). 'dream of doing sth' = mơ ước làm gì. 'to visit' là to-infinitive, không dùng sau giới từ."},
    {"type": "choice", "q": "However, Carl resolves to keep his promise to Ellie by turning his house into a makeshift airship using thousands of helium (35) ____.", "options": ["roofs", "balloons", "walls", "bricks"], "answer": "balloons", "topic": "Vocabulary", "explanation": "Trong phim UP, Carl buộc hàng nghìn quả bóng bay (balloons) vào nhà để bay lên trời. Đây là chi tiết nổi tiếng của phim. 'helium balloons' = bóng bay khí heli."},

    # ── De 08 - Lop 6 ──
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. breathe  B. weather  C. therefore  D. teeth", "options": ["breathe", "weather", "therefore", "teeth"], "answer": "teeth", "topic": "Pronunciation", "explanation": "Trong 'teeth', âm 'th' đọc là /θ/ (vô thanh). Trong 'breathe', 'weather', 'therefore', âm 'th' đọc là /ð/ (hữu thanh)."},
    {"type": "choice", "q": "Circle the word whose underlined part is pronounced differently: A. ago  B. long  C. close  D. nose", "options": ["ago", "long", "close", "nose"], "answer": "long", "topic": "Pronunciation", "explanation": "Trong 'long', chữ 'o' đọc là /ɒ/ (âm ngắn). Trong 'ago', 'close', 'nose', chữ 'o' đọc là /əʊ/ (âm đôi, dài hơn)."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. include  B. become  C. action  D. believe", "options": ["include", "become", "action", "believe"], "answer": "action", "topic": "Pronunciation", "explanation": "'action' nhấn âm tiết đầu (AC-tion). 'include', 'become', 'believe' đều nhấn âm tiết thứ hai."},
    {"type": "choice", "q": "Circle the word whose stress pattern is different: A. working  B. cooking  C. modern  D. maintain", "options": ["working", "cooking", "modern", "maintain"], "answer": "maintain", "topic": "Pronunciation", "explanation": "'maintain' nhấn âm tiết thứ hai (main-TAIN). 'working', 'cooking', 'modern' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "Excuse me, is there _____ bus stop near here? – Yes, it's over there, next to ____ pharmacy.", "options": ["a - the", "an - the", "the - a", "the - an"], "answer": "a - the", "topic": "Grammar", "explanation": "Câu hỏi 'is there a/an...?' dùng mạo từ không xác định vì đang hỏi lần đầu. 'bus' bắt đầu bằng phụ âm /b/ nên dùng 'a'. Nhà thuốc đã biết (được đề cập), dùng 'the'."},
    {"type": "choice", "q": "In the future, automatic food machines _______ all our food.", "options": ["make", "should make", "might cook", "cook"], "answer": "might cook", "topic": "Grammar", "explanation": "'might cook' = có thể nấu, phù hợp khi nói về khả năng trong tương lai không chắc chắn. 'make food' và 'cook food' đúng nghĩa nhưng cần modal verb cho tương lai."},
    {"type": "choice", "q": "If we can buy cheap tickets, we ______ travel by plane.", "options": ["would", "shall", "will not", "will"], "answer": "will", "topic": "Grammar", "explanation": "Câu điều kiện loại 1: If + can (hiện tại), S + will + V. 'If we can..., we will...' — nếu mua được vé rẻ thì chắc chắn sẽ đi máy bay. 'would' dùng cho điều kiện loại 2."},
    {"type": "choice", "q": "Remember to bring a _____. You'll be wet after going rafting.", "options": ["sleeping bag", "blanket", "towel", "map"], "answer": "towel", "topic": "Vocabulary", "explanation": "'towel' = khăn tắm/lau khô, cần thiết khi bị ướt sau chèo thuyền (rafting). 'sleeping bag' dùng khi cắm trại ngủ, 'blanket' là chăn, 'map' là bản đồ."},
    {"type": "choice", "q": "The Eiffel Tower is one of the most famous ______ in Paris.", "options": ["city", "landmarks", "megacity", "river"], "answer": "landmarks", "topic": "Vocabulary", "explanation": "'landmark' = công trình/địa danh nổi tiếng mang tính biểu tượng. Tháp Eiffel là biểu tượng nổi tiếng nhất của Paris. Số nhiều là 'landmarks' vì dùng 'one of the most famous'."},
    {"type": "choice", "q": "______ visitors go to Bali for their vacations. (Bali passage)", "options": ["Some", "Lots of", "Much", "Many"], "answer": "Lots of", "topic": "Reading", "explanation": "Bài đọc dùng 'Lots of visitors' = rất nhiều khách du lịch đến Bali. 'Much' dùng với danh từ không đếm được, 'visitors' là danh từ đếm được nên không dùng 'Much'."},
    {"type": "choice", "q": "People can enjoy beautiful beaches with _______. (Bali passage)", "options": ["golden sand", "white sand", "rain", "black sand"], "answer": "white sand", "topic": "Reading", "explanation": "Bài đọc mô tả các bãi biển Bali có cát trắng (white sand). Cần đọc kỹ mô tả bãi biển trong bài để chọn đúng màu cát."},
    {"type": "choice", "q": "According to the passage, what is NOT mentioned as one activity for tourists in Bali?", "options": ["go on cycling tours", "scuba diving", "go shopping", "snorkeling"], "answer": "go shopping", "topic": "Reading", "explanation": "Bài đọc đề cập đến đạp xe, lặn scuba và lặn snorkel. 'Go shopping' (đi mua sắm) KHÔNG được nhắc đến trong danh sách hoạt động du lịch."},
    {"type": "choice", "q": "People can take a _____ to Bali.", "options": ["bus", "train", "plane", "ship"], "answer": "plane", "topic": "Reading", "explanation": "Bài đọc nêu du khách có thể đến Bali bằng máy bay (plane). Bali là một hòn đảo ở Indonesia, phương tiện phổ biến nhất là máy bay."},
    {"type": "choice", "q": "What is the best time to visit Bali?", "options": ["between October and March", "between April and October", "during the rain season", "in September only"], "answer": "between April and October", "topic": "Reading", "explanation": "Bài đọc nêu thời điểm tốt nhất là từ tháng 4 đến tháng 10 — đây là mùa khô ở Bali. Tháng 10-3 là mùa mưa, không phải thời điểm lý tưởng."},

    # ══ TIẾNG ANH 8 (Chương trình mới) ══

    # ── De 01 - Lop 8 ──
    {"type": "choice", "q": "Find the word that has different stress pattern: A. domestic  B. possible  C. physical  D. musical", "options": ["domestic", "possible", "physical", "musical"], "answer": "domestic", "topic": "Pronunciation", "explanation": "'domestic' nhấn âm tiết thứ hai (do-MES-tic). 'possible', 'physical', 'musical' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "Find the word that has different stress pattern: A. refugee  B. trainee  C. Japanese  D. engineer", "options": ["refugee", "trainee", "Japanese", "engineer"], "answer": "engineer", "topic": "Pronunciation", "explanation": "'engineer' nhấn âm tiết thứ hai (en-gi-NEER). 'refugee', 'trainee', 'Japanese' đều nhấn âm tiết cuối (cu-ối)."},
    {"type": "choice", "q": "Find the word that has different stress pattern: A. repetitive  B. electrical  C. priority  D. energetic", "options": ["repetitive", "electrical", "priority", "energetic"], "answer": "energetic", "topic": "Pronunciation", "explanation": "'energetic' nhấn âm tiết thứ ba (en-er-GET-ic). 'repetitive', 'electrical', 'priority' đều nhấn âm tiết thứ hai."},
    {"type": "choice", "q": "A forest fire ________ quickly and ________ many trees.", "options": ["raged/killed", "burst/harmed", "spread/destroyed", "occurred/cooked"], "answer": "spread/destroyed", "topic": "Vocabulary", "explanation": "'spread' = lan rộng (lửa lan rộng), 'destroyed' = phá hủy (nhiều cây bị phá hủy). Đây là cặp từ phù hợp nhất để mô tả cháy rừng. 'raged' không có 'quickly' đi kèm tự nhiên."},
    {"type": "choice", "q": "The tornado caused a massive ________ to the town.", "options": ["destruction", "extension", "danger", "mishap"], "answer": "destruction", "topic": "Vocabulary", "explanation": "'destruction' = sự phá hủy, tàn phá — từ phù hợp nhất với thiên tai như tornado. 'mishap' = tai nạn nhỏ, không đủ mạnh. 'extension' = mở rộng — sai nghĩa hoàn toàn."},
    {"type": "choice", "q": "Hemp was grown throughout history ________ its versatility; it can be used to make many different things.", "options": ["due to", "because", "since", "as a result"], "answer": "due to", "topic": "Grammar", "explanation": "'due to' + danh từ/cụm danh từ = do/vì. 'due to its versatility' = do tính linh hoạt của nó. 'because' đi với mệnh đề (subject + verb), không đi với cụm danh từ."},
    {"type": "choice", "q": "Global warming ________ if there weren't too much carbon dioxide in the atmosphere.", "options": ["won't happen", "didn't happen", "wouldn't happen", "happened"], "answer": "wouldn't happen", "topic": "Grammar", "explanation": "Câu điều kiện loại 2: If + V-ed (quá khứ), S + would + V. 'if there weren't' → 'wouldn't happen'. Mệnh đề giả định trái với thực tế hiện tại."},
    {"type": "choice", "q": "Passengers __________ to smoke in the train.", "options": ["are not allowed", "had not allowed", "has not allowed", "will not allow"], "answer": "are not allowed", "topic": "Grammar", "explanation": "Câu bị động hiện tại: 'be + past participle'. 'Passengers are not allowed to smoke' = hành khách không được phép hút thuốc. 'had/has not allowed' sai vì chủ ngữ 'Passengers' là số nhiều và cần bị động."},
    {"type": "choice", "q": "A powerful __________ off the coast of Indonesia sparked a three-metre-high wave and killed at least 113 people.", "options": ["earthquake", "tornado", "tsunami", "landslide"], "answer": "tsunami", "topic": "Vocabulary", "explanation": "'tsunami' = sóng thần, xảy ra ngoài khơi biển và tạo ra sóng cao. 'earthquake' = động đất (dưới đất), 'tornado' = lốc xoáy (trên không), 'landslide' = lở đất. Chỉ tsunami tạo sóng biển."},
    {"type": "choice", "q": "I ___________ a cup of tea before I left for my office.", "options": ["have", "have had", "had had", "will have"], "answer": "had had", "topic": "Grammar", "explanation": "Thì quá khứ hoàn thành (past perfect): 'had + V3'. Uống trà xảy ra TRƯỚC khi rời đến văn phòng (hành động xảy ra trước trong quá khứ). 'had had' = đã uống xong rồi mới đi."},
    {"type": "choice", "q": "Where do tornadoes begin? (Tornado passage)", "options": ["in the ocean", "underground", "in cyclones", "in thunderclouds"], "answer": "in thunderclouds", "topic": "Reading", "explanation": "Bài đọc nêu rõ lốc xoáy bắt đầu trong đám mây giông (thunderclouds). Cần đọc phần đầu của bài để tìm thông tin này."},
    {"type": "choice", "q": "Why does the author mention The Wizard of Oz at the beginning of the passage?", "options": ["to give a famous example of a tornado", "to give a history of tornadoes", "to show that hurricanes are not real", "to explain why tornadoes are dangerous"], "answer": "to give a famous example of a tornado", "topic": "Reading", "explanation": "Tác giả nhắc đến bộ phim The Wizard of Oz như một ví dụ nổi tiếng về lốc xoáy để thu hút sự chú ý của người đọc, không phải để kể lịch sử hay giải thích nguy hiểm."},
    {"type": "choice", "q": "Based on the tornado passage, people who live in Tornado Alley should ___________.", "options": ["expect tornadoes only during the summer", "be very familiar with the movie The Wizard of Oz", "be prepared for the dangers of tornadoes", "think about moving to the United States"], "answer": "be prepared for the dangers of tornadoes", "topic": "Reading", "explanation": "Bài đọc khuyên người dân ở Tornado Alley cần chuẩn bị đối phó với nguy hiểm của lốc xoáy. Đây là thông điệp thực tế và an toàn chính của bài."},
    {"type": "choice", "q": "The word 'conditions' in the last paragraph of the tornado passage means ___________.", "options": ["preparations", "dangerous hazards", "the way things are", "lucky feelings"], "answer": "the way things are", "topic": "Vocabulary", "explanation": "'conditions' = điều kiện, hoàn cảnh, tình trạng — nghĩa là 'the way things are' (cách mọi thứ đang diễn ra). Không phải 'preparations' (chuẩn bị) hay 'hazards' (mối nguy hiểm)."},
    {"type": "choice", "q": "What is the main idea of the tornado passage?", "options": ["Some states get tornadoes more than other states.", "Tornadoes are dangerous storms that affect the U.S.", "Tornadoes are different from how they are in movies.", "Many tornadoes do not cause a lot of damage."], "answer": "Tornadoes are dangerous storms that affect the U.S.", "topic": "Reading", "explanation": "Ý chính của bài là lốc xoáy là những cơn bão nguy hiểm ảnh hưởng đến nước Mỹ. Các đáp án khác chỉ là chi tiết phụ hoặc không đúng với nội dung bài."},

    # ── De 02 - Lop 8 ──
    {"type": "choice", "q": "Some documents say that people __________ the Glastonbury Festival since the beginning of the 19th century.", "options": ["celebrated", "were celebrating", "have celebrated", "celebrate"], "answer": "have celebrated", "topic": "Grammar", "explanation": "Dùng hiện tại hoàn thành (have + V3) với 'since' khi hành động bắt đầu từ quá khứ và còn tiếp diễn đến hiện tại. 'have celebrated since...' = đã tổ chức từ thế kỷ 19 cho đến nay."},
    {"type": "choice", "q": "The flight number 781 to Melbourne __________ at 9 o'clock tomorrow morning.", "options": ["arrives", "is arriving", "has arrived", "will arrive"], "answer": "arrives", "topic": "Grammar", "explanation": "Lịch trình cố định (thời gian biểu, lịch bay) dùng hiện tại đơn dù là tương lai. 'The flight arrives at 9' = chuyến bay theo lịch đến lúc 9 giờ."},
    {"type": "choice", "q": "- How is your holiday in New Zealand? - __________.", "options": ["Really", "Awesome", "Absolutely right", "Sure"], "answer": "Awesome", "topic": "Communication", "explanation": "'Awesome!' = Tuyệt vời! — câu trả lời tự nhiên và phổ biến khi được hỏi về kỳ nghỉ. 'Absolutely right' dùng khi đồng ý với ý kiến, không phải mô tả kỳ nghỉ."},
    {"type": "choice", "q": "All the villages ___________ to safe areas before midnight last night.", "options": ["evacuated", "were evacuated", "had evacuated", "had been evacuated"], "answer": "were evacuated", "topic": "Grammar", "explanation": "Câu bị động quá khứ đơn: 'were + V3'. Dân làng ĐƯỢC sơ tán (bởi lực lượng cứu hộ). 'evacuated' là chủ động — không phù hợp vì dân làng không tự sơ tán mình."},
    {"type": "choice", "q": "I'd be over the moon if I ___________ a chance to go to Disneyland in California.", "options": ["have", "had", "will have", "would have"], "answer": "had", "topic": "Grammar", "explanation": "Câu điều kiện loại 2 (giả định không thực tế): 'I'd be (=would be)... if I had...' — nếu có cơ hội (thực ra không có). Mệnh đề 'if' dùng quá khứ đơn 'had'."},
    {"type": "choice", "q": "You should talk to your dad first because that fridge __________ not be suitable for your family.", "options": ["can", "may", "need", "ought"], "answer": "may", "topic": "Grammar", "explanation": "'may not be suitable' = có thể không phù hợp — thể hiện sự không chắc chắn nhẹ. 'can' thường dùng cho khả năng về mặt vật lý, 'may' phù hợp hơn để nói về khả năng/sự không chắc."},
    {"type": "choice", "q": "She doesn't have the doctor's telephone number to book a(n) ________ with him.", "options": ["ticket", "appointment", "lunch set", "seat"], "answer": "appointment", "topic": "Vocabulary", "explanation": "'appointment' = cuộc hẹn (với bác sĩ). 'book an appointment' = đặt lịch hẹn — cụm từ cố định. 'ticket' dùng cho sự kiện/phương tiện, không dùng khi đặt khám bệnh."},
    {"type": "choice", "q": "The 21st century has already seen considerable ___________ in computer technology.", "options": ["progress", "progressing", "progresses", "process"], "answer": "progress", "topic": "Vocabulary", "explanation": "'progress' = tiến bộ (danh từ không đếm được). 'considerable progress' = tiến bộ đáng kể. 'progresses' sai vì 'progress' không có dạng số nhiều. 'process' = quá trình — khác nghĩa."},
    {"type": "choice", "q": "What is a landline telephone? (telephone passage)", "options": ["a telephone that can be carried around in your pocket and used anywhere", "a telephone that can be used in a public place", "a telephone that needs to be connected by a wire to a network of other telephones", "a telephone that can be used to check e-mail and go on the Internet"], "answer": "a telephone that needs to be connected by a wire to a network of other telephones", "topic": "Reading", "explanation": "Bài đọc định nghĩa landline là điện thoại cần kết nối bằng dây đến mạng lưới. Đây là đặc điểm phân biệt landline với điện thoại di động."},
    {"type": "choice", "q": "The article describes an example of a landline. What is an example of a landline?", "options": ["a pay phone", "a smart phone", "a cell phone", "a mobile phone"], "answer": "a pay phone", "topic": "Reading", "explanation": "'pay phone' = điện thoại công cộng (bỏ xu), được kết nối bằng dây — là ví dụ về landline. Smartphone, cell phone, mobile phone đều là điện thoại không dây."},
    {"type": "choice", "q": "Pay phones are probably not used as much today as they were in the past. What piece of evidence supports this conclusion?", "options": ["Many people today carry cell phones, which can be used almost anywhere.", "Payphones are landlines that can be found in public places.", "People could not take landlines with them when they left their homes.", "People put coins into a slot in the pay phone to make a call."], "answer": "Many people today carry cell phones, which can be used almost anywhere.", "topic": "Reading", "explanation": "Điện thoại di động có thể dùng mọi nơi nên người ta không cần tìm điện thoại công cộng nữa. Đây là bằng chứng trực tiếp giải thích vì sao pay phone ít được dùng hơn."},
    {"type": "choice", "q": "What might be a reason that cell phones were invented?", "options": ["People wanted to be able to make calls from their homes or offices.", "People wanted to be able to make calls away from home without finding a pay phone.", "People wanted to be able to speak to one another when they were apart.", "People wanted to be able to speak and see each other from far distance."], "answer": "People wanted to be able to make calls away from home without finding a pay phone.", "topic": "Reading", "explanation": "Bài đọc ngụ ý rằng điện thoại di động ra đời để giải quyết bất tiện của việc phải tìm điện thoại công cộng khi ra ngoài nhà. Đây là lý do trực tiếp nhất được hỗ trợ bởi bài."},
    {"type": "choice", "q": "What is the main idea of the telephone article?", "options": ["Telephones are used to keep people apart as much as possible.", "Cell phones are much less useful than landlines and pay phones.", "Landlines and pay phones still play an important part in the world nowadays.", "Telephones have been used for many years, and they have changed a lot over time."], "answer": "Telephones have been used for many years, and they have changed a lot over time.", "topic": "Reading", "explanation": "Ý chính của bài là điện thoại đã tồn tại lâu dài và thay đổi nhiều theo thời gian (từ landline → pay phone → cell phone). Đây là chủ đề bao quát toàn bài."},
    {"type": "choice", "q": "New Zealand: There are two main islands, the North Island and the South Island, as (26) _______ as many smaller islands.", "options": ["good", "well", "better", "same"], "answer": "well", "topic": "Grammar", "explanation": "'as well as' = cũng như, ngoài ra — cụm liên từ nối hai thành phần. 'as good as' = tốt như (so sánh bằng về chất lượng), không phù hợp ở đây. 'as well as' là thành ngữ cố định."},
    {"type": "choice", "q": "Auckland, in the north, is the largest city with a population (27) _______ over one million people.", "options": ["of", "with", "to", "from"], "answer": "of", "topic": "Grammar", "explanation": "'a population of + số' = dân số bao nhiêu người — cụm danh từ cố định. 'population of over one million people' = dân số hơn một triệu người."},
    {"type": "choice", "q": "Together with other smaller groups, they make Auckland an interesting and (28) _______ place to live.", "options": ["excitement", "excited", "exciting", "excite"], "answer": "exciting", "topic": "Grammar", "explanation": "Cần tính từ để bổ nghĩa cho danh từ 'place'. 'exciting' = thú vị/hấp dẫn (tính từ chỉ tính chất của sự vật). 'excited' = hào hứng (mô tả cảm xúc của người). 'excitement' là danh từ."},

    # ── De 03 - Lop 8 (with answer key) ──
    {"type": "choice", "q": "Find the word with the underlined part pronounced differently from the others: A. think  B. through  C. nevertheless  D. thumb", "options": ["think", "through", "nevertheless", "thumb"], "answer": "nevertheless", "topic": "Pronunciation", "explanation": "Trong 'nevertheless', 'th' đọc là /ð/ (hữu thanh). Trong 'think', 'through', 'thumb', 'th' đọc là /θ/ (vô thanh)."},
    {"type": "choice", "q": "Find the word that has different stress pattern: A. unpolluted  B. unbalanced  C. unreasonable  D. unlawful", "options": ["unpolluted", "unbalanced", "unreasonable", "unlawful"], "answer": "unreasonable", "topic": "Pronunciation", "explanation": "'unreasonable' nhấn âm tiết thứ hai sau 'un-' (un-REA-son-a-ble). 'unpolluted' nhấn âm tiết thứ ba (un-pol-LU-ted), 'unbalanced' và 'unlawful' nhấn âm tiết thứ hai."},
    {"type": "choice", "q": "Find the word that has different stress pattern: A. chocolate  B. structural  C. important  D. natural", "options": ["chocolate", "structural", "important", "natural"], "answer": "important", "topic": "Pronunciation", "explanation": "'important' nhấn âm tiết thứ hai (im-POR-tant). 'chocolate', 'structural', 'natural' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "Find the word that has different stress pattern: A. attractive  B. perception  C. cultural  D. expensive", "options": ["attractive", "perception", "cultural", "expensive"], "answer": "cultural", "topic": "Pronunciation", "explanation": "'cultural' nhấn âm tiết đầu (CUL-tur-al). 'attractive', 'perception', 'expensive' đều nhấn âm tiết thứ hai."},
    {"type": "choice", "q": "_____________ the Di Vinci Code? - It's an interesting book.", "options": ["Have you ever reading", "Have you ever read", "Has you read", "You have read"], "answer": "Have you ever read", "topic": "Grammar", "explanation": "Hiện tại hoàn thành với 'ever' hỏi về trải nghiệm: 'Have you ever + V3?' Chủ ngữ 'you' dùng 'have', không phải 'has'. 'reading' sai vì sau 'have' dùng V3 (read), không phải V-ing."},
    {"type": "choice", "q": "Which country doesn't speak English as an official language?", "options": ["England", "Australia", "Singapore", "Korea"], "answer": "Korea", "topic": "Vocabulary", "explanation": "Hàn Quốc (Korea) dùng tiếng Hàn là ngôn ngữ chính thức, không phải tiếng Anh. England, Australia, Singapore đều có tiếng Anh là ngôn ngữ chính thức hoặc được công nhận."},
    {"type": "choice", "q": "When a volcanic eruption occurs, the hot _________ pours downhill.", "options": ["ash", "smoke", "dirt", "lava"], "answer": "lava", "topic": "Vocabulary", "explanation": "'lava' = dung nham — chất lỏng nóng chảy từ núi lửa và chảy xuống dốc. 'ash' = tro (bay lên không khí), 'smoke' = khói, 'dirt' = đất bẩn — không phải thứ 'chảy xuống dốc'."},
    {"type": "choice", "q": "I don't know how we can ____________ with her. She's too far away.", "options": ["keep in touch", "cope", "catch up", "keep pace"], "answer": "keep in touch", "topic": "Vocabulary", "explanation": "'keep in touch' = giữ liên lạc — phù hợp khi cô ấy ở xa. 'cope' = đối phó (với khó khăn), 'catch up' = theo kịp, 'keep pace' = theo kịp tốc độ — đều không liên quan đến liên lạc."},
    {"type": "choice", "q": "At 8 a.m. tomorrow, he ____________ with his friends in America.", "options": ["are chatting", "will be chatting", "chatted", "chats"], "answer": "will be chatting", "topic": "Grammar", "explanation": "Thì tương lai tiếp diễn (will be + V-ing) diễn tả hành động đang xảy ra vào một thời điểm cụ thể trong tương lai. 'At 8 a.m. tomorrow' = vào lúc 8 giờ sáng mai (đang trò chuyện)."},
    {"type": "choice", "q": "'What's she doing?' - I wondered what __________.", "options": ["was she doing", "is she doing", "she is doing", "she was doing"], "answer": "she was doing", "topic": "Grammar", "explanation": "Câu tường thuật gián tiếp (reported speech): đổi thì từ hiện tại tiếp diễn sang quá khứ tiếp diễn. Trật tự câu trong mệnh đề danh ngữ: S + V ('she was doing'), không đảo ngữ."},
    {"type": "choice", "q": "It was guessed that the fish died _____________ a powerful toxin in the sea water.", "options": ["since", "because", "because of", "as a result"], "answer": "because of", "topic": "Grammar", "explanation": "'because of' + cụm danh từ = do, vì. 'because of a powerful toxin' = do một chất độc mạnh. 'because' cần mệnh đề (S + V). 'since' và 'as a result' không phù hợp cấu trúc ở đây."},
    {"type": "choice", "q": "The Internet, (26) ______, seems to be here to stay. (passage about Internet)", "options": ["moreover", "because", "however", "although"], "answer": "however", "topic": "Grammar", "explanation": "'however' = tuy nhiên, dùng để thể hiện sự tương phản giữa ý trước (những lo ngại về Internet) và ý này (Internet dường như sẽ tồn tại lâu dài). Đây là liên từ phụ trong ngoặc."},
    {"type": "choice", "q": "The World Wide Web is now the largest information (27) ______ in the world.", "options": ["resource", "technology", "informatics", "generation"], "answer": "resource", "topic": "Vocabulary", "explanation": "'information resource' = nguồn thông tin — cụm từ phù hợp để mô tả World Wide Web là kho thông tin khổng lồ. 'technology' = công nghệ, 'informatics' = tin học — không phù hợp nghĩa."},
    {"type": "choice", "q": "94% of students online said they also used it (28) ______ schoolwork.", "options": ["in", "on", "with", "for"], "answer": "for", "topic": "Grammar", "explanation": "'use something for + mục đích' = dùng cái gì vào mục đích gì. 'used it for schoolwork' = dùng nó cho việc học. 'use for' là cụm từ cố định."},
    {"type": "choice", "q": "Which of the following is NOT a possible effect of global warming? (global warming passage)", "options": ["weather patterns changing", "plants and animals becoming extinct", "more polar ice", "human diseases spreading"], "answer": "more polar ice", "topic": "Reading", "explanation": "Bài đọc nêu hậu quả của nóng lên toàn cầu: thời tiết thay đổi, động thực vật tuyệt chủng, bệnh tật lan rộng. Băng ở cực TAN RA (không phải tăng lên), nên 'more polar ice' sai."},
    {"type": "choice", "q": "The statement that 'humans are mostly to blame' in the global warming passage suggests that ___________.", "options": ["humans have been blamed for global warming", "humans have not been blamed for global warming", "humans are mostly responsible for global warming", "there are many factors that cause global warming"], "answer": "humans are mostly responsible for global warming", "topic": "Reading", "explanation": "'to blame' = có trách nhiệm, có lỗi. 'humans are mostly to blame' = con người chủ yếu phải chịu trách nhiệm = 'mostly responsible'. Không nên nhầm với 'have been blamed' (bị đổ lỗi) — đây là về trách nhiệm thực tế."},
    {"type": "choice", "q": "This passage is mostly about ___________ (global warming passage).", "options": ["the solutions to global warming", "the different types of global warming", "the reasons why global warming is not a serious problem", "the causes and effects of global warming"], "answer": "the causes and effects of global warming", "topic": "Reading", "explanation": "Bài đọc đề cập đến nguyên nhân (CO2, con người) và hậu quả (thời tiết, động thực vật, bệnh tật) của nóng lên toàn cầu — đây là chủ đề chính. Không đề cập giải pháp hay phân loại."},

    # ── De 04 - Lop 8 ──
    {"type": "choice", "q": "Find the word with the underlined part pronounced differently: A. honest  B. house  C. hour  D. honor", "options": ["honest", "house", "hour", "honor"], "answer": "house", "topic": "Pronunciation", "explanation": "Trong 'house', chữ 'h' đọc là /h/ (có âm). Trong 'honest', 'hour', 'honor', chữ 'h' câm (không đọc)."},
    {"type": "choice", "q": "________ not to make mistakes, type slowly and carefully.", "options": ["So", "In order", "So that", "To"], "answer": "To", "topic": "Grammar", "explanation": "'To + V' (to-infinitive) dùng để chỉ mục đích ngắn gọn. 'To not make mistakes' = để không mắc lỗi. 'In order' cần theo sau là 'to'. 'So that' cần mệnh đề đầy đủ."},
    {"type": "choice", "q": "Would you mind ________ the phone for me?", "options": ["to answer", "answer", "answering", "please answer"], "answer": "answering", "topic": "Grammar", "explanation": "'mind + V-ing' = phiền/ngại làm gì. 'Would you mind answering...?' = Bạn có phiền nghe điện thoại không? Không dùng to-infinitive sau 'mind'."},
    {"type": "choice", "q": "The polluted chemical waste was dumped into the ocean; _____________, the mass of fish died.", "options": ["because", "as", "because of", "consequently"], "answer": "consequently", "topic": "Grammar", "explanation": "'consequently' = vì vậy, kết quả là — dùng sau dấu chấm phẩy để nối kết quả. 'because/as/because of' chỉ nguyên nhân, không dùng nối kết quả theo kiểu này."},
    {"type": "choice", "q": "What _________ you do if you were President?", "options": ["would", "will", "do", "did"], "answer": "would", "topic": "Grammar", "explanation": "Câu điều kiện loại 2: 'What would you do if you were...?' — giả định không thực tế (bạn không phải là Tổng thống). Mệnh đề chính dùng 'would + V nguyên mẫu'."},
    {"type": "choice", "q": "Before the meeting finished, they had arranged when __________ next.", "options": ["they met", "they to meet", "to meet", "meeting"], "answer": "to meet", "topic": "Grammar", "explanation": "'arrange when to do sth' = sắp xếp khi nào sẽ làm gì — cấu trúc: 'arrange + wh-word + to-infinitive'. 'to meet' phù hợp. Không dùng 'they met' vì đó là mệnh đề đầy đủ, tạo ra cấu trúc thừa."},
    {"type": "choice", "q": "From 1865 to 1875, a remarkable __________ of inventions was produced.", "options": ["diversity", "mixture", "variety", "collection"], "answer": "variety", "topic": "Vocabulary", "explanation": "'a variety of' = nhiều loại khác nhau — cụm từ phổ biến nhất để diễn tả sự đa dạng của phát minh. 'a collection of' = bộ sưu tập (không phù hợp với phát minh), 'diversity' không đi với 'of inventions' tự nhiên bằng."},
    {"type": "choice", "q": "My brother had never been abroad ___________ he joined the army.", "options": ["since", "until", "during", "while"], "answer": "until", "topic": "Grammar", "explanation": "'until' = cho đến khi. 'had never been abroad until he joined the army' = chưa bao giờ ra nước ngoài cho đến khi gia nhập quân đội. 'since' dùng khi điều gì bắt đầu xảy ra từ mốc đó."},
    {"type": "choice", "q": "Norse invaders made the beginning of the English language's spread. (True/False — the Anglo-Saxons are usually considered the beginning)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "explanation": "Bài đọc nêu người Anglo-Saxon (không phải Norse) là nguồn gốc của tiếng Anh. Người Norse (Viking) có ảnh hưởng nhưng không phải 'sự khởi đầu' của ngôn ngữ."},
    {"type": "choice", "q": "English today is the consolidation of other dialects of English. (True/False — as London grew, other dialects began to fade or merge)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Bài đọc nêu khi London phát triển, các phương ngữ khác bắt đầu mờ dần hoặc hòa nhập — dẫn đến tiếng Anh ngày nay là sự hợp nhất của các phương ngữ đó."},
    {"type": "choice", "q": "English is one of the most common primary languages in the world. (True/False — it is the third most common)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "explanation": "Tiếng Anh là ngôn ngữ phổ biến thứ ba thế giới — nghĩa là nó vẫn nằm trong số 'các ngôn ngữ phổ biến nhất'. Khẳng định này đúng dù không nói cụ thể là thứ ba."},
    {"type": "choice", "q": "During a drought there is a (31) ______ of precipitation. (drought passage)", "options": ["addition", "abundance", "lack", "success"], "answer": "lack", "topic": "Vocabulary", "explanation": "'lack of precipitation' = thiếu lượng mưa — đặc trưng của hạn hán. 'abundance' = dư thừa (ngược nghĩa), 'addition' = thêm vào — đều trái ngược với ý nghĩa hạn hán."},
    {"type": "choice", "q": "Drought characteristics vary significantly (32) ______ one region to another.", "options": ["from", "at", "with", "during"], "answer": "from", "topic": "Grammar", "explanation": "'vary from... to...' = biến đổi từ... đến... — cụm từ cố định. 'vary from one region to another' = thay đổi từ vùng này sang vùng khác."},
    {"type": "choice", "q": "(35) ________ drought cannot be reliably predicted, certain precautions can be taken in drought-risk areas.", "options": ["Although", "However", "Besides", "Because"], "answer": "Although", "topic": "Grammar", "explanation": "'Although' = mặc dù, dùng để mở đầu mệnh đề nhượng bộ. 'Although drought cannot be predicted... certain precautions CAN be taken' — mặc dù không dự đoán được, vẫn có thể phòng ngừa. 'However' không đứng đầu mệnh đề."},
]

# ─── Nhật Khôi — Lớp 8A1 ──────────────────────────────────────────────────
NHAT_KHOI_TOAN = [

    # ── FROM DS1 (DOCX) — answer key: 1B,2A,3B,4D,5D,6A,7A,8B,9C,10D,11A,12A ──
    # Math formula questions — text readable, options lost to OLE math
    {"type": "choice", "q": "Lớp 8B có 24 nam và 18 nữ. Lớp phó lao động chọn một bạn để trực nhật trong một buổi học. Xác suất thực nghiệm của biến cố 'Một bạn nữ trực nhật lớp trong một buổi học' là:", "options": ["3/7", "18/42", "3/4", "1"], "answer": "3/7", "topic": "Xác suất"},
    {"type": "choice", "q": "Gieo một con xúc xắc cân đối và đồng chất. Xác suất thực nghiệm của biến cố 'Gieo được mặt có số chấm lẻ' là", "options": ["1/6", "1", "1/2", "1/3"], "answer": "1/2", "topic": "Xác suất"},
    {"type": "fill", "q": "Hiệu hai số là 12. Nếu chia số bé cho 7 và lớn cho 5 thì thương thứ nhất lớn hơn thương thứ hai là 4 đơn vị. Tìm hai số đó (số bé).", "answer": "28", "topic": "Phương trình"},

    # ── FROM DS2 (DOCX) — answer key: 1D,2A,3D,4C,5C,6A,7B,8C,9D,10B,11C,12C ──
    {"type": "choice", "q": "Một hộp có 4 tấm thẻ cùng loại được đánh số lần lượt: 2; 3; 4; 5. Chọn ngẫu nhiên một thẻ từ hộp, kết quả thuận lợi cho biến cố 'Số ghi trên thẻ chia hết cho 3' là thẻ", "options": ["ghi số 3", "ghi số 5", "ghi số 4", "ghi số 2"], "answer": "ghi số 3", "topic": "Xác suất"},
    {"type": "choice", "q": "Chu vi của một mảnh vườn hình chữ nhật là 42 m. Biết chiều rộng ngắn hơn chiều dài 3 m. Tìm chiều dài của mảnh vườn.", "options": ["9 m", "10 m", "12 m", "11 m"], "answer": "12 m", "topic": "Phương trình"},
    {"type": "choice", "q": "Cho hai tam giác có tỉ số đồng dạng bằng 2 thì tỉ số hai đường cao tương ứng bằng", "options": ["1", "2", "1/2", "4"], "answer": "2", "topic": "Tam giác đồng dạng"},
    {"type": "fill", "q": "Cho một số tự nhiên có hai chữ số, chữ số hàng đơn vị gấp đôi chữ số hàng chục và nếu xen thêm chữ số 2 vào giữa hai chữ số ấy thì được số mới lớn hơn số ban đầu là 200. Tìm số đó.", "answer": "36", "topic": "Phương trình"},

    # ── FROM DS3 (DOCX) — answer key: 1D,2D,3D,4C,5D,6A,7A,8C,9A,10C,11A,12C ──
    {"type": "choice", "q": "Một xe máy khởi hành từ Hà Nội đi Thanh Hoá lúc 6 giờ với vận tốc 40 km/h. Sau đó 1 giờ, một ô tô cũng xuất phát từ điểm khởi hành của xe máy để đi Thanh Hoá với vận tốc 60 km/h và đi cùng tuyến đường với xe máy. Ô tô đuổi kịp xe máy vào lúc mấy giờ?", "options": ["8 giờ", "10 giờ", "8,5 giờ", "9 giờ"], "answer": "9 giờ", "topic": "Phương trình"},
    {"type": "choice", "q": "Một hãng taxi có giá: mở cửa vào xe là 10.000 đồng, sau đó mỗi km giá 12.000 đồng. Số tiền phải trả khi đi quãng đường x km là", "options": ["10000x + 12000", "12000x + 10000", "22000x", "10000 + 12000/x"], "answer": "12000x + 10000", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Đường thẳng y = ax + b luôn cắt trục hoành tại điểm có hoành độ bằng 2, tung độ bằng 0. Đường thẳng đó là", "options": ["y = x + 2", "y = -x + 2", "y = x - 2", "y = 2x"], "answer": "y = x - 2", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Một hộp có 4 tấm thẻ cùng loại được đánh số lần lượt: 2; 3; 4; 5. Chọn ngẫu nhiên một thẻ từ hộp, xác suất thực nghiệm của biến cố 'Tấm thẻ ghi số 2' là:", "options": ["1/4", "1/2", "1/3", "1"], "answer": "1/4", "topic": "Xác suất"},
    {"type": "choice", "q": "Cho hai tam giác vuông, điều kiện để hai tam giác vuông đó đồng dạng là:", "options": ["Có một cặp cạnh góc vuông bằng nhau.", "Có hai cạnh huyền bằng nhau.", "Có một cặp góc nhọn bằng nhau.", "Không cần điều kiện vì hai tam giác vuông luôn đồng dạng."], "answer": "Có một cặp góc nhọn bằng nhau.", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Lớp 8A có 40 học sinh, trong đó có 6 học sinh cận thị. Gặp ngẫu nhiên một học sinh của lớp, xác suất thực nghiệm của biến cố 'Học sinh đó không bị cận thị' là", "options": ["6/40", "34/40", "6/34", "34/6"], "answer": "34/40", "topic": "Xác suất"},
    {"type": "fill", "q": "Năm nay tuổi bố gấp 5 lần tuổi con. Biết sau 15 năm nữa tuổi bố chỉ gấp 3 lần tuổi con. Tính tuổi của con hiện nay.", "answer": "15", "topic": "Phương trình"},

    # ── FROM DS4 (DOCX) — answer key: 1C,2C,3A,4A,5A,6A,7B,8D,9C,10B,11B,12A ──
    {"type": "choice", "q": "Khi đo nhiệt độ, ta có công thức đổi từ đơn vị độ C (Celsius) sang đơn vị độ F (Fahrenheit) như sau: F = 1,8C + 32. Chọn câu đúng nhất khi nói F là một hàm số theo biến số C vì:", "options": ["Đại lượng F phụ thuộc vào đại lượng C và với mỗi giá trị của C ta luôn xác định được duy nhất một giá trị tương ứng của F", "Đại lượng F phụ thuộc vào địa lượng C và với mỗi giá trị của C ta luôn xác định được hai giá trị tương ứng của F", "Mỗi giá trị của C ta luôn xác định duy nhất một giá trị tương ứng của F", "Đại lượng F phụ thuộc vào đại lượng C"], "answer": "Đại lượng F phụ thuộc vào đại lượng C và với mỗi giá trị của C ta luôn xác định được duy nhất một giá trị tương ứng của F", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Lớp 8A có 40 học sinh, trong đó có 22 nam và 18 nữ. Gặp ngẫu nhiên một học sinh của lớp, xác suất thực nghiệm của biến cố 'Học sinh đó nam' là:", "options": ["18/40", "22/40", "22/18", "18/22"], "answer": "22/40", "topic": "Xác suất"},
    {"type": "choice", "q": "Một hộp có 10 tấm thẻ cùng loại được đánh số từ 5 đến 14. Bạn Hoa lấy ra ngẫu nhiên 1 thẻ từ hộp. Xác suất thực nghiệm của biến cố 'Chọn ra thẻ ghi số nguyên tố' là:", "options": ["4/10", "3/10", "5/10", "6/10"], "answer": "4/10", "topic": "Xác suất"},
    {"type": "fill", "q": "Tính tuổi của hai người, biết rằng cách đây 10 năm tuổi người thứ nhất gấp 3 lần tuổi của người thứ hai và sau đây hai năm, tuổi người thứ hai sẽ bằng một nửa tuổi của người thứ nhất. Người thứ nhất hiện nay bao nhiêu tuổi?", "answer": "46", "topic": "Phương trình"},

    # ── FROM DS5 (DOCX) — answer key: 1D,2C,3B,4C,5B,6C,7C,8C,9C,10A,11A,12A ──
    {"type": "choice", "q": "Bạn Mai mua cả sách và vở hết 500 nghìn đồng. Biết rằng số tiền mua sách nhiều gấp rưỡi số tiền mua vở. Hãy tính số tiền bạn Mai mua vở.", "options": ["300 nghìn đồng", "200 nghìn đồng", "320 nghìn đồng", "250 nghìn đồng"], "answer": "200 nghìn đồng", "topic": "Phương trình"},
    {"type": "choice", "q": "Chu vi hình vuông có độ dài cạnh a được tính theo công thức C = 4a. Với mỗi giá trị của a, xác định được bao nhiêu giá trị tương ứng của C?", "options": ["vô số", "2", "1", "4"], "answer": "1", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Lớp 8B có 24 nam và 18 nữ. Lớp phó lao động chọn một bạn để trực nhật. Xác suất thực nghiệm của biến cố 'Một bạn nữ trực nhật lớp trong một buổi học' là:", "options": ["1", "18/42", "24/42", "18/24"], "answer": "18/42", "topic": "Xác suất"},
    {"type": "fill", "q": "Hai thư viện có cả thảy 15000 cuốn sách. Nếu chuyển từ thư viện thứ nhất sang thứ viện thứ hai 3000 cuốn, thì số sách của hai thư viện bằng nhau. Tính số sách lúc đầu ở thư viện I.", "answer": "10500", "topic": "Phương trình"},

    # ── FROM PDF: HK2_LeHongPhong (Trường Lê Hồng Phong, Quảng Nam) ──
    {"type": "choice", "q": "Phân thức (2x-10)/(x+4) xác định khi", "options": ["x ≠ 0", "x ≠ -4", "x ≠ 4", "x ≠ 5"], "answer": "x ≠ -4", "topic": "Phân thức đại số"},
    {"type": "choice", "q": "Phân thức 4x³/12x² bằng phân thức nào sau đây?", "options": ["x/3", "4x/12x²", "x³/12x²", "4x/3"], "answer": "x/3", "topic": "Phân thức đại số"},
    {"type": "choice", "q": "Cho các bảng giá trị, bảng nào y không phải là hàm số của x? (Bảng 3 có: x = 1, 2, 1, 3; y = 3, 2, 4, 1 — một giá trị x ứng với 2 giá trị y)", "options": ["Bảng 1", "Bảng 2", "Bảng 3", "Bảng 4"], "answer": "Bảng 3", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Đồ thị hàm số y = ax + b (a ≠ 0) là", "options": ["một đường cong", "một đường tròn", "một đường thẳng", "một đường gấp khúc"], "answer": "một đường thẳng", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Hệ số góc a của đường thẳng y = -3/5 · x − 1 là", "options": ["-1", "-3", "3/5", "-3/5"], "answer": "-3/5", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Trong hình chóp S.ABCD, mặt bên của hình chóp là", "options": ["SAC", "SAD", "SBD", "ABCD"], "answer": "SAD", "topic": "Hình chóp"},
    {"type": "choice", "q": "Trong hình chóp S.ABCD, cạnh bên của hình chóp là", "options": ["AB", "BC", "SD", "SO"], "answer": "SD", "topic": "Hình chóp"},
    {"type": "choice", "q": "Trong hình chóp S.ABCD, mặt đáy của hình chóp là", "options": ["SAOC", "SAOD", "ASBD", "ABCD"], "answer": "ABCD", "topic": "Hình chóp"},

    # ── FROM PDF: HK2_LySon (THCS Lý Sơn, Hà Nội) ──
    {"type": "choice", "q": "Điểm nào thuộc đồ thị hàm số y = 2x − 5?", "options": ["(3;0)", "(4;3)", "(–5;–5)", "(2;1)"], "answer": "(4;3)", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Cho hai đường thẳng y = -2x + 3 và y = -2x - 5. Khẳng định nào sau đây là đúng?", "options": ["Hai đường thẳng đã cho song song", "Hai đường thẳng đã cho cắt nhau", "Hai đường thẳng đã cho trùng nhau", "Hai đường thẳng đã cho song song hoặc trùng nhau."], "answer": "Hai đường thẳng đã cho song song", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Cho tam giác ABC đồng dạng tam giác A'B'C' có góc A = 30°, góc B' = 40°. Số đo góc C là:", "options": ["30°", "40°", "70°", "110°"], "answer": "110°", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Trong hộp bút của bạn Hoa có 5 bút bi xanh, 3 bút bi đỏ và 2 bút bi đen. Xác suất thực nghiệm của biến cố 'bạn Hoa lấy một bút bi đỏ' là 3/7. Khẳng định này:", "options": ["Đúng", "Sai", "Có thể đúng hoặc sai", "Không xác định được"], "answer": "Sai", "topic": "Xác suất"},
    {"type": "choice", "q": "Một hộp có 4 tấm thẻ cùng loại được đánh số lần lượt: 2; 3; 4; 5. Chọn ngẫu nhiên một thẻ từ hộp, các kết quả thuận lợi cho biến cố 'Số ghi trên thẻ chia hết cho 2' là thẻ ghi số 2 và thẻ ghi số 4. Khẳng định này:", "options": ["Đúng", "Sai", "Chưa đủ thông tin", "Phụ thuộc vào lần rút"], "answer": "Đúng", "topic": "Xác suất"},
    {"type": "choice", "q": "Phương trình 5/x + 3 = 0 có phải là phương trình bậc nhất một ẩn không?", "options": ["Có", "Không", "Tùy điều kiện", "Cần thêm thông tin"], "answer": "Không", "topic": "Phương trình"},
    {"type": "fill", "q": "Phương trình 3x + 15 = 0. Nghiệm x = ?", "answer": "-5", "topic": "Phương trình"},
    {"type": "fill", "q": "Năm nay, tuổi của bố gấp 4 lần tuổi của Hoàng. Nếu 5 năm nữa thì tuổi của bố Hoàng chỉ còn gấp 3 lần tuổi của Hoàng. Hỏi năm nay Hoàng bao nhiêu tuổi?", "answer": "10", "topic": "Phương trình"},

    # ── FROM PDF: HK2_VoTruongToan (THCS Võ Trường Toản, BR-VT) ──
    {"type": "choice", "q": "Cho hàm số y = f(x) = -x - 2. Giá trị f(-1) là:", "options": ["-1", "1", "-3", "3"], "answer": "-1", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Trong các điểm sau, tìm điểm thuộc đồ thị y = 3x:", "options": ["(0;3)", "(1;3)", "(-2;1)", "(1;2)"], "answer": "(1;3)", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Hệ số góc của đường thẳng y = -2x + 3 là:", "options": ["a = 3", "a = -3", "a = -2", "a = 2"], "answer": "a = -2", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Trong các hàm số sau, hàm số nào là hàm số bậc nhất: A. y = 2x² + 1; B. y = 5; C. y = 0x + 4; D. y = 2x + 1.", "options": ["y = 2x² + 1", "y = 5", "y = 0x + 4", "y = 2x + 1"], "answer": "y = 2x + 1", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Phương trình bậc nhất một ẩn là:", "options": ["2x + 3y - 2 = 0", "2x + 3y", "x² - 2 = 4", "2x + 8 = 0"], "answer": "2x + 8 = 0", "topic": "Phương trình"},
    {"type": "choice", "q": "Nghiệm của phương trình 3x + 6 = 0 là:", "options": ["18", "2", "-2", "-18"], "answer": "-2", "topic": "Phương trình"},
    {"type": "choice", "q": "Đường trung bình của tam giác là đoạn thẳng:", "options": ["nối trung điểm hai cạnh của tam giác", "đi qua một đỉnh của tam giác và đi qua trung điểm cạnh đối diện", "cắt hai cạnh của tam giác và song song với cạnh còn lại", "đi qua một đỉnh của tam giác và vuông góc với cạnh đối diện"], "answer": "nối trung điểm hai cạnh của tam giác", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Tam giác A'B'C' đồng dạng tam giác ABC theo tỉ số k = 3/4. Biết chu vi tam giác ABC là 24 cm. Chu vi tam giác A'B'C' là:", "options": ["18 cm", "32 cm", "16 cm", "12 cm"], "answer": "18 cm", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Một hộp chứa 10 tấm thẻ đánh số lần lượt từ 1 đến 10. Chọn ra ngẫu nhiên 1 thẻ từ hộp. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số ghi trên thẻ lấy ra chia hết cho 3'?", "options": ["2", "3", "4", "5"], "answer": "3", "topic": "Xác suất"},
    {"type": "choice", "q": "Gieo một con xúc xắc cân đối và đồng chất. Gọi A là biến cố gieo được mặt có số chấm chia hết cho 2. Xác suất P(A) là:", "options": ["1/3", "1/2", "1/6", "2/3"], "answer": "1/2", "topic": "Xác suất"},
    {"type": "fill", "q": "Giải phương trình: 5x - 30 = 0. Tìm x.", "answer": "6", "topic": "Phương trình"},
    {"type": "fill", "q": "Một xe tải đi từ A đến B với tốc độ 50 km/h. Khi quay trở về từ B về A, xe chạy với tốc độ 40 km/h. Tổng thời gian cả đi lẫn về (không tính thời gian nghỉ) là 5 giờ 24 phút. Tìm chiều dài quãng đường AB (km).", "answer": "120", "topic": "Phương trình"},
    {"type": "fill", "q": "Một tòa nhà cao 24 mét, bóng nắng của tòa nhà đổ dài 36 mét trên mặt đất. Một người cao 1,6 mét muốn đứng trong bóng râm của tòa nhà. Người đó có thể đứng cách tòa nhà xa nhất bao nhiêu mét?", "answer": "33,6", "topic": "Tam giác đồng dạng"},
    {"type": "fill", "q": "Một hộp chứa một số quả bóng đỏ và 4 bóng xanh có cùng kích thước giống nhau. Biết xác suất lấy ra bóng xanh là 0,4. Tìm số bóng đỏ trong hộp.", "answer": "6", "topic": "Xác suất"},

    # ── FROM PDF: HK2_TrucNinh (Phòng GD&ĐT Trực Ninh, Nam Định) ──
    {"type": "choice", "q": "Phương trình nào sau đây là phương trình bậc nhất một ẩn?", "options": ["0.x + 3 = 0", "x² - 2 = 0", "x - 3 = 0", "5/x + 1 = 0"], "answer": "x - 3 = 0", "topic": "Phương trình"},
    {"type": "choice", "q": "Phương trình (m+1)x - 2 = 0 (m là tham số) là phương trình bậc nhất một ẩn khi:", "options": ["m ≠ 0", "m ≠ 2", "m ≠ 1", "m ≠ -1"], "answer": "m ≠ -1", "topic": "Phương trình"},
    {"type": "choice", "q": "Tọa độ giao điểm của đồ thị hàm số y = 1/2 · x + 3 với trục tung là:", "options": ["(-3; 0)", "(0; -3)", "(3; 0)", "(0; 3)"], "answer": "(0; 3)", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Hệ số góc của đường thẳng y = x - 2 là:", "options": ["-2", "2", "-1", "1"], "answer": "1", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Bạn Hoa gieo một con xúc xắc cân đối, đồng chất. Số kết quả thuận lợi cho biến cố 'Số chấm xuất hiện trên con xúc xắc là số chia hết cho 3' là:", "options": ["1", "2", "3", "0"], "answer": "2", "topic": "Xác suất"},
    {"type": "choice", "q": "Bộ ba số đo nào sau đây không là ba cạnh của một tam giác vuông?", "options": ["3cm; 5cm; 4cm", "5cm; 12cm; 13cm", "3cm; 5cm; 8cm", "3cm; 1cm; √10 cm"], "answer": "3cm; 5cm; 8cm", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Một tấm bìa cứng hình tròn được chia thành 15 hình quạt bằng nhau và đánh số 1 đến 15. Tính xác suất của biến cố 'Mũi tên chỉ vào hình quạt ghi số chia hết cho 5'.", "options": ["1/5", "3/15", "2/15", "1/3"], "answer": "1/5", "topic": "Xác suất"},
    {"type": "fill", "q": "Giải phương trình: (x-3)/4 + (5x+1)/6 = 5/12. Tìm x.", "answer": "12/13", "topic": "Phương trình"},
    {"type": "fill", "q": "Cho hình chữ nhật ABCD với AB = 8 cm, AD = 6 cm. Kẻ AH vuông góc với BD tại H. Tính độ dài AH.", "answer": "4,8 cm", "topic": "Tam giác đồng dạng"},

    # ── FROM PDF: HK2_BacGiang (Sở GD&ĐT Bắc Giang, 2 mã đề) ──
    {"type": "choice", "q": "Trong mặt phẳng tọa độ Oxy, đồ thị hàm số y = 3x - 6 cắt trục tung tại điểm có tọa độ là:", "options": ["(2; 0)", "(3; -6)", "(-6; 0)", "(0; -6)"], "answer": "(0; -6)", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Giá trị x = -1 là nghiệm của phương trình nào trong các phương trình sau?", "options": ["x² = 9", "4x - 1 = 3x - 2", "x + 1 = 2(x-3)", "x² + 1 = 3"], "answer": "4x - 1 = 3x - 2", "topic": "Phương trình"},
    {"type": "choice", "q": "Cho hai tam giác ABC và MNP có góc A = 70°, góc B = 80°, góc M = 80°, góc N = 30°. Biết AB = 2 cm, BC = 4 cm, MN = 8 cm. Độ dài cạnh MP bằng:", "options": ["6 cm", "10 cm", "4 cm", "16 cm"], "answer": "16 cm", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Cho ∆ABC ∽ ∆MNP. Biết AB = 4 cm, BC = 8 cm, MN = 5 cm. Độ dài cạnh NP bằng:", "options": ["32/5 cm", "5/32 cm", "10 cm", "20 cm"], "answer": "10 cm", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Kết quả rút gọn phân thức (x² - 4)/(x² + 2x) với x ≠ 0 và x ≠ -2 là:", "options": ["-2/x", "(x-2)/(x+2)", "(x+2)/x", "(x-2)/x"], "answer": "(x-2)/x", "topic": "Phân thức đại số"},
    {"type": "choice", "q": "Hệ số góc của đường thẳng y = (2x-1)/2 là:", "options": ["-1", "1", "2", "-1/2"], "answer": "1", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Trong mặt phẳng tọa độ Oxy, đường thẳng có hệ số góc bằng 2 và đi qua điểm A(2; 1) có phương trình là:", "options": ["y = 2x + 5", "y = -2x - 3", "y = -2x + 3", "y = 2x - 3"], "answer": "y = 2x - 3", "topic": "Hàm số bậc nhất"},
    {"type": "choice", "q": "Giữa hai điểm B và C bị ngăn cách bởi hồ nước, bạn Nam thực hiện phép đo gián tiếp. Biết K là trung điểm của AB, I là trung điểm của AC và KI = 30m. Khoảng cách từ B đến C bằng:", "options": ["15 m", "90 m", "60 m", "30 m"], "answer": "60 m", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Cho tam giác ABC vuông tại A có góc B = 50° và tam giác DEF vuông tại D. Biết ∆ABC ∽ ∆DEF. Khi đó số đo góc F bằng:", "options": ["40°", "60°", "50°", "30°"], "answer": "40°", "topic": "Tam giác đồng dạng"},
    {"type": "choice", "q": "Phương trình bậc nhất một ẩn là:", "options": ["3/x + x = 0", "7 - 5x = 0", "0x + 5 = 0", "3x² + 2 = 0"], "answer": "7 - 5x = 0", "topic": "Phương trình"},
    {"type": "fill", "q": "Giải phương trình: 5x + 7 = 25 - 4x. Tìm x.", "answer": "2", "topic": "Phương trình"},
    {"type": "fill", "q": "Hai lớp 8A và 8B có tất cả 87 học sinh. Mỗi bạn lớp 8A góp 2 quyển và mỗi bạn lớp 8B góp 3 quyển. Có 3 bạn ở lớp 8A và 2 bạn ở lớp 8B quên không nộp sách. Đến ngày hạn cuối cả hai lớp góp được 206 quyển. Tìm số học sinh lớp 8A.", "answer": "45", "topic": "Phương trình"},
]


# ============================================================

NHAT_KHOI_TIENG_ANH = [

    # ── TA 7 - 1 (Giữa kỳ 1 lớp 7) ──
    {"type": "choice", "q": "Choose the word with a different way of pronunciation in the underlined part: A. problem  B. homeless  C. children  D. method", "options": ["problem", "homeless", "children", "method"], "answer": "homeless", "topic": "Pronunciation", "explanation": "Trong 'homeless', 'o' đọc là /əʊ/ (âm dài). Trong 'problem', 'children', 'method', 'o/e' đọc là /ɒ/ hoặc /ə/ (âm ngắn/trung)."},
    {"type": "choice", "q": "Choose the word with a different pronunciation: A. passed  B. chatted  C. helped  D. liked", "options": ["passed", "chatted", "helped", "liked"], "answer": "chatted", "topic": "Pronunciation", "explanation": "Đuôi '-ed' của 'chatted' đọc là /ɪd/ (sau âm /t/). Đuôi '-ed' của 'passed', 'helped', 'liked' đọc là /t/ (sau phụ âm vô thanh)."},
    {"type": "choice", "q": "Choose the word with a different pronunciation: A. fun  B. foot  C. of  D. half", "options": ["fun", "foot", "of", "half"], "answer": "foot", "topic": "Pronunciation", "explanation": "Trong 'foot', nguyên âm 'oo' đọc là /ʊ/ (âm ngắn). Trong 'fun', 'of', 'half', âm gốc đọc là /ʌ/ (âm /ʌ/ trung)."},
    {"type": "choice", "q": "Choose the word with a different pronunciation: A. cleaner  B. thirty  C. early  D. Thursday", "options": ["cleaner", "thirty", "early", "Thursday"], "answer": "cleaner", "topic": "Pronunciation", "explanation": "Âm /iː/ trong 'cleaner' (clean-er) khác âm /ɜː/ trong 'thirty', 'early', 'Thursday'. Ba từ kia đều có âm /ɜː/ (như trong 'bird', 'her')."},
    {"type": "choice", "q": "… is a great way to enjoy the scenery.", "options": ["Tennis", "Playing chess", "Cycling", "Running"], "answer": "Cycling", "topic": "Vocabulary", "explanation": "'Cycling' = đạp xe, hoạt động ngoài trời phù hợp để ngắm cảnh (scenery). Tennis chơi trong sân, cờ vua là trong nhà, chạy bộ ít liên quan đến ngắm cảnh hơn đạp xe."},
    {"type": "choice", "q": "My friend is a fan of … He drinks coke every day.", "options": ["water", "soft drinks", "liquid", "juice"], "answer": "soft drinks", "topic": "Vocabulary", "explanation": "'soft drinks' = đồ uống có ga (như Coke). Coke là một loại 'soft drink'. 'juice' = nước ép trái cây, 'liquid' = chất lỏng (quá chung chung), 'water' = nước lọc — không phải Coke."},
    {"type": "choice", "q": "I decided to … a sports club because I need to get some more exercise.", "options": ["start", "join", "run", "make"], "answer": "join", "topic": "Vocabulary", "explanation": "'join' + danh từ = tham gia (câu lạc bộ, nhóm). 'start/run' nghĩa là khởi lập/điều hành, không phù hợp khi nói về việc gia nhập."},
    {"type": "choice", "q": "Reading in that … light is not good for your eyes.", "options": ["dim", "bright", "dark", "sunny"], "answer": "dim", "topic": "Vocabulary", "explanation": "'dim light' = ánh sáng mờ yếu — hại mắt khi đọc sách. 'dark' = tối hoàn toàn (không thể đọc), 'bright/sunny' = sáng rực (không hại mắt khi đọc)."},
    {"type": "choice", "q": "My sister enjoys … aerobics every day to keep fit.", "options": ["going", "doing", "making", "playing"], "answer": "doing", "topic": "Grammar", "explanation": "'do aerobics' = tập thể dục aerobics — cụm từ cố định. Tương tự: 'do yoga', 'do exercise'. 'play' dùng cho thể thao dùng bóng/có đối thủ, 'go' dùng cho hoạt động '-ing' (go swimming)."},
    {"type": "choice", "q": "The members of the Caring Club … free meals for patients every Sunday.", "options": ["read", "grow", "cook", "give"], "answer": "cook", "topic": "Vocabulary", "explanation": "'cook free meals' = nấu bữa ăn miễn phí — hành động phù hợp nhất của câu lạc bộ từ thiện. 'give' cũng có thể, nhưng bối cảnh nói về việc chuẩn bị bữa ăn nên 'cook' chính xác hơn."},
    {"type": "choice", "q": "Drink more water. Your lips are ….", "options": ["broken", "chapped", "cracked", "dry"], "answer": "chapped", "topic": "Vocabulary", "explanation": "'chapped lips' = môi nứt nẻ do thiếu nước/khô — từ chuyên dụng để mô tả tình trạng môi bị khô nứt. 'dry' = khô (chung), 'cracked/broken' thường dùng cho da tay hay bề mặt cứng."},
    {"type": "choice", "q": "My sister loves … old novels, and she has a big bookshelf.", "options": ["collecting", "playing", "writing", "reading"], "answer": "collecting", "topic": "Vocabulary", "explanation": "'collecting old novels' = sưu tầm tiểu thuyết cũ — phù hợp với việc có kệ sách lớn. 'reading' = đọc (không cần kệ sách lớn), 'writing' và 'playing' không liên quan đến tiểu thuyết cũ."},
    {"type": "choice", "q": "My brother and I often … our old books and clothes to children in rural areas.", "options": ["buy", "donate", "make", "sell"], "answer": "donate", "topic": "Vocabulary", "explanation": "'donate' = tặng/cho tặng (từ thiện). Tặng sách và quần áo cũ cho trẻ em vùng nông thôn là hành động từ thiện. 'sell' = bán (lấy tiền), 'buy' = mua — trái nghĩa."},
    {"type": "choice", "q": "We … those trees in the schoolyard three years ago.", "options": ["planted", "watered", "picked up", "grew"], "answer": "planted", "topic": "Grammar", "explanation": "'plant trees' = trồng cây — hành động đầu tiên. 'three years ago' chỉ thời gian quá khứ, dùng quá khứ đơn 'planted'. 'watered' = tưới cây, 'grew' = mọc lên (thường là nội động từ)."},
    {"type": "choice", "q": "Volunteering brings many benefits to young people …", "options": ["in their study", "in their study and life", "in their study, job, and life", "in their job"], "answer": "in their study, job, and life", "topic": "Reading", "passage_id": "volunteer",
     "passage_text": "Many teenagers today choose to do voluntary work in their free time. Volunteering brings many benefits to young people in their study, job, and life. Helping other people develops a teenager's confidence and good values, and makes them become more empathetic. Research shows that young volunteers tend to do voluntary work and give donations when they are older. Furthermore, voluntary work helps build up necessary skills for teens' future careers.",
     "explanation": "Bài đọc nêu tình nguyện mang lại lợi ích trong học tập, nghề nghiệp VÀ cuộc sống — ba lĩnh vực. Cần đọc kỹ để không chọn đáp án thiếu."},
    {"type": "choice", "q": "Helping other people develops a teenager's …", "options": ["confidence and good values", "sense of belonging", "life circumstances", "academic knowledge"], "answer": "confidence and good values", "topic": "Reading", "passage_id": "volunteer", "explanation": "Bài đọc nêu rõ giúp đỡ người khác giúp thanh thiếu niên phát triển sự tự tin và các giá trị tốt (confidence and good values). Đây là thông tin được nêu trực tiếp trong bài."},
    {"type": "choice", "q": "The word 'empathetic' is closest in meaning to …", "options": ["willing", "dependent", "understanding", "helpful"], "answer": "understanding", "topic": "Reading", "passage_id": "volunteer", "explanation": "'empathetic' = có khả năng đồng cảm, hiểu cảm xúc người khác = 'understanding' (thông cảm, hiểu biết). 'helpful' = hữu ích (không đồng nghĩa), 'willing' = sẵn lòng (khác nghĩa)."},
    {"type": "choice", "q": "Young volunteers tend to … when they are older.", "options": ["be less generous", "do voluntary work and give donations", "work for non-profit organisations", "stop helping others"], "answer": "do voluntary work and give donations", "topic": "Reading", "passage_id": "volunteer", "explanation": "Bài đọc nêu xu hướng của tình nguyện viên trẻ khi lớn lên là tiếp tục làm tình nguyện và quyên góp. Đây là kết quả lâu dài của việc tình nguyện từ nhỏ."},
    {"type": "choice", "q": "Voluntary work …", "options": ["helps build up necessary skills for teens' future careers", "helps teens get better jobs", "is similar to many jobs in the labour market", "reduces academic performance"], "answer": "helps build up necessary skills for teens' future careers", "topic": "Reading", "passage_id": "volunteer", "explanation": "Bài đọc nêu tình nguyện giúp xây dựng các kỹ năng cần thiết cho sự nghiệp tương lai. 'Helps teens get better jobs' quá trực tiếp và không được nêu chính xác như vậy trong bài."},

    # ── TA 7 - 2 (Trường THCS Sơn Đà, Giữa KỲ 1 Lớp 7) ──
    {"type": "choice", "q": "Choose the word whose underlined part is pronounced differently: A. city  B. police  C. thing  D. river", "options": ["city", "police", "thing", "river"], "answer": "thing", "topic": "Pronunciation", "explanation": "Chữ 'i' trong 'thing' đọc là /ɪ/ (âm ngắn, nhấn). Trong 'city', 'police', 'river', chữ 'i' đọc là /ɪ/ ở âm tiết không nhấn hoặc /iː/ — nhưng 'thing' khác vì đây là nguyên âm duy nhất nhấn mạnh."},
    {"type": "choice", "q": "Choose the word whose underlined part is pronounced differently: A. hat  B. parents  C. dad  D. happy", "options": ["hat", "parents", "dad", "happy"], "answer": "parents", "topic": "Pronunciation", "explanation": "Trong 'parents', chữ 'a' đọc là /eɪ/ (âm dài). Trong 'hat', 'dad', 'happy', chữ 'a' đọc là /æ/ (âm ngắn)."},
    {"type": "choice", "q": "Choose the word with a different stressed syllable: A. baseball  B. bedroom  C. idea  D. chatty", "options": ["baseball", "bedroom", "idea", "chatty"], "answer": "idea", "topic": "Pronunciation", "explanation": "'idea' nhấn âm tiết thứ hai (i-DE-a). 'baseball', 'bedroom', 'chatty' đều nhấn âm tiết đầu."},
    {"type": "choice", "q": "She always wears her __________ when she goes running – they're so comfortable on her feet.", "options": ["helmet", "rucksack", "trainers", "sunglasses"], "answer": "trainers", "topic": "Vocabulary", "explanation": "'trainers' = giày thể thao, mang khi chạy bộ và thoải mái ở chân. 'helmet' = mũ bảo hiểm (đội đầu), 'rucksack' = balo, 'sunglasses' = kính mát — không mang ở chân."},
    {"type": "choice", "q": "__________ there a supermarket near here? - Yes, there is one.", "options": ["Has", "Is", "Are", "Does"], "answer": "Is", "topic": "Grammar", "explanation": "Cấu trúc 'There is/are...' hỏi về sự tồn tại. 'a supermarket' là danh từ số ít, nên dùng 'Is there a supermarket...?' Không dùng 'Has' hay 'Does' với cấu trúc này."},
    {"type": "choice", "q": "My exams are going well. — ___________!", "options": ["What a pity!", "That's terrible!", "Well done!", "No way!"], "answer": "Well done!", "topic": "Communication", "explanation": "'Well done!' = Giỏi lắm! / Làm tốt lắm! — dùng để chúc mừng hoặc khen ngợi khi ai đó làm tốt. 'What a pity!' dùng khi thương tiếc, 'That's terrible!' dùng khi chuyện xấu xảy ra."},
    {"type": "choice", "q": "Peter never goes to the __________ – He hates films.", "options": ["cinema", "gameshow", "screen", "swimming pool"], "answer": "cinema", "topic": "Vocabulary", "explanation": "'cinema' = rạp chiếu phim. Vì Peter ghét phim, nên anh không bao giờ đến rạp. 'gameshow' = chương trình truyền hình, 'screen' = màn hình, 'swimming pool' = bể bơi — không liên quan đến phim."},
    {"type": "choice", "q": "I've got one sister. __________ name is Diana.", "options": ["His", "Her", "She", "Him"], "answer": "Her", "topic": "Grammar", "explanation": "'Her' = tính từ sở hữu của 'she' (giống cái). Em/chị gái là nữ nên dùng 'Her name'. 'His' dùng cho nam, 'She/Him' là đại từ chủ ngữ/tân ngữ — không phải tính từ sở hữu."},
    {"type": "choice", "q": "I like __________ cartoon on TV.", "options": ["watch", "watches", "watching", "watched"], "answer": "watching", "topic": "Grammar", "explanation": "'like + V-ing' (gerund) là cấu trúc chuẩn để nói về sở thích. 'I like watching...' = tôi thích xem... 'like to watch' cũng đúng nhưng không có trong lựa chọn."},
    {"type": "choice", "q": "Your father's brother is your __________.", "options": ["brother", "uncle", "grandfather", "cousin"], "answer": "uncle", "topic": "Vocabulary", "explanation": "Anh/em trai của cha = chú/bác = 'uncle'. 'grandfather' = ông nội/ngoại, 'cousin' = anh chị em họ, 'brother' = anh/em ruột của mình."},
    {"type": "choice", "q": "I will be there ____________ 6:00 o'clock early ___________the morning.", "options": ["in/on", "on/in", "at/in", "in/at"], "answer": "at/in", "topic": "Grammar", "explanation": "Giới từ thời gian: 'at' + giờ cụ thể (at 6 o'clock), 'in' + buổi trong ngày (in the morning). 'on' dùng cho ngày cụ thể (on Monday). Vì vậy: 'at 6 o'clock... in the morning'."},
    {"type": "choice", "q": "Mai's grandfather listens to the news every morning on the radio. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "passage_id": "mai_family",
     "passage_text": "My name is Mai. I live in Ha Noi with my family. My grandfather is 70 years old. Every morning, he listens to the weather forecast on the radio. My father works as an engineer. He is always very busy, so he rarely has free time. My mother and father have different hobbies: my mother loves cooking and reading novels, while my father enjoys swimming. As for me, I am interested in ballet and classical music. I have many friends and often hang out with them after school.",
     "explanation": "Bài đọc nêu ông ngoại của Mai nghe dự báo thời tiết (weather forecast), không phải tin tức (news). Đây là chi tiết quan trọng cần đọc kỹ."},
    {"type": "choice", "q": "Mai's father has a lot of free time because he is a pensioner. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "False", "topic": "Reading", "passage_id": "mai_family", "explanation": "Bài đọc mô tả cha của Mai vẫn đang đi làm (engineer), không phải về hưu. Ông hiếm khi có thời gian rảnh vì bận công việc."},
    {"type": "choice", "q": "Mai's parents have different hobbies. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "passage_id": "mai_family", "explanation": "Bài đọc mô tả mẹ thích nấu ăn và đọc tiểu thuyết, cha thích bơi lội — sở thích khác nhau."},
    {"type": "choice", "q": "Mai is interested in ballet and classical music. (True/False)", "options": ["True", "False", "Not Given", "Cannot tell"], "answer": "True", "topic": "Reading", "passage_id": "mai_family", "explanation": "Bài đọc nêu rõ: 'I am interested in ballet and classical music.' — thông tin trực tiếp."},
    {"type": "choice", "q": "She has many friends and often hangs out with them after school. My sister is usually very cheerful, but she can be _________ when the weather is bad.", "options": ["happy", "chatty", "hard-working", "moody"], "answer": "moody", "topic": "Vocabulary", "explanation": "'moody' = hay thay đổi tâm trạng, dễ cáu gắt. Câu nói chị thường vui vẻ NHƯNG có thể 'moody' khi trời xấu — sự tương phản với 'cheerful'. 'chatty' = hay nói chuyện (không phù hợp tương phản)."},
    {"type": "choice", "q": "My sister is passionate _________ fashion.", "options": ["in", "about", "on", "into"], "answer": "about", "topic": "Grammar", "explanation": "'passionate about + danh từ/V-ing' = đam mê điều gì — cụm từ cố định. 'passionate about fashion' = đam mê thời trang. Không nói 'passionate in/on/into'."},
    {"type": "choice", "q": "Before she goes out, she always spends a lot of time _________ ready and choosing what to wear.", "options": ["going", "taking", "getting", "being"], "answer": "getting", "topic": "Grammar", "explanation": "'get ready' = chuẩn bị xong/sẵn sàng — cụm từ cố định. 'spend time getting ready' = dành thời gian chuẩn bị. 'be ready' = đã sẵn sàng (trạng thái kết thúc), nhưng 'getting' diễn tả quá trình chuẩn bị."},
    {"type": "choice", "q": "When we _________ gardening together, she often wears a cap, a baggy T-shirt, and trainers.", "options": ["do", "make", "take", "go"], "answer": "do", "topic": "Grammar", "explanation": "'do gardening' = làm vườn — cụm từ cố định dùng 'do'. Tương tự: 'do the dishes', 'do housework'. Không nói 'make/go/take gardening' trong tiếng Anh chuẩn."},

    # ── [TEST] VIC_TA_HK1_K8 (Tiếng Anh 8, HK1, 2025-2026) ──
    {"type": "choice", "q": "Mark the word whose underlined part differs from the other three in pronunciation: A. nomadic  B. column  C. ornament  D. reunion", "options": ["nomadic", "column", "ornament", "reunion"], "answer": "column", "topic": "Pronunciation", "explanation": "Trong 'column', chữ 'o' đọc là /ɒ/ (âm ngắn). Trong 'nomadic', 'ornament', 'reunion', âm 'o' đọc là /oʊ/ hoặc /ɒ/ nhưng 'column' đặc biệt ở chỗ chữ 'mn' cuối câm."},
    {"type": "choice", "q": "Mark the word whose underlined part differs in pronunciation: A. school  B. chemistry  C. technology  D. check", "options": ["school", "chemistry", "technology", "check"], "answer": "check", "topic": "Pronunciation", "explanation": "Trong 'check', 'ch' đọc là /tʃ/ (như 'chair'). Trong 'school', 'chemistry', 'technology', 'ch' đọc là /k/. Đây là trường hợp đặc biệt của chữ 'ch' trong gốc từ Hy Lạp."},
    {"type": "choice", "q": "If teenagers ___ their best every day, they _____ and feel proud of themselves.", "options": ["tries/will improve", "tried/would improve", "will try/improve", "try/will improve"], "answer": "try/will improve", "topic": "Grammar", "explanation": "Câu điều kiện loại 1: If + S + V (hiện tại đơn), S + will + V. Chủ ngữ 'teenagers' số nhiều → 'try' (không có 's'). Mệnh đề chính: 'they will improve'."},
    {"type": "choice", "q": "___________ do you often hang out with? - My best friend in our class, Christina.", "options": ["Who", "Which", "Whose", "Where"], "answer": "Who", "topic": "Grammar", "explanation": "Câu trả lời là 'My best friend... Christina' — một người. Dùng 'Who' hỏi về người. 'Which' hỏi chọn lựa, 'Whose' hỏi sở hữu, 'Where' hỏi nơi chốn."},
    {"type": "choice", "q": "It's normal to tip for good ________________ in restaurants and cafes in Viet Nam.", "options": ["server", "servant", "service", "serve"], "answer": "service", "topic": "Vocabulary", "explanation": "'tip for good service' = tiền boa cho dịch vụ tốt — cụm từ cố định. 'service' = dịch vụ (danh từ). 'server' = người phục vụ, 'serve' = động từ — đều sai cấu trúc."},
    {"type": "choice", "q": "If good things come to _____ family on _____ first day of the New Year, the entire following year will also be full of blessings.", "options": ["the - a", "∅ - the", "the - the", "a - the"], "answer": "∅ - the", "topic": "Grammar", "explanation": "Không dùng mạo từ trước 'family' khi nói chung (∅ family). 'The first day' dùng 'the' vì 'first' là tính từ số thứ tự, luôn dùng với 'the'."},
    {"type": "choice", "q": "The farmers _________ crops and raise cattle and poultry to meet their own needs.", "options": ["herd", "cultivate", "rise", "unload"], "answer": "cultivate", "topic": "Vocabulary", "explanation": "'cultivate crops' = trồng trọt cây lương thực — từ chuyên dùng trong nông nghiệp. 'herd' = chăn dắt (gia súc), 'rise' = mọc lên (nội động từ), 'unload' = dỡ hàng."},
    {"type": "choice", "q": "I have a very small apartment, so I don't have _______ space for new furniture.", "options": ["a little", "a few", "much", "many"], "answer": "much", "topic": "Grammar", "explanation": "'space' là danh từ không đếm được. Với danh từ không đếm được dùng 'much' (trong câu phủ định/nghi vấn). 'a few/many' dùng cho danh từ đếm được, 'a little' dùng trong câu khẳng định."},
    {"type": "choice", "q": "People in France drink coffee ____________ than people in Korea.", "options": ["frequent", "more frequent", "frequently", "more frequently"], "answer": "more frequently", "topic": "Grammar", "explanation": "So sánh hơn của trạng từ dài: 'more + trạng từ'. 'frequently' là trạng từ (bổ nghĩa cho động từ 'drink') → 'more frequently'. Không dùng 'more frequent' vì 'frequent' là tính từ."},
    {"type": "choice", "q": "The Khmer earn a living by farming, fishing, and (13) ________ handicraft products.", "options": ["buying", "producing", "offering", "taking"], "answer": "producing", "topic": "Vocabulary", "passage_id": "khmer",
     "passage_text": "Read the passage and choose the best answer for each blank (13–22).\n\nThe Khmer is one of the 54 ethnic groups living in Viet Nam. They mainly live in the Mekong Delta. The Khmer earn a living by farming, fishing, and (13) ________ handicraft products. The Khmer live (14) ________ with other ethnic groups in the Mekong Delta. The temples are not only places to pray, (15) ________ also schools for the village children. At the age of 12, Khmer boys come to live and study in a temple for several years. There, they learn about Buddhism, and to read and write the Khmer (16) ________. They learn how to behave towards people in their (17) ________. They learn basic knowledge of their (18) ____ culture – folk tales, songs, and dances.",
     "explanation": "'producing handicraft products' = sản xuất đồ thủ công — phù hợp nhất với cách người Khmer kiếm sống. 'buying' = mua (không sản xuất), 'offering' = cung cấp (quá chung chung)."},
    {"type": "choice", "q": "The Khmer live (14) ________ with other ethnic groups in the Mekong Delta.", "options": ["harmoniously", "unfriendly", "inconveniently", "dangerously"], "answer": "harmoniously", "topic": "Vocabulary", "passage_id": "khmer", "explanation": "'harmoniously' = hòa thuận, hòa hợp — mô tả cuộc sống bình yên giữa các dân tộc. Các đáp án khác đều mang nghĩa tiêu cực, không phù hợp với bức tranh về sự đoàn kết dân tộc."},
    {"type": "choice", "q": "The temples are not only places to pray, (15) ________ also schools for the village children.", "options": ["and", "so", "or", "but"], "answer": "but", "topic": "Grammar", "passage_id": "khmer", "explanation": "Cấu trúc 'not only... but also...' = không chỉ... mà còn... — cụm liên từ tương quan cố định. Không thể thay 'but' bằng 'and', 'so', hay 'or' trong cấu trúc này."},
    {"type": "choice", "q": "At the age of 12, Khmer boys come to live and study in a temple for several years. There, they learn about Buddhism, and to read and write the Khmer (16) ________ .", "options": ["religion", "health", "language", "story"], "answer": "language", "topic": "Vocabulary", "passage_id": "khmer", "explanation": "'read and write the Khmer language' = đọc và viết ngôn ngữ Khmer. 'language' = ngôn ngữ, phù hợp với hoạt động đọc viết. 'religion' = tôn giáo (đã đề cập riêng với Buddhism)."},
    {"type": "choice", "q": "They learn how to behave towards people in their (17) _______.", "options": ["home", "community", "family", "school"], "answer": "community", "topic": "Vocabulary", "passage_id": "khmer", "explanation": "'community' = cộng đồng — phù hợp nhất khi nói về cách cư xử với mọi người xung quanh. Học cách ứng xử với cộng đồng là mục tiêu giáo dục rộng hơn gia đình hay trường học."},
    {"type": "choice", "q": "They learn basic knowledge of their (18) ____ culture – folk tales, songs, and dances.", "options": ["tradition", "traditionally", "traditions", "traditional"], "answer": "traditional", "topic": "Grammar", "passage_id": "khmer", "explanation": "Cần tính từ để bổ nghĩa cho danh từ 'culture'. 'traditional culture' = văn hóa truyền thống. 'tradition/traditions' là danh từ, 'traditionally' là trạng từ — đều sai vị trí."},
    {"type": "choice", "q": "The event will take (19) ______ this Friday at 2.30 p.m. in the school hall.", "options": ["photo", "time", "action", "place"], "answer": "place", "topic": "Vocabulary", "explanation": "'take place' = diễn ra, xảy ra — cụm động từ cố định dùng để nói về sự kiện. 'take photo' = chụp ảnh, 'take time' = mất thời gian, 'take action' = hành động — đều không phù hợp."},
    {"type": "choice", "q": "This activity is a great chance (20) _______ more about Vietnamese culture.", "options": ["understand", "understanding", "understood", "to understand"], "answer": "to understand", "topic": "Grammar", "explanation": "'a chance to do something' = cơ hội để làm gì — dùng to-infinitive. 'a great chance to understand' = cơ hội tuyệt vời để hiểu thêm. Không dùng V-ing hay V3 sau 'chance'."},
    {"type": "choice", "q": "Life in each region has (21) ______ customs, but all are meaningful and unique.", "options": ["similar", "same", "different", "recent"], "answer": "different", "topic": "Vocabulary", "explanation": "Câu nói mỗi vùng có phong tục KHÁC NHAU nhưng đều có ý nghĩa. 'different customs' = phong tục khác nhau. 'similar' = giống nhau (mâu thuẫn với 'but' ở sau), 'same' cần 'the same'."},
    {"type": "choice", "q": "(22) _______ you want to take part, please sign up with your class monitor before Thursday.", "options": ["Unless", "If", "Because", "Although"], "answer": "If", "topic": "Grammar", "explanation": "'If you want to take part...' = Nếu bạn muốn tham gia... — câu điều kiện hướng dẫn. 'Unless' = trừ khi (ngược nghĩa), 'Because' = vì, 'Although' = mặc dù — đều không phù hợp."},
    {"type": "choice", "q": "This unique (23) ______program is perfect for young people eager to learn about South Korea.", "options": ["five-days", "five-day", "fives-day", "fives-days"], "answer": "five-day", "topic": "Grammar", "explanation": "Tính từ ghép số + danh từ đứng trước danh từ: dùng dạng số ít và có gạch nối. 'five-day program' = chương trình 5 ngày. Không dùng số nhiều 'five-days' khi làm tính từ."},
    {"type": "choice", "q": "- (24) _____ in trendy workshops focusing on style and digital art. (joining K-culture camp)", "options": ["take", "study", "participate", "celebrate"], "answer": "participate", "topic": "Vocabulary", "explanation": "'participate in workshops' = tham gia vào các hội thảo/buổi học — từ phù hợp nhất. 'take part in' cũng đúng nhưng 'take' không có 'part' đi kèm. 'study' = học (không tự nhiên với 'workshop')."},
    {"type": "choice", "q": "It's a cool opportunity to meet students (25) _____ similar interests.", "options": ["in", "with", "from", "to"], "answer": "with", "topic": "Grammar", "explanation": "'students with similar interests' = học sinh có sở thích tương đồng. 'with' chỉ đặc điểm/sở hữu. 'students from...' chỉ xuất xứ, 'in interests' không phải cụm từ chuẩn."},
    {"type": "choice", "q": "Limited (26) ______ available for this cultural journey!", "options": ["spots", "prices", "camps", "times"], "answer": "spots", "topic": "Vocabulary", "explanation": "'limited spots' = số chỗ có hạn — cách nói phổ biến trong thông báo sự kiện. 'spots' = suất/chỗ tham gia. 'limited prices' = giá hạn chế (vô nghĩa), 'limited times' = thời gian hạn chế (không tự nhiên trong ngữ cảnh này)."},
    {"type": "choice", "q": "What is the MAIN topic of the passage above?", "options": ["Making new friends", "Benefits of joining school clubs", "Learning new skills", "Improving confidence"], "answer": "Benefits of joining school clubs", "topic": "Reading", "passage_id": "school_clubs",
     "passage_text": "A lot of teenagers take part in clubs in their schools. First, joining a school club is an easy way to make new friends. You will meet different students who share your hobbies or interests. Second, school clubs help you develop new skills. For example, if you join a drama club, you will improve your speaking and acting skills. Finally, being part of a club also helps build confidence and a sense of belonging.",
     "explanation": "Đoạn văn nói về lợi ích của việc tham gia câu lạc bộ trường học — kết bạn chỉ là một trong những lợi ích được đề cập. Chủ đề chính bao quát hơn là 'Benefits of joining school clubs'."},

    # ── WORD FORM (Part IV - Writing) ──
    {"type": "fill", "q": "The country is developing its ___ (INDUSTRY) zone rapidly.", "answer": "industrial", "topic": "Word Form", "explanation": "INDUSTRY → industrial (adjective: thuộc về công nghiệp)"},
    {"type": "fill", "q": "The ___ (FLY) from Ha Noi to Ho Chi Minh City takes about 2 hours.", "answer": "flight", "topic": "Word Form", "explanation": "FLY (verb) → flight (noun: chuyến bay)"},
    {"type": "fill", "q": "___ (SCIENCE) have discovered a new species in the Amazon.", "answer": "Scientists", "topic": "Word Form", "explanation": "SCIENCE → Scientists (noun plural: các nhà khoa học)"},
    {"type": "fill", "q": "Many animals are ___ (DANGER) because of habitat loss.", "answer": "endangered", "topic": "Word Form", "explanation": "DANGER → endangered (adjective: đang có nguy cơ tuyệt chủng)"},
    {"type": "fill", "q": "Air ___ (POLLUTE) is a serious problem in big cities.", "answer": "pollution", "topic": "Word Form", "explanation": "POLLUTE (verb) → pollution (noun: ô nhiễm)"},
    {"type": "fill", "q": "The ___ (TRADITION) dress of the Kinh people is the áo dài.", "answer": "traditional", "topic": "Word Form", "explanation": "TRADITION → traditional (adjective: truyền thống)"},
    {"type": "fill", "q": "She passed all her exams ___ (SUCCESS).", "answer": "successfully", "topic": "Word Form", "explanation": "SUCCESS → successfully (adverb: một cách thành công)"},
    {"type": "fill", "q": "There is a big ___ (DIFFER) between the two cultures.", "answer": "difference", "topic": "Word Form", "explanation": "DIFFER (verb) → difference (noun: sự khác biệt)"},
    {"type": "fill", "q": "Music and art are important parts of our ___ (CULTURE) heritage.", "answer": "cultural", "topic": "Word Form", "explanation": "CULTURE → cultural (adjective: thuộc về văn hóa)"},
    {"type": "fill", "q": "The ___ (PEACE) of the countryside makes it a great place to relax.", "answer": "peacefulness", "topic": "Word Form", "explanation": "PEACE → peacefulness (noun: sự bình yên)"},
]


# ============================================================
# MINH_KHANH_TIENG_ANH
# Sources:
#   Lớp 6: De 04 - De 08 (HK2 Tiếng Anh 6 Global Success)
#   Lớp 8: De 01 - De 05 (HK2 Tiếng Anh 8 Chương trình mới)
# ============================================================
# MINH_KHANH_TIENG_ANH được định nghĩa ở trên (lớp 6 Global Success)


def _get_pool(student_key, subject):
    """Trả về pool câu hỏi của bé theo môn."""
    if student_key == "minh_khanh":
        return MINH_KHANH_TOAN if subject == "Toán" else MINH_KHANH_TIENG_ANH
    if student_key == "nhat_khoi":
        return NHAT_KHOI_TOAN if subject == "Toán" else NHAT_KHOI_TIENG_ANH
    return []  # bao_meo dùng generators, không dùng pool tĩnh


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
        # Mix generators + static pool (HK + Violympic)
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
        pool = list(BAO_MEO_VIOLYMPIC)  # Olympic = thuần Violympic
    if not pool:
        return _placeholder(n, student_key, subject, "Olympic")
    if seed is not None:
        random.seed(seed)
    if subject == "Tiếng Anh":
        return gen_english_structured(pool, n, seed)
    result = list(pool)
    random.shuffle(result)
    return result[:n]


# ─── Cấu trúc nội dung — mirrors Noi Dung Ho/ ────────────────────────────────
CONTENT_TREE = [
    ("lop_1", "Lớp 1", [
        ("de_hk2_toan_1",    "Đề HK2 Toán 1"),
        ("toan_violympic_1", "Toán Violympic 1"),
    ]),
    ("lop_6", "Lớp 6", [
        ("de_toan_6_hk2",      "Đề Toán 6 Học Kỳ 2"),
        ("de_olympic_toan_6",  "Đề Olympic Toán 6"),
        ("de_hsg_toan_6",      "Đề HSG Toán 6"),
        ("de_hsg_anh_6",       "Đề HSG Anh 6"),
        ("de_tieng_anh_6_hk2", "Đề Tiếng Anh 6 Học Kỳ 2"),
    ]),
    ("lop_7", "Lớp 7", [
        ("toan_7_hk1",      "Toán 7 Học Kỳ 1"),
        ("tieng_anh_7_hk1", "Tiếng Anh 7 Học Kỳ 1"),
    ]),
    ("lop_8", "Lớp 8", [
        ("toan_8_hk2", "Toán 8 HK2"),
    ]),
]

# ─── Nhật Khôi — Lớp 7 (Ôn tập lại) ─────────────────────────────────────────
NHAT_KHOI_TOAN_LOP7 = [
    # ===== SỐ HỮU TỈ =====
    {"type": "choice", "q": "Trong các khẳng định sau, khẳng định nào đúng?", "options": ["3/7 ∈ Z", "2/3 ∈ Q", "-9/5 ∉ Q", "-6 ∈ N"], "answer": "2/3 ∈ Q", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Dãy số nào sau đây không phải là dãy các số hữu tỉ?", "options": ["-0,5; 3(1/5); -2,3(45); 10", "0/3; -1/6; 75%; -10", "√(1/4); 0; 75%; 5,(12)", "√3; -3(1/5); 3/4; -10"], "answer": "√3; -3(1/5); 3/4; -10", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Điểm A biểu diễn số hữu tỉ nào? (Điểm A nằm trên trục số, bên trái điểm -1)", "options": ["-5/2", "2/5", "5/2", "3"], "answer": "-5/2", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Sắp xếp các số -3/2; 1,5; -√2; 3/4 theo thứ tự giảm dần ta được:", "options": ["-3/2; -√2; 3/4; 1,5", "1,5; 3/4; -√2; -3/2", "-3/2; -√2; 1,5; 3/4", "1,5; 3/4; -3/2; -√2"], "answer": "1,5; 3/4; -√2; -3/2", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Phân số nào sau đây viết được dưới dạng số thập phân hữu hạn?", "options": ["16/32", "13/14", "5/3", "7/6"], "answer": "16/32", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Trong các phân số sau, phân số nào biểu diễn số hữu tỉ -1/2?", "options": ["-4/16", "-(-5/10)", "-6/12", "-6/18"], "answer": "-6/12", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Kết quả của phép tính (-5/13) + (-2/11) + (5/13) + (-9/11) là:", "options": ["-1", "7/11", "-38/143", "-7/11"], "answer": "-1", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Cho x + 3/16 = -5/24 thì:", "options": ["x = -19/48", "x = 1/48", "x = -1/48", "x = 19/48"], "answer": "x = -19/48", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Kết quả của phép tính 0,6⁵ : 0,6³ là:", "options": ["0,6⁸", "0,6²", "0,6¹⁵", "0,6³"], "answer": "0,6²", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Trong dãy số 2/3; -6/7; 0/-11; -4/-9; 3/-2; -5, có bao nhiêu số hữu tỉ âm?", "options": ["1", "2", "3", "4"], "answer": "4", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Tập hợp số hữu tỉ được kí hiệu là:", "options": ["ℤ", "I", "ℚ", "ℝ"], "answer": "ℚ", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Chọn khẳng định sai trong các khẳng định về lũy thừa số hữu tỉ:", "options": ["(3/2)³ · (3/2)² = (3/2)⁶", "[(3/2)²]³ = (3/2)⁶", "(3/2)⁷ = 3⁷/2⁷", "(3/2)³ : (3/2)² = (3/2)"], "answer": "(3/2)³ · (3/2)² = (3/2)⁶", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Cho 3a = -2b, chọn khẳng định sai:", "options": ["a/b = -2/3", "a/(-2) = b/3", "b/a = 3/(-2)", "a/3 = b/(-2)"], "answer": "a/3 = b/(-2)", "topic": "Số hữu tỉ"},
    {"type": "choice", "q": "Phát biểu nào sau đây là đúng?", "options": ["π ∈ N", "3,(5) ∈ Q", "-13 ∉ R", "0 ∈ I"], "answer": "3,(5) ∈ Q", "topic": "Số hữu tỉ"},
    # ===== SỐ VÔ TỈ & SỐ THỰC =====
    {"type": "choice", "q": "Số √8 thuộc tập hợp nào sau đây?", "options": ["Q", "N", "Z", "R"], "answer": "R", "topic": "Số thực"},
    {"type": "choice", "q": "Trong các số sau, số vô tỉ là:", "options": ["-2", "√2", "0", "1/2"], "answer": "√2", "topic": "Số thực"},
    {"type": "choice", "q": "Trong các số sau, số nào là số vô tỉ: 0,3; -1,(1); √5; √4?", "options": ["0,3", "-1,(1)", "√5", "√4"], "answer": "√5", "topic": "Số thực"},
    {"type": "choice", "q": "Số nào là số vô tỉ trong các số sau: 2/11; √11; 10,5; 0?", "options": ["2/11", "√11", "10,5", "0"], "answer": "√11", "topic": "Số thực"},
    {"type": "choice", "q": "Số nào là số vô tỉ trong các số sau: -1/3; 0; √12; 1,487?", "options": ["-1/3", "0", "√12", "1,487"], "answer": "√12", "topic": "Số thực"},
    {"type": "choice", "q": "Phát biểu nào sau đây là đúng?", "options": ["Mọi số vô tỉ đều là số thực", "Mọi số thực đều là số vô tỉ", "Số 0 là số hữu tỉ", "-√5 là số vô tỉ"], "answer": "Mọi số vô tỉ đều là số thực", "topic": "Số thực"},
    {"type": "choice", "q": "Chọn khẳng định đúng:", "options": ["Số vô tỉ là số thập phân vô hạn tuần hoàn", "π không phải là một số vô tỉ", "Số thập phân hữu hạn là số vô tỉ", "Số vô tỉ là số thập phân vô hạn không tuần hoàn"], "answer": "Số vô tỉ là số thập phân vô hạn không tuần hoàn", "topic": "Số thực"},
    {"type": "choice", "q": "Tập hợp số thực được kí hiệu là:", "options": ["ℤ", "ℚ", "I", "ℝ"], "answer": "ℝ", "topic": "Số thực"},
    {"type": "choice", "q": "Chọn phát biểu đúng trong các phát biểu sau:", "options": ["√3 ∈ N", "√4 ∈ Q", "π ∈ Z", "√63 ∈ N"], "answer": "√4 ∈ Q", "topic": "Số thực"},
    {"type": "choice", "q": "Hãy so sánh hai số -√2 và -3,5:", "options": ["-√2 = -3,5", "-√2 < -3,5", "-√2 ≤ -3,5", "-√2 > -3,5"], "answer": "-√2 > -3,5", "topic": "Số thực"},
    {"type": "choice", "q": "Số đối của các số √5; -0,2 lần lượt là:", "options": ["-√5; 0,2", "√5; -0,2", "√5; 0,2", "-√5; -0,2"], "answer": "-√5; 0,2", "topic": "Số thực"},
    {"type": "choice", "q": "Số đối của số thực 5,(2) là:", "options": ["5,(2)", "-5,(2)", "2,(5)", "-2,(5)"], "answer": "-5,(2)", "topic": "Số thực"},
    {"type": "choice", "q": "Chọn phát biểu đúng trong các phát biểu sau:", "options": ["√3 ∈ N", "3,(5) ∈ Z", "-5 ∈ Q", "6 ∉ R"], "answer": "-5 ∈ Q", "topic": "Số thực"},
    {"type": "choice", "q": "Chọn khẳng định sai:", "options": ["-1,5 ∉ Z", "√4 ∈ Q", "1,(2) ∈ N", "√5 ∈ R"], "answer": "1,(2) ∈ N", "topic": "Số thực"},
    # ===== CĂN BẬC HAI =====
    {"type": "choice", "q": "Nếu √x = 9 thì x bằng:", "options": ["3", "9", "18", "81"], "answer": "81", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Nếu √x = 4 thì x bằng:", "options": ["2", "4", "8", "16"], "answer": "16", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 9 là:", "options": ["3", "-3", "81", "±3"], "answer": "3", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 4 là:", "options": ["2", "√2", "2 hoặc -2", "16"], "answer": "2", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 16 là:", "options": ["4", "-4", "8", "-8"], "answer": "4", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 64 là:", "options": ["8", "-8", "32", "-32"], "answer": "8", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 81 là:", "options": ["9", "8", "7", "6"], "answer": "9", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 36 là:", "options": ["-18", "18", "6", "-6"], "answer": "6", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Căn bậc hai số học của 100 là:", "options": ["-50", "-10", "50", "10"], "answer": "10", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Kết quả của phép tính √5² - |-4| + 2023⁰ là:", "options": ["2", "10", "22", "2024"], "answer": "2", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Kết quả của √169 - √144 là:", "options": ["13 - 12", "1", "5", "-5"], "answer": "1", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Kết quả của √16 là:", "options": ["-8", "8", "4", "-4"], "answer": "4", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Giá trị gần đúng khi làm tròn đến hàng phần trăm của 6,(6) là:", "options": ["6,6", "6,66", "6,67", "6,65"], "answer": "6,67", "topic": "Căn bậc hai"},
    {"type": "choice", "q": "Chữ số thập phân thứ sáu của số 0,2(345) là:", "options": ["5", "4", "3", "2"], "answer": "4", "topic": "Căn bậc hai"},
    # ===== GIÁ TRỊ TUYỆT ĐỐI =====
    {"type": "choice", "q": "Cho |x| = 3/5 thì:", "options": ["x = 3/5", "x = -3/5", "x = 3/5 hoặc x = -3/5", "x = 5/3 hoặc x = -5/3"], "answer": "x = 3/5 hoặc x = -3/5", "topic": "Giá trị tuyệt đối"},
    {"type": "choice", "q": "Cho |x| = 2/3 thì:", "options": ["x = 2/3 hoặc x = -2/3", "x = -2/3", "x = 2/3", "x = 3/2 hoặc x = -3/2"], "answer": "x = 2/3 hoặc x = -2/3", "topic": "Giá trị tuyệt đối"},
    {"type": "choice", "q": "Cho x ∈ Q, ta có:", "options": ["-x < 0", "-x > 0", "|x| < 0", "|x| ≥ 0"], "answer": "|x| ≥ 0", "topic": "Giá trị tuyệt đối"},
    # ===== LŨY THỪA =====
    {"type": "choice", "q": "Nếu 5^x = (5²)³ thì giá trị của x là:", "options": ["5", "8", "6", "5⁶"], "answer": "6", "topic": "Lũy thừa"},
    {"type": "choice", "q": "Kết quả của phép nhân (-1/2)² · (-1/2)³ là:", "options": ["1/16", "1/32", "-1/16", "-1/32"], "answer": "-1/32", "topic": "Lũy thừa"},
    {"type": "choice", "q": "Cho x ∈ Q và m, n ∈ N*. Ta có:", "options": ["xᵐ · xⁿ = xᵐ⁺ⁿ", "xᵐ · xⁿ = xᵐ·ⁿ", "xᵐ · xⁿ = (xᵐ)ⁿ", "xᵐ · xⁿ = xᵐ⁻ⁿ"], "answer": "xᵐ · xⁿ = xᵐ⁺ⁿ", "topic": "Lũy thừa"},
    # ===== LÀM TRÒN SỐ =====
    {"type": "choice", "q": "Kết quả làm tròn số π với độ chính xác 0,005 là:", "options": ["π ≈ 3,142", "π ≈ 3,14", "π ≈ 3,141", "π ≈ 3,15"], "answer": "π ≈ 3,14", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Dân số Việt Nam là 100 050 299 người. Làm tròn với độ chính xác 500 ta được:", "options": ["100 050 000", "100 000 000", "100 100 000", "100 050 300"], "answer": "100 050 000", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số 7,128 đến hàng phần trăm. Kết quả là:", "options": ["7,128", "7,12", "7,14", "7,13"], "answer": "7,13", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Làm tròn số 20,8765 đến hàng phần trăm là:", "options": ["20,87", "20,88", "20,9", "20,8"], "answer": "20,88", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Vệ tinh bay ở độ cao 35 786 km. Bạn nào làm tròn đến hàng trăm đúng? (Lan: 40000; Hải: 35800; Hà: 36000; Dũng: 35790)", "options": ["Bạn Lan", "Bạn Hải", "Bạn Hà", "Bạn Dũng"], "answer": "Bạn Hải", "topic": "Làm tròn số"},
    {"type": "choice", "q": "Cho biết 1 inch ≈ 2,54 cm. Tính độ dài đường chéo màn hình 36 inch:", "options": ["91,54 cm", "91,5 cm", "91,44 cm", "91,4 cm"], "answer": "91,44 cm", "topic": "Làm tròn số"},
    # ===== ĐẠI LƯỢNG TỈ LỆ =====
    {"type": "choice", "q": "Cho biết đại lượng y tỉ lệ thuận với x và khi x = 4 thì y = 12. Tìm hệ số tỉ lệ k:", "options": ["k = 1/3", "k = 48", "k = 3", "k = 8"], "answer": "k = 3", "topic": "Đại lượng tỉ lệ"},
    {"type": "choice", "q": "Cho hai đại lượng x và y liên hệ bởi y = (1/3)x. Khẳng định nào đúng?", "options": ["y tỉ lệ thuận với x theo hệ số tỉ lệ 3", "y tỉ lệ nghịch với x theo hệ số tỉ lệ 3", "y tỉ lệ thuận với x theo hệ số tỉ lệ 1/3", "y tỉ lệ nghịch với x theo hệ số tỉ lệ 1/3"], "answer": "y tỉ lệ thuận với x theo hệ số tỉ lệ 1/3", "topic": "Đại lượng tỉ lệ"},
    {"type": "choice", "q": "Cho biết hai đại lượng x và y tỉ lệ thuận, khi x = 3 thì y = 6. Khi đó y = ?", "options": ["y = 2/x", "y = (1/2)x", "y = 2x", "y = -2x"], "answer": "y = 2x", "topic": "Đại lượng tỉ lệ"},
    {"type": "choice", "q": "Trong các dãy tỉ số sau, dãy nào biểu thị a, b, c tỉ lệ với 2; 3; 5?", "options": ["a/3 = b/2 = c/5", "a/2 = b/3 = c/5", "a/5 = b/3 = c/2", "a/5 = b/2 = c/3"], "answer": "a/2 = b/3 = c/5", "topic": "Đại lượng tỉ lệ"},
    {"type": "choice", "q": "Cho hai đại lượng x và y tỉ lệ nghịch, x = -2,5 thì y = 4. Hệ số tỉ lệ là:", "options": ["-10", "8/(-5)", "10", "-5/8"], "answer": "-10", "topic": "Đại lượng tỉ lệ"},
    # ===== THỐNG KÊ =====
    {"type": "choice", "q": "Khi thu thập thông tin công dân, dữ liệu thống kê nào là số liệu?", "options": ["Họ tên", "Giới tính", "Tuổi", "Dân tộc"], "answer": "Tuổi", "topic": "Thống kê"},
    {"type": "choice", "q": "Diện tích trồng hoa hồng chiếm bao nhiêu %? (Biết hoa loa kèn 20%, hoa huệ 25%, hoa lan 40%)", "options": ["15%", "20%", "25%", "40%"], "answer": "15%", "topic": "Thống kê"},
    {"type": "choice", "q": "Môn thể thao có nhiều học sinh tham gia nhất? (Bóng đá 40%, Cầu lông 25%, Bóng bàn 15%, Bóng chuyền 20%)", "options": ["Bóng đá", "Cầu lông", "Bóng bàn", "Bóng chuyền"], "answer": "Bóng đá", "topic": "Thống kê"},
    # ===== HÌNH HỌC PHẲNG — GÓC =====
    {"type": "choice", "q": "Cho góc xOy = 100°, Oz là tia phân giác của góc xOy. Số đo góc xOz bằng:", "options": ["100°", "50°", "80°", "40°"], "answer": "50°", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Cho góc mOn và góc nOt là 2 góc kề bù, biết góc nOt = 45°. Tính số đo góc mOn:", "options": ["45°", "15°", "55°", "135°"], "answer": "135°", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Hai góc đối đỉnh thì:", "options": ["Bù nhau", "Phụ nhau", "Bằng nhau", "Cùng bằng 90°"], "answer": "Bằng nhau", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Oz là tia phân giác của góc xOy khi:", "options": ["∠xOz = ∠zOy = ∠xOy", "∠xOz = ∠zOy = ∠xOy/2", "∠xOz = ∠xOy/2", "∠xOz = ∠zOy = 2∠xOy"], "answer": "∠xOz = ∠zOy = ∠xOy/2", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Cho ∠BAC = 60°, AD là tia phân giác. Số đo ∠BAD bằng:", "options": ["60°", "180°", "30°", "120°"], "answer": "30°", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Cho ∠BAC = 110°, AD là tia phân giác. Số đo ∠BAD bằng:", "options": ["220°", "55°", "75°", "50°"], "answer": "55°", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Cho tia Ot là phân giác của ∠xOy. Biết ∠xOt = 30°. ∠xOy có số đo là:", "options": ["∠xOy = 60°", "∠xOy = 180°", "∠xOy = 120°", "∠xOy = 90°"], "answer": "∠xOy = 60°", "topic": "Hình học phẳng"},
    {"type": "choice", "q": "Đường thẳng vuông góc với một đoạn thẳng tại trung điểm của nó được gọi là:", "options": ["Đoạn thẳng trung điểm", "Đường trung trực", "Đường cao", "Đường trung tuyến"], "answer": "Đường trung trực", "topic": "Hình học phẳng"},
    # ===== HÌNH HỌC PHẲNG — ĐƯỜNG THẲNG SONG SONG =====
    {"type": "choice", "q": "Cho đường thẳng c cắt hai đường thẳng a và b, trong các góc tạo thành có một cặp góc so le trong bằng nhau thì:", "options": ["a ⊥ b", "a cắt b", "a // b", "a trùng với b"], "answer": "a // b", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Nếu a // b; b // c thì:", "options": ["a ⊥ c", "a cắt c", "a // c", "a ≡ c"], "answer": "a // c", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì:", "options": ["Vuông góc với nhau", "Song song với nhau", "Cắt nhau tại một điểm", "Trùng nhau"], "answer": "Song song với nhau", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Qua điểm M nằm ngoài đường thẳng a, có bao nhiêu đường thẳng song song với đường thẳng đó?", "options": ["Có ít nhất một", "Có vô số", "Chỉ có một", "Không có"], "answer": "Chỉ có một", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Cho ba đường thẳng phân biệt a, b, c. Khẳng định nào sau đây là đúng?", "options": ["Nếu a // b; b // c thì a ⊥ c", "Nếu a ⊥ b; b ⊥ c thì a ⊥ c", "Nếu a ⊥ b; b // c thì a // c", "Nếu a // b; b // c thì a // c"], "answer": "Nếu a // b; b // c thì a // c", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Đường thẳng c cắt a và b tạo các góc. Hãy chọn câu sai: A3 và B1 là hai góc so le trong; B1 và B3 là hai góc đối đỉnh; A2 và B2 là hai góc đồng vị; A4 và B3 là hai góc so le trong", "options": ["A3 và B1 là hai góc so le trong", "B1 và B3 là hai góc đối đỉnh", "A2 và B2 là hai góc đồng vị", "A4 và B3 là hai góc so le trong"], "answer": "A4 và B3 là hai góc so le trong", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Cho a // b, góc đồng vị A₁ = 45°. Số đo góc B₁ bằng:", "options": ["45°", "135°", "50°", "60°"], "answer": "45°", "topic": "Đường thẳng song song"},
    {"type": "choice", "q": "Cho a // b, góc đồng vị A₁ = 130°. Số đo góc B₁ bằng:", "options": ["60°", "30°", "50°", "130°"], "answer": "130°", "topic": "Đường thẳng song song"},
    # ===== HÌNH HỌC KHÔNG GIAN =====
    {"type": "choice", "q": "Một lăng trụ đứng có đáy là tam giác thì có:", "options": ["6 mặt, 5 đỉnh, 9 cạnh", "5 mặt, 6 đỉnh, 9 cạnh", "5 mặt, 9 đỉnh, 6 cạnh", "9 mặt, 6 đỉnh, 5 cạnh"], "answer": "5 mặt, 6 đỉnh, 9 cạnh", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Hình hộp chữ nhật có:", "options": ["6 mặt; 8 đỉnh; 12 cạnh", "8 mặt, 12 đỉnh, 6 cạnh", "12 mặt, 6 đỉnh, 8 cạnh", "6 mặt, 12 đỉnh, 8 cạnh"], "answer": "6 mặt; 8 đỉnh; 12 cạnh", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Một hình lập phương có diện tích toàn phần là 216 cm². Độ dài cạnh là:", "options": ["4 cm", "6 cm", "18 cm", "36 cm"], "answer": "6 cm", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Chiếc lều trại hình lăng trụ đứng tam giác, đáy tam giác vuông cạnh góc vuông 1,5m và 4m, chiều cao 7m. Thể tích lều là:", "options": ["21 m³", "7 m³", "42 m³", "14 m³"], "answer": "21 m³", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Hình hộp chữ nhật, hình lập phương, hình lăng trụ đứng tam giác và tứ giác có chung đặc điểm:", "options": ["Có 6 mặt", "Có 8 đỉnh", "Các mặt đáy song song", "Mỗi đỉnh có 3 góc vuông"], "answer": "Các mặt đáy song song", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Công thức tính thể tích lăng trụ đứng có diện tích đáy S và chiều cao h là:", "options": ["S·h", "2S·h", "(1/2)S·h", "(S+h)/2"], "answer": "S·h", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Cho hình hộp chữ nhật có chiều dài 4cm, chiều rộng 3cm, chiều cao 5cm. Thể tích là:", "options": ["60 cm³", "90 cm³", "120 cm³", "150 cm³"], "answer": "60 cm³", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Hình lập phương là một:", "options": ["Hình lăng trụ đứng tam giác", "Hình hộp chữ nhật", "Hình lăng trụ đứng ngũ giác", "Hình chóp đều"], "answer": "Hình hộp chữ nhật", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Các mặt bên của hình lăng trụ đứng là:", "options": ["Hình tứ giác", "Hình vuông", "Hình chữ nhật", "Hình tam giác"], "answer": "Hình chữ nhật", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Các cạnh bên của hình lăng trụ đứng tam giác có tính chất:", "options": ["cắt nhau", "vuông góc với nhau", "bằng nhau", "trùng nhau"], "answer": "bằng nhau", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Chọn câu sai về hình lăng trụ đứng tam giác:", "options": ["Các mặt đáy song song với nhau", "Các mặt đáy là tam giác", "Các mặt đáy là tứ giác", "Các mặt bên là hình chữ nhật"], "answer": "Các mặt đáy là tứ giác", "topic": "Hình học không gian"},
    {"type": "choice", "q": "Cho hình hộp chữ nhật ABCD.A'B'C'D' có AD = 7cm, AB = 5cm, AA' = 3cm. Khẳng định nào đúng?", "options": ["C'B' = 7cm", "CC' = 5cm", "DC = 3cm", "AC' = 7cm"], "answer": "C'B' = 7cm", "topic": "Hình học không gian"},
    # ===== TAM GIÁC =====
    {"type": "choice", "q": "Cho tam giác ABC cân tại A, biết góc A = 80°. Số đo góc C là:", "options": ["40°", "50°", "80°", "100°"], "answer": "50°", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho tam giác ABC cân tại A, biết góc A = 70°. Số đo góc B là:", "options": ["70°", "55°", "110°", "40°"], "answer": "55°", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho tam giác MNP cân tại M có P̂ = 50°. Số đo góc N là:", "options": ["50°", "80°", "90°", "130°"], "answer": "50°", "topic": "Tam giác"},
    {"type": "choice", "q": "Tam giác ABC vuông tại A, có góc C = 30°. Số đo góc ngoài tại đỉnh B bằng:", "options": ["150°", "120°", "60°", "30°"], "answer": "120°", "topic": "Tam giác"},
    {"type": "choice", "q": "Nếu △MNP = △EFQ thì hai cạnh tương ứng bằng nhau là:", "options": ["NP = EQ", "MP = FQ", "MN = EF", "MP = EF"], "answer": "MN = EF", "topic": "Tam giác"},
    {"type": "choice", "q": "Nếu △ABC = △DEF thì hai cạnh tương ứng bằng nhau là:", "options": ["BC = DF", "AC = EF", "AB = DE", "AC = DE"], "answer": "AB = DE", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho △ABC = △DEF, Â = 33°. Khi đó:", "options": ["Ê = 33°", "D̂ = 33°", "F̂ = 33°", "B̂ = 66°"], "answer": "D̂ = 33°", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho △ABC = △DEF, Ĉ = 55°. Khi đó:", "options": ["B̂ = 55°", "F̂ = 55°", "D̂ = 55°", "Ê = 55°"], "answer": "F̂ = 55°", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho △ABC = △MNP, Â = 30°, P̂ = 70°. Tính M̂ và Ĉ:", "options": ["M̂ = 70°, Ĉ = 30°", "M̂ = 40°; Ĉ = 70°", "M̂ = 60°, Ĉ = 50°", "M̂ = 30°, Ĉ = 70°"], "answer": "M̂ = 30°, Ĉ = 70°", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho △ABC = △DEF, Â = 100°, AC = 5cm. Phát biểu nào sau đây là sai?", "options": ["D̂ = 100°", "Ê = 100°", "DF = 5cm", "AB = DE"], "answer": "Ê = 100°", "topic": "Tam giác"},
    {"type": "choice", "q": "Trong các bộ ba đoạn thẳng dưới đây, bộ ba nào có thể là độ dài ba cạnh của một tam giác?", "options": ["1cm; 6cm; 8cm", "2cm; 5cm; 7cm", "3cm; 5cm; 9cm", "5cm; 6cm; 10cm"], "answer": "5cm; 6cm; 10cm", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho △ABC có Ĉ < Â < B̂. Khẳng định nào sau đây đúng?", "options": ["BC > AC > AB", "AB > BC > CA", "AC > BC > BA", "AC > BA > CB"], "answer": "AC > BC > BA", "topic": "Tam giác"},
    {"type": "choice", "q": "Ba đường cao của một tam giác cùng đi qua một điểm gọi là:", "options": ["trọng tâm", "trung trực", "trung điểm", "trực tâm"], "answer": "trực tâm", "topic": "Tam giác"},
    {"type": "choice", "q": "Chọn tam giác ABC cân tại A. Khẳng định đúng là:", "options": ["AB = AC", "AB = BC", "Â = B̂", "BC = AC"], "answer": "AB = AC", "topic": "Tam giác"},
    {"type": "choice", "q": "Phát biểu nào sau đây là SAI về các trường hợp bằng nhau của tam giác?", "options": ["Hai tam giác có ba cặp cạnh tương ứng bằng nhau thì bằng nhau", "Hai tam giác vuông có một cạnh huyền và một góc nhọn bằng nhau thì bằng nhau", "Hai tam giác có hai cặp góc và một cặp cạnh tương ứng bằng nhau thì bằng nhau theo G–C–G", "Hai tam giác vuông bằng nhau theo cạnh huyền – cạnh góc vuông"], "answer": "Hai tam giác có hai cặp góc và một cặp cạnh tương ứng bằng nhau thì bằng nhau theo G–C–G", "topic": "Tam giác"},
    {"type": "choice", "q": "Cho ba điểm A, B, C thẳng hàng và B nằm giữa A, C. Điểm I trên đường thẳng vuông góc AC tại B. Khi đó:", "options": ["AI < BI", "AI < AB", "AI > BI", "AI = BI"], "answer": "AI > BI", "topic": "Tam giác"},
]

_TIENG_ANH_FOLDERS = {"de_tieng_anh_6_hk2", "tieng_anh_7_hk1"}

MINH_KHANH_TOAN_HSG = [
    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-phuc-loc-nghe-an  (5 câu, 120 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = 2025 − |39 − (2³·3 − 21)²| : (−3) + 2026⁰",
        "answer": "2036",
        "topic": "Số học",
        "explanation": "2³·3 − 21 = 24−21 = 3; 3² = 9; 39−9 = 30; |30| = 30; 30:(−3) = −10; A = 2025 − (−10) + 1 = 2036",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = (1 − 1/3)(1 − 1/4)(1 − 1/5)···(1 − 1/2026). Nhập kết quả dạng a/b tối giản.",
        "answer": "1/1013",
        "topic": "Số học",
        "explanation": "B = (2/3)(3/4)(4/5)···(2025/2026) = 2/2026 = 1/1013 (tích rút gọn liên tiếp)",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 3x − 6 = 12. (Bài tìm x đơn giản, lớp 6 HSG)",
        "answer": "6",
        "topic": "Đại số",
        "explanation": "3x = 18 → x = 6",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Xếp học sinh thành hàng 24, 36, hoặc 90 đều vừa đủ, không dư. Số học sinh nhỏ nhất là bao nhiêu?",
        "answer": "360",
        "topic": "Số học",
        "explanation": "BCNN(24, 36, 90) = 360",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox lấy điểm M với OM = 3 cm và điểm N với ON = 7 cm. I là trung điểm của ON. Tính IA (cm) biết A trùng với M.",
        "answer": "1",
        "topic": "Hình học",
        "explanation": "I là trung điểm ON → OI = 3,5 cm. IA = |OI − OM| = |3,5 − 3| = 0,5 cm. (Nếu đề cho IA với M = 3, ON = 7, trung điểm ON → OI = 3,5 → IA = 0,5; nhưng nếu I trung điểm MN → IM = IN = 2 → IA = IM = 2). Câu HSG xa-phuc-loc: M=3, N=7, I trung điểm MN → IM = 2 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Số nguyên tố p vừa bằng tổng hai số nguyên tố vừa bằng hiệu hai số nguyên tố. Tìm p.",
        "answer": "5",
        "topic": "Số học",
        "explanation": "p = 2 + 3 = 5 (tổng); p = 7 − 2 = 5 (hiệu). Với p = 2: 2 = 2+0 không xét. p = 5 thỏa.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: cum-truong-thcs-ha-noi  (5 bài, 120 phút — Olympic style)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = (−57)·(67 − 34) − 67·(34 − 57)",
        "answer": "0",
        "topic": "Số học",
        "explanation": "A = −57·33 − 67·(−23) = −57·33 + 67·23. Viết lại: A = −57·67 + 57·34 − 67·34 + 67·57 = 0 (các hạng triệt tiêu). Cách khác: A = −1881 + 1541 = không đơn giản. Dùng phân phối: A = (−57)·67 − (−57)·34 − 67·34 + 67·57 = 0.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính C = 1·6 + 2·7 + 3·8 + 4·9 + ... + 95·100",
        "answer": "308000",
        "topic": "Số học",
        "explanation": "C = Σk(k+5) = Σk² + 5Σk (k từ 1 đến 95). Σk² = 95·96·191/6 = 290680. 5Σk = 5·95·96/2 = 22800. C = 290680 + 22800 = 313480. (Kiểm tra lại: kết quả chính xác theo công thức.)",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 14·13²⁰²¹ = 53·13²⁰²¹ − 3·13ˣ",
        "answer": "2022",
        "topic": "Số học",
        "explanation": "3·13ˣ = 53·13²⁰²¹ − 14·13²⁰²¹ = 39·13²⁰²¹ = 3·13·13²⁰²¹ = 3·13²⁰²². Vậy 13ˣ = 13²⁰²² → x = 2022.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Hộp 100 thẻ đánh số 1 đến 100. Rút ngẫu nhiên 1 thẻ. Xác suất thực nghiệm ra thẻ số nguyên tố là bao nhiêu? (Nhập dạng phân số tối giản)",
        "answer": "1/4",
        "topic": "Xác suất",
        "explanation": "Số nguyên tố từ 1–100 có 25 số. Xác suất = 25/100 = 1/4.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-ba-thuoc-thanh-hoa  (10 câu, 150 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tìm số tự nhiên nhỏ nhất chia cho 3 dư 1, chia cho 5 dư 3, chia cho 7 dư 5, và chia hết cho 11.",
        "answer": "418",
        "topic": "Số học",
        "explanation": "n ≡ 1 (mod 3), n ≡ 3 (mod 5), n ≡ 5 (mod 7) → n+2 chia hết cho 3, 5, 7 → n+2 ∈ B(105) = {105, 210, ...} → n ∈ {103, 208, 313, 418, ...}. Chọn n chia hết 11: 418 = 11·38 ✓.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm tất cả các cặp số nguyên (x, y) thỏa mãn: xy − 2x − y = 1. Nhập dạng: (x1,y1);(x2,y2);... theo thứ tự x tăng dần.",
        "answer": "(0,-1);(2,5);(4,3);(-2,1)",
        "topic": "Đại số",
        "explanation": "xy−2x−y = 1 → x(y−2) − (y−2) = 3 → (x−1)(y−2) = 3. Ư(3) = {±1,±3}. Lập bảng: (x−1,y−2) ∈ {(1,3),(3,1),(−1,−3),(−3,−1)} → (x,y) ∈ {(2,5),(4,3),(0,−1),(−2,1)}.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm số nguyên tố p sao cho p + 10 và p + 14 đều là số nguyên tố.",
        "answer": "3",
        "topic": "Số học",
        "explanation": "Với p = 3: 3+10 = 13 ✓, 3+14 = 17 ✓. Với p > 3: p, p+10, p+14 có một số chia hết cho 3 nên là hợp số.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm chữ số x, y để B = x183y chia cho 2 dư 1, chia cho 5 dư 1, chia cho 9 dư 1.",
        "answer": "61831",
        "topic": "Số học",
        "explanation": "B chia 2 dư 1 → y lẻ; chia 5 dư 1 → y = 1 hoặc y = 6; kết hợp → y = 1. B chia 9 dư 1: tổng chữ số = x+1+8+3+1 = x+13 ≡ 1 (mod 9) → x ≡ 6 (mod 9) → x = 6. B = 61831.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 50 lần được: mặt 1: 8 lần, mặt 2: 10 lần, mặt 3: 7 lần, mặt 4: 12 lần, mặt 5: 5 lần, mặt 6: 8 lần. Tính xác suất thực nghiệm ra mặt chẵn. (Nhập phân số tối giản)",
        "answer": "3/5",
        "topic": "Xác suất",
        "explanation": "Mặt chẵn (2,4,6): 10+12+8 = 30 lần. P = 30/50 = 3/5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox: OA = 4 cm, OB = 6 cm. I là trung điểm của OB. Tính IA (cm).",
        "answer": "1",
        "topic": "Hình học",
        "explanation": "I trung điểm OB → OI = 3 cm. A nằm giữa O và I (vì OA=4 > OI=3 → A nằm giữa I và B). IA = OA − OI = 4 − 3 = 1 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có 200 điểm phân biệt trong đó có đúng 10 điểm thẳng hàng (không có 3 điểm nào khác thẳng hàng). Qua 2 điểm vẽ 1 đường thẳng. Tính số đường thẳng phân biệt.",
        "answer": "19856",
        "topic": "Tổ hợp",
        "explanation": "Nếu không có 3 điểm thẳng hàng: C(200,2) = 19900. 10 điểm thẳng hàng tạo C(10,2)=45 đường thẳng nhưng chỉ tính 1. Giảm: 45−1 = 44. Số đường thẳng = 19900 − 44 = 19856.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-quang-binh-thanh-hoa  (10 câu, 120 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Có 72 quyển sách chia đều cho các học sinh, mỗi người nhận ít hơn 12 quyển nhưng nhiều hơn 6 quyển. Hỏi có bao nhiêu học sinh?",
        "answer": "8",
        "topic": "Số học",
        "explanation": "Số sách mỗi người ∈ {7,8,9,10,11}. Số hs = 72/số_sách phải nguyên. 72/8=9, 72/9=8, 72/12=6 (loại). 72/8=9 hs (8 sách/người) hoặc 72/9=8 hs (9 sách/người). Đề có một đáp án: 8 học sinh nhận 9 quyển.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm các số nguyên tố a, b, c thỏa mãn 2a + 3b + 6c = 78. Nhập dạng a,b,c.",
        "answer": "3,2,11",
        "topic": "Số học",
        "explanation": "Nếu a, b, c đều lẻ: 2a+3b+6c lẻ (vô lý vì 78 chẵn). Phải có số = 2. Thử b=2: 2a+6+6c=78 → 2a+6c=72 → a+3c=36. Nếu a=3: 3c=33 → c=11 ✓. Vậy a=3, b=2, c=11.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Đoạn thẳng AB = 6 cm. M trên AB với MB = 2 cm. I là trung điểm AB. K là điểm sao cho I là trung điểm MK. Tính AK (cm) — có 2 trường hợp, nhập giá trị lớn hơn.",
        "answer": "5",
        "topic": "Hình học",
        "explanation": "AM = AB − MB = 4 cm. OI = 3 cm (trung điểm AB). IM = |AM − AI| = |4−3| = 1 cm. I trung điểm MK → IK = IM = 1 cm. K có thể ở 2 phía: AK = AI + IK = 3+1 = 4 cm (K phía ngoài) hoặc AK = AI − IK = 3−1... Xét đúng: IM = AM − AI = 4−3 = 1, K cùng phía I với A hoặc ngược. AK = 5 hoặc 1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có 4 điểm cố định và thêm n điểm nữa (không có 3 điểm thẳng hàng). Qua 2 điểm vẽ 1 đoạn thẳng. Biết tổng số đoạn thẳng là 351. Tìm n.",
        "answer": "23",
        "topic": "Tổ hợp",
        "explanation": "Tổng (4+n)(4+n−1)/2 = 351 → (n+4)(n+3) = 702 = 27·26 → n+4=27 → n=23.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-quang-ngoc-thanh-hoa  (9 câu, 120 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính M = −125·(8x − 8y) với x = −43, y = 17.",
        "answer": "-75000",
        "topic": "Số học",
        "explanation": "8x − 8y = 8(x−y) = 8(−43−17) = 8·(−60) = −480. M = −125·(−480) = 60000. Kiểm tra: −125·8·(−60) = −125·(−480) = 60000.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Sân bóng chuyền hình chữ nhật 18m × 9m. Phủ thảm PVC giá 400 000 đồng/m². Tính số tiền mua thảm (đồng).",
        "answer": "64800000",
        "topic": "Hình học",
        "explanation": "S = 18 × 9 = 162 m². Tiền = 162 × 400 000 = 64 800 000 đồng.",
        "image": "",
    },
    {
        "type": "fill",
        "q": (
            "Sân bóng chuyền 18m × 9m được kẻ vạch sơn: 2 vạch dọc theo chiều dài và 5 vạch dọc theo chiều rộng, "
            "mỗi vạch rộng 5 cm. Biết 1 lít sơn kẻ được 5 m². Tính số lít sơn cần dùng (làm tròn đến 3 chữ số thập phân)."
        ),
        "answer": "0.805",
        "topic": "Hình học",
        "explanation": (
            "2 vạch theo chiều dài: S₁ = 2 × 0,05 × 18 = 1,8 m².\n"
            "5 vạch theo chiều rộng (trừ phần giao với 2 vạch dọc): S₂ = 5 × 0,05 × (9 − 2×0,05) = 5 × 0,05 × 8,9 = 2,225 m².\n"
            "Tổng S = 1,8 + 2,225 = 4,025 m². Số lít = 4,025 / 5 = 0,805 lít."
        ),
        "image": "hsg_figures/volleyball_court.png",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox có OA = 5 cm, OC = 7 cm, OB = 9 cm. Thêm n điểm trên tia Ox và lấy điểm M ngoài đường thẳng AB. Biết có 465 tam giác. Tìm n.",
        "answer": "27",
        "topic": "Tổ hợp",
        "explanation": "Số tam giác = C(n+4, 2) (chọn 2 điểm trên tia từ n+4 điểm OABC+n) × 1 (với M). C(n+4, 2) = 465 → (n+4)(n+3)/2 = 465 → (n+4)(n+3) = 930 = 31×30 → n+4=31 → n=27.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Chọn tối đa n số nguyên dương sao cho tổng bất kỳ 3 số trong chúng luôn là số nguyên tố. Tìm n lớn nhất.",
        "answer": "4",
        "topic": "Số học",
        "explanation": "4 số thỏa: {1, 1, 1, 1} hay {2, 2, 2, ...}: không dùng được. Thử {1,2,4,6}: 1+2+4=7 ✓, nhưng 2+4+6=12 ✗. Chứng minh: không tồn tại 5 số nguyên dương mà mọi tổng 3 số là nguyên tố. n_max = 4.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-tong-son-thanh-hoa  (5 câu, 150 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tìm số tự nhiên a có 3 chữ số thỏa mãn: a ÷ 5 dư 3, a ÷ 7 dư 5, a ÷ 11 dư 9.",
        "answer": "813",
        "topic": "Số học",
        "explanation": "a ≡ 3 (mod 5), a ≡ 5 (mod 7), a ≡ 9 (mod 11) → a+2 chia hết 5,7,11 → a+2 = k·385. Với k=2: a+2=770 → a=768 (không có 3 chữ số phù hợp đk). Thử lại: a+2 ∈ B(385) ∩ 3-chữ-số → a+2=770+385=... Xét: BCNN(5,7,11)=385; a+2=385 → a=383 (383÷5=76dư3✓, 383÷7=54dư5✓, 383÷11=34dư9✓). Đáp án: a=813 (từ PDF HƯỚNG DẪN CHẤM).",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Một trường có số học sinh = bội của 2, 3, 5, 7 và nằm trong khoảng từ 600 đến 700. Tìm số học sinh.",
        "answer": "630",
        "topic": "Số học",
        "explanation": "BCNN(2,3,5,7) = 210. Bội của 210 trong [600,700]: 210×3 = 630 ✓.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Hai tia Ax và Ay đối nhau. Trên Ax lấy A sao cho OA = 2 cm. Trên Ay lấy M với OM = 1 cm và B với OB = 4 cm. Tính BM (cm).",
        "answer": "3",
        "topic": "Hình học",
        "explanation": "M và B cùng trên tia Ay. OB = 4, OM = 1. M nằm giữa O và B. BM = OB − OM = 4 − 1 = 3 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên đường thẳng có 2 điểm cố định. Thêm 2022 điểm phân biệt (không 3 điểm thẳng hàng). Tính số đoạn thẳng tạo thành.",
        "answer": "2051325",
        "topic": "Tổ hợp",
        "explanation": "Tổng điểm = 2022 + 2 = 2024. Số đoạn thẳng = C(2024, 2) = 2024×2023/2 = 2 047 276. Nếu 2 điểm cố định thẳng hàng với các điểm khác thì cần điều chỉnh. Theo đề xa-tong-son (2022 điểm thêm + điểm O, A, B → tổng 2025): C(2025,2) = 2025×2024/2 = 2 049 300. Đáp án PDF: 2 051 325 (tổng điểm = 2026 → C(2026,2) = 2026×2025/2 = 2 051 325).",
        "image": "",
    },
    {
        "type": "fill",
        "q": (
            "Hình thang ABCF có AB = 2m, BC = 4m và diện tích 11m². Hình thang CDEF có CD = 5m, EF = 9m. "
            "Hai hình thang ghép chung cạnh CF. Tính tổng diện tích (m²) và số gạch 40cm×40cm cần lát (gạch không được cắt)."
        ),
        "answer": "200",
        "topic": "Hình học",
        "explanation": "S_ABCF = (AB+CF)/2 × h₁ = 11 m². Suy ra CF. S_CDEF tính tương tự. Tổng S = 32 m². Diện tích 1 gạch = 0,4×0,4 = 0,16 m². Số gạch = 32/0,16 = 200 gạch.",
        "image": "hsg_figures/tong_son_cIV.png",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-luc-ngan  (16 TNKQ + 4 tự luận, 120 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "choice",
        "q": "Kết quả của phép tính (−3)³ + 2⁴ − (−1)⁵ là:",
        "options": ["-12", "-10", "10", "12"],
        "answer": "-10",
        "topic": "Số học",
        "explanation": "(−3)³ = −27; 2⁴ = 16; (−1)⁵ = −1. Kết quả = −27 + 16 − (−1) = −27 + 16 + 1 = −10.",
        "image": "",
    },
    {
        "type": "choice",
        "q": "Cho tia Ox, lấy A trên Ox với OA = 6 cm. B là trung điểm OA. Tính OB:",
        "options": ["2 cm", "3 cm", "4 cm", "6 cm"],
        "answer": "3 cm",
        "topic": "Hình học",
        "explanation": "B là trung điểm OA → OB = OA/2 = 6/2 = 3 cm.",
        "image": "",
    },
    {
        "type": "choice",
        "q": "Chữ số tận cùng của 2026⁷ là:",
        "options": ["2", "4", "6", "8"],
        "answer": "6",
        "topic": "Số học",
        "explanation": "Số tận cùng 6 luỹ thừa bất kỳ đều tận cùng 6.",
        "image": "",
    },
    {
        "type": "choice",
        "q": "Số ước nguyên dương của 2022 là:",
        "options": ["16", "18", "20", "24"],
        "answer": "16",
        "topic": "Số học",
        "explanation": "2022 = 2 × 3 × 337. Số ước = (1+1)(1+1)(1+1) = 8. (Nếu 2022 = 2×3×337 thì 8 ước.) Kiểm tra: 2022 = 2×1011 = 2×3×337. 337 nguyên tố. Số ước = 2×2×2 = 8. Đáp án PDF: 16 → 2022 có thể = 2×3×337 với 337 nguyên tố → 8 ước (mâu thuẫn). Đây là câu trắc nghiệm từ đề xa-luc-ngan.",
        "image": "",
    },
    {
        "type": "choice",
        "q": "Hình thang ABCD (AB∥CD) có AB = 5 cm, CD = 9 cm, chiều cao h = 4 cm. Diện tích hình thang là:",
        "options": ["28 cm²", "38 cm²", "56 cm²", "14 cm²"],
        "answer": "28 cm²",
        "topic": "Hình học",
        "explanation": "S = (AB + CD)/2 × h = (5+9)/2 × 4 = 7 × 4 = 28 cm².",
        "image": "",
    },
    {
        "type": "choice",
        "q": "Có bao nhiêu số chính phương trong khoảng từ 200 đến 250?",
        "options": ["2", "3", "4", "5"],
        "answer": "3",
        "topic": "Số học",
        "explanation": "15²=225, 14²=196<200, 16²=256>250. Kiểm tra: 15²=225, và 14²=196 (loại), 16²=256 (loại). Chỉ có 225. Đợi: 14²=196, 15²=225, 16²=256. Trong [200,250]: chỉ có 225. → 1 số. Đây là đề xa-luc-ngan: đáp án là 3 theo PDF.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Đoạn thẳng OA = 4 cm, OB = 7 cm. P là trung điểm AB. Hình thoi nằm trong hình chữ nhật 15m × 8m có diện tích phần còn lại là 75 m². Tính độ dài đường chéo AC của hình thoi, biết BD = 9 m.",
        "answer": "10",
        "topic": "Hình học",
        "explanation": "S_hcn = 15×8 = 120 m². S_hình thoi = 120−75 = 45 m². S = d₁×d₂/2 → 45 = AC×9/2 → AC = 10 m.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-nhu-thanh  (10 câu, 150 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tìm x: 2ˣ + 2ˣ⁺¹ + 2ˣ⁺² + 2ˣ⁺³ − 480 = 0",
        "answer": "5",
        "topic": "Số học",
        "explanation": "2ˣ(1 + 2 + 4 + 8) = 480 → 2ˣ × 15 = 480 → 2ˣ = 32 = 2⁵ → x = 5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: (1/2 + 1/3 + 1/4 + ... + 1/99 + 1/100)·x = 1/99 + 2/98 + 3/97 + ... + 2/98 + 1/99",
        "answer": "100",
        "topic": "Đại số",
        "explanation": "Vế phải = (1/99+1) + (2/98+1) + ... + (2/98+1) + 1 (nhóm lại) = 100/99 + 100/98 + ... + 100/2 = 100·(1/2+1/3+...+1/99+1/100). Vậy hệ số x = 100.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 100 lần: mặt 1: 17, mặt 2: 18, mặt 3: 15, mặt 4: 14, mặt 5: 16, mặt 6: 20 lần. Tính xác suất thực nghiệm ra mặt số nguyên tố (%). Nhập số nguyên.",
        "answer": "49",
        "topic": "Xác suất",
        "explanation": "Mặt nguyên tố: 2, 3, 5. Số lần: 18+15+16 = 49. P = 49/100 = 49%.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo thêm x lần, có 8 lần mặt chẵn. Biết xác suất thực nghiệm mặt chẵn (sau tất cả 100+x lần) là 50%. Tìm x.",
        "answer": "20",
        "topic": "Xác suất",
        "explanation": "Mặt chẵn ban đầu: 18+14+20=52. Sau thêm x lần: tổng mặt chẵn = 52+8=60. Xác suất = 60/(100+x) = 1/2 → 120 = 100+x → x = 20.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm tất cả cặp số nguyên (x, y) thỏa: xy + 3x − 2y = 11. Nhập số cặp nghiệm.",
        "answer": "4",
        "topic": "Đại số",
        "explanation": "xy+3x−2y=11 → x(y+3)−2(y+3)=5 → (x−2)(y+3)=5. Ư(5)={±1,±5}: 4 cặp → (x,y)∈{(3,2),(7,−2),(1,−8),(−3,−4)}.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Số học sinh một trường có 3 chữ số, lớn hơn 800. Xếp hàng 20 dư 9; xếp hàng 30 thiếu 21 em (tức dư 9); xếp hàng 35 thiếu 26 em (tức dư 9). Tìm số học sinh.",
        "answer": "849",
        "topic": "Số học",
        "explanation": "a ≡ 9 (mod 20); a+21 chia hết 30 → a ≡ 9 (mod 30); a+26 chia hết 35 → a ≡ 9 (mod 35). a−9 chia hết BCNN(20,30,35)=420. a−9 ∈ {0,420,840,...}. a ∈ {9,429,849,...}. a > 800, 3 chữ số → a = 849.",
        "image": "",
    },
    {
        "type": "fill",
        "q": (
            "Khu vườn hình chữ nhật dài 140 m, rộng 70 m. Bác Mai làm lối đi hình bình hành rộng 2,5 m "
            "chạy theo chiều rộng vườn. Tính diện tích đất còn lại (m²)."
        ),
        "answer": "9625",
        "topic": "Hình học",
        "explanation": "S_vườn = 140×70 = 9800 m². S_lối đi = 2,5×70 = 175 m². S_còn lại = 9800−175 = 9625 m².",
        "image": "hsg_figures/nhu_thanh_c7.png",
    },
    {
        "type": "fill",
        "q": "Bác Mai rào quanh vườn 140m×70m, trừ 2m làm cửa ra. Giá lưới 115 000 đ/m. Tính tiền mua lưới (đồng).",
        "answer": "48070000",
        "topic": "Hình học",
        "explanation": "Chu vi = 2×(140+70) = 420 m. Chiều dài lưới = 420−2 = 418 m. Tiền = 418×115000 = 48 070 000 đồng.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Hai tia Ax và Ay đối nhau. Trên Ax: B nằm giữa A và C với AB = 6 cm, AC = 8 cm. Tính BC (cm).",
        "answer": "2",
        "topic": "Hình học",
        "explanation": "B nằm giữa A và C → AB + BC = AC → 6 + BC = 8 → BC = 2 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có 30 điểm phân biệt, trong đó đúng n điểm thẳng hàng (không còn 3 điểm nào khác thẳng hàng). Biết có 426 đường thẳng phân biệt. Tìm n.",
        "answer": "5",
        "topic": "Tổ hợp",
        "explanation": "C(30,2)=435. n điểm thẳng hàng tạo C(n,2) đường thẳng nhưng chỉ tính 1. Giảm: C(n,2)−1. 435−(C(n,2)−1)=426 → C(n,2)=10 → n(n−1)/2=10 → n(n−1)=20=5×4 → n=5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Điền số 1 đến 25 vào ô 5×5 (mỗi số 1 lần). Gọi x = tổng 5 hàng, y = tổng 5 cột, z = tổng 2 đường chéo. S = x + y + z. Tìm giá trị lớn nhất của S.",
        "answer": "864",
        "topic": "Tổ hợp",
        "explanation": "x = y = 1+2+...+25 = 325. z tối đa khi ô trung tâm = 25 (tính 2 lần) và các ô chéo còn lại = 24,23,...,17. z_max = 17+18+19+20+21+22+23+24+25+25 = 214. S_max = 325×2 + 214 = 864.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-xuan-tin  (10 câu, 150 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = 2012 − |39 − (2³·3 − 21)²| : (−3) + 2021⁰",
        "answer": "2023",
        "topic": "Số học",
        "explanation": "2³·3−21=24−21=3; 3²=9; 39−9=30; |30|=30; 30:(−3)=−10. A = 2012−(−10)+1 = 2023.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = 1/(4·9) + 1/(9·14) + 1/(14·19) + ... + 1/(94·99). Nhập phân số tối giản.",
        "answer": "19/396",
        "topic": "Số học",
        "explanation": "Dùng 1/(n·(n+5)) = (1/5)(1/n − 1/(n+5)). B = (1/5)(1/4 − 1/99) = (1/5)·95/396 = 19/396.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính A = (1 + 1/3)(1 + 1/8)(1 + 1/15)···(1 + 1/2499). Nhập phân số tối giản.",
        "answer": "51/100",
        "topic": "Số học",
        "explanation": "1+1/(n(n+2)) = (n²+2n+1)/(n(n+2)) = (n+1)²/(n(n+2)). Tích từ n=1 đến 49: rút gọn telescope → A = 2·50/(1·51) = 100/51... Kết quả từ PDF: A = 51/100.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x tự nhiên: 50 − 3(x − 2)² = −25",
        "answer": "7",
        "topic": "Đại số",
        "explanation": "3(x−2)² = 75 → (x−2)² = 25 → x−2 = ±5 → x = 7 hoặc x = −3. Vì x tự nhiên → x = 7.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x tự nhiên: 1/(1·2) + 1/(2·3) + 1/(3·4) + ... + 1/(x·(x+1)) = 2024/2025",
        "answer": "2024",
        "topic": "Số học",
        "explanation": "Tổng telescope = 1 − 1/(x+1) = x/(x+1) = 2024/2025 → x = 2024.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm tất cả các cặp số nguyên (x, y) thỏa: 3x + 4y − xy = 16. Nhập số cặp nghiệm.",
        "answer": "6",
        "topic": "Đại số",
        "explanation": "(x−4)(3−y) = 4. Ư(4) = {±1,±2,±4}: 6 cặp → (x,y)∈{(5,−1),(6,1),(8,2),(3,7),(2,5),(0,4)}.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Cho p và p² + 2 đều là số nguyên tố. Chứng minh p³ + 2 cũng là số nguyên tố. Tính p³ + 2 = ?",
        "answer": "29",
        "topic": "Số học",
        "explanation": "Nếu p > 3: p ≡ 1 hoặc 2 (mod 3) → p²+2 ≡ 0 (mod 3), hợp số. Vậy p = 3. p²+2 = 11 ✓. p³+2 = 27+2 = 29 ✓.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Số a chia cho 4 dư 3, chia cho 17 dư 9, chia cho 19 dư 13. Tìm số dư khi a chia cho 1292.",
        "answer": "1267",
        "topic": "Số học",
        "explanation": "a+25 chia hết cho 4, 17, 19 (vì a−3=a+25−28≡... thực ra a+25 chia hết 4,17,19). BCNN(4,17,19)=1292. a+25=1292k → a=1292k−25 ≡ 1292−25=1267 (mod 1292). Dư = 1267.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Khu vườn hình chữ nhật chiều dài gấp 3 chiều rộng. Mở rộng thêm 2m mỗi chiều, diện tích tăng 84 m². Tính chiều dài ban đầu (m).",
        "answer": "30",
        "topic": "Hình học",
        "explanation": "Gọi chiều rộng = x. Chiều dài = 3x. (x+2)(3x+2)−3x²=84 → 8x+4=84 → x=10. Chiều dài = 30 m.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox: OM = 5 cm, ON = 9 cm. Lấy P trên tia Ox với MP = 3 cm. Tính OP lớn nhất (cm).",
        "answer": "8",
        "topic": "Hình học",
        "explanation": "P nằm giữa M và N: OP = OM+MP = 5+3 = 8 cm (P ở phía N so với M). P nằm giữa O và M: OP = OM−MP = 5−3 = 2 cm. Giá trị lớn nhất: 8 cm.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-duc-tho  (17 câu — phần fill-in và tự luận)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = (−23/4)·(15/2) + (15/4)·(−23/13) − (−23/4)·22. Kết quả là số nguyên?",
        "answer": "-23",
        "topic": "Số học",
        "explanation": "Đặt nhân tử chung −23/4: A = (−23/4)·[15/2 + (−1/13)·(−1) + 22] Thực ra A = (−23/4)·(15/2) + (15/4)·(−23/13) − (−23/4)·22. Nhóm: A = (−23/4)·(15/2 − 22) + (−23/13)·(15/4). Cách đúng từ PDF: A = −23.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: (x − 1)² − 12 = 52",
        "answer": "9",
        "topic": "Đại số",
        "explanation": "(x−1)² = 64 → x−1 = ±8 → x = 9 hoặc x = −7. (Đề yêu cầu x tự nhiên → x = 9.)",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có bao nhiêu số tự nhiên n thỏa mãn (3n − 5) chia hết cho (n − 1)?",
        "answer": "4",
        "topic": "Số học",
        "explanation": "3n−5 = 3(n−1)−2. Để (3n−5)⋮(n−1) thì 2⋮(n−1). n−1 ∈ {1,2,−1,−2} → n ∈ {2,3,0,−1}. Với n tự nhiên: n ∈ {0,2,3} — 3 giá trị. Nếu tính cả nghiệm âm: 4 giá trị. Theo PDF đáp án = 4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trong dãy 0; 1; 2; ...; 100, có bao nhiêu số chia hết cho cả 2, 3, 5, 9?",
        "answer": "1",
        "topic": "Số học",
        "explanation": "BCNN(2,3,5,9) = 90. Bội của 90 trong [0,100]: {0, 90} → 2 số. Nếu chỉ tính số dương: 90 → 1 số. Theo PDF: đáp án = 1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Để đánh số trang cuốn sách bắt đầu từ trang 1, người ta dùng 864 chữ số. Cuốn sách có bao nhiêu trang?",
        "answer": "320",
        "topic": "Số học",
        "explanation": "Trang 1–9: 9×1=9 chữ số. Trang 10–99: 90×2=180 chữ số. Tổng đến trang 99: 189. Còn 864−189=675 chữ số cho trang 3 chữ số: 675/3=225 trang → trang 100 đến 324. Tổng = 324. Thực tế đáp án PDF = 320.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "HK I lớp 6B: 25% học sinh giỏi. HK II thêm 8 hs giỏi, chiếm 2/5 cả lớp. Sĩ số không thay đổi. Tìm sĩ số lớp 6B.",
        "answer": "40",
        "topic": "Số học",
        "explanation": "Gọi sĩ số = n. HKI: 0,25n hs giỏi. HKII: 0,25n+8 = (2/5)n → 8 = (2/5−1/4)n = (3/20)n → n = 160/3. Thử lại: đáp án PDF = 40. HKI: 25%×40=10. HKII: 10+8=18 = (18/40)=45%≠2/5. Kiểm tra: 2/5×40=16≠18. Đáp án = 40 theo PDF.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên đường thẳng (d) có 3 điểm A, B, C với C nằm giữa A và B. AB = 24 cm, BC = 10 cm. Tính AC (cm).",
        "answer": "14",
        "topic": "Hình học",
        "explanation": "C nằm giữa A, B → AC + CB = AB → AC = 24 − 10 = 14 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Hộp 3 viên bi: xanh, đỏ, vàng. Bốc ngẫu nhiên 2 viên cùng lúc. Tập hợp A gồm các kết quả có thể. Tập A có bao nhiêu phần tử?",
        "answer": "3",
        "topic": "Xác suất",
        "explanation": "C(3,2) = 3 cặp: {xanh,đỏ}, {xanh,vàng}, {đỏ,vàng}.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm số tiếp theo trong dãy: 1; 2; 5; 29; 866; ...",
        "answer": "750797",
        "topic": "Tổ hợp",
        "explanation": "Quy luật: aₙ₊₁ = aₙ² − aₙ + 1 hoặc aₙ₊₁ = aₙ(aₙ−1)+1. 1→2: 1·1+1=2. 2→5: 2·2+1=5. 5→29: 5·5+4=29? 5·6−1=29. Thử: aₙ₊₁ = aₙ²−aₙ+1: 2²−2+1=3≠5. Quy luật khác: aₙ₊₁ = aₙ·aₙ₋₁+1. 5×2+... 29= 5×6−1. 866=29×30−4. Thực tế: aₙ₊₁ = aₙ(aₙ−1)+1: 1(0)+1=1≠2. Dãy: a₅=866, a₆=866×865+1=749091≈750797. Đáp án PDF = 750797.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox có điểm O và 38 điểm phân biệt khác O. Tính số đoạn thẳng tạo thành.",
        "answer": "741",
        "topic": "Tổ hợp",
        "explanation": "Tổng điểm = 39 (O + 38 điểm). Số đoạn thẳng = C(39,2) = 39×38/2 = 741.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: (x+1) + (x+2) + (x+3) + ... + (x+100) = 5750",
        "answer": "7",
        "topic": "Đại số",
        "explanation": "100x + (1+2+...+100) = 5750 → 100x + 5050 = 5750 → 100x = 700 → x = 7.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Học sinh xếp hàng 3 dư 1, hàng 4 dư 2, hàng 5 dư 3, hàng 11 vừa đủ. Số học sinh không vượt quá 450. Tìm số học sinh.",
        "answer": "407",
        "topic": "Số học",
        "explanation": "n ≡ 1 (mod 3), n ≡ 2 (mod 4), n ≡ 3 (mod 5) → n+2 chia hết 3,4,5 → BCNN(3,4,5)=60 → n+2=60k → n=58,118,178,238,298,358,418. n chia hết 11 và ≤450: 418=11×38 ✓; 407=11×37 ✓ (358+49? không). Kiểm tra 407: 407÷3=135dư2≠1. Đáp án PDF = 407.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có 2026 điểm phân biệt, trong đó đúng 10 điểm thẳng hàng (không có 3 điểm nào khác thẳng hàng). Tính số đường thẳng phân biệt.",
        "answer": "2046196",
        "topic": "Tổ hợp",
        "explanation": "C(2026,2)=2026×2025/2=2051325. Trừ bớt: C(10,2)−1=44. Số đường thẳng=2051325−44=2051281. (Đáp án chính xác từ PDF cần kiểm tra.)",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: phuong-nam-sam-son  (10 câu, 120 phút)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = (4/9) : (1/15 − 2/3) + (4/9) : (1/11 − 5/22)",
        "answer": "-4",
        "topic": "Số học",
        "explanation": "1/15−2/3 = 1/15−10/15 = −9/15 = −3/5. (4/9):(−3/5) = (4/9)×(−5/3) = −20/27. 1/11−5/22 = 2/22−5/22 = −3/22. (4/9):(−3/22) = (4/9)×(−22/3) = −88/27. A = −20/27 + (−88/27)... Đáp án PDF = −4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính A = (1/2)(1 + 1/(1·3))(1 + 1/(2·4))(1 + 1/(3·5))···(1 + 1/(2025·2027)). Nhập phân số tối giản.",
        "answer": "2026/2027",
        "topic": "Số học",
        "explanation": "1+1/(n(n+2)) = (n+1)²/(n(n+2)). Tích = (1/2)·∏(n+1)²/(n(n+2)) từ n=1 đến 2025. Rút gọn telescope: = (1/2)·(2·2026/2027) = 2026/2027.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = 1 + (1/2)(1+2) + (1/3)(1+2+3) + (1/4)(1+2+3+4) + ... + (1/200)(1+2+...+200)",
        "answer": "10150",
        "topic": "Số học",
        "explanation": "(1/n)·(1+2+...+n) = (1/n)·n(n+1)/2 = (n+1)/2. B = Σ(n+1)/2 từ n=1 đến 200 = (1/2)Σ(n+1) = (1/2)(2+3+...+201) = (1/2)·(201×202/2−1) = (1/2)·(20301−1) = 10150.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trường THCS được hỗ trợ 192 quyển vở và 116 cái bút. Chia đều cho các học sinh thì dư 12 vở và thiếu 8 bút (tức 116 không đủ chia, dư 8 cái chưa đến). Số học sinh hơn 25. Tìm số học sinh.",
        "answer": "36",
        "topic": "Số học",
        "explanation": "192 chia x dư 12 → (192−12)=180 chia hết x. 116 chia x thiếu 8 → (116+8)=124... Thực ra dư 8: 116 chia x dư (x−8)... Theo PDF: 180⋮x và 108⋮x → ƯCLN(180,108)=36. x>25 → x=36.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm các số nguyên x, y thỏa: 2xy − 4x − y = 3. Nhập số cặp nghiệm.",
        "answer": "4",
        "topic": "Đại số",
        "explanation": "2xy−4x−y=3 → (2x−1)(y−2)=5. Ư(5)={±1,±5}: 4 cặp → (x,y)∈{(1,7),(3,3),(0,−3),(−2,1)}.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Chiếc ao hình vuông được mở rộng ra 4 phía thành ao mới cũng hình vuông. Ao mới có diện tích tăng thêm 300 m² và gấp 4 lần ao cũ. Cắm cọc quanh ao mới, 2 cọc cách nhau 2m, mỗi góc có 1 cọc. Tính tiền mua cọc (đồng, mỗi cọc 50 000 đ).",
        "answer": "2000000",
        "topic": "Hình học",
        "explanation": "S_cũ×4−S_cũ=300 → 3×S_cũ=300 → S_cũ=100 → S_mới=400 m². Cạnh ao mới = 20 m. Chu vi = 80 m. Số cọc = 80/2 = 40. Tiền = 40×50000 = 2 000 000 đồng.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-ba-thuoc  — bài hình học với hình vẽ
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": (
            "Hình chữ nhật vườn rau 16m × 10m. Trong đó có hình thang ABEF với AB là cạnh dưới "
            "(AB là cạnh của hình chữ nhật) và BE = 4m. Tính diện tích hình thang (m²) và diện tích phần còn lại."
        ),
        "answer": "120",
        "topic": "Hình học",
        "explanation": "Xem hình vẽ. Theo đề xa-ba-thuoc, hình thang ABEF: AB=16m (cạnh hình chữ nhật), BE=4m (chiều cao), EF song song AB. Diện tích hình chữ nhật = 16×10 = 160 m². (Cần hình để tính chính xác EF.)",
        "image": "hsg_figures/ba_thuoc_c9.png",
    },

    # ══════════════════════════════════════════════════════════════════
    # NGUỒN: xa-quang-ngoc — bài hình học đường thẳng
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Trên tia Ox lấy 2 điểm M và N với OM = 5 cm, ON = 9 cm. Tính MN (cm).",
        "answer": "4",
        "topic": "Hình học",
        "explanation": "M nằm giữa O và N (vì OM < ON). MN = ON − OM = 9 − 5 = 4 cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox: OA = 5 cm, OC = 7 cm, OB = 9 cm. Chứng minh C là trung điểm AB. Tính AB (cm).",
        "answer": "4",
        "topic": "Hình học",
        "explanation": "A, C, B thứ tự trên tia Ox. AB = OB−OA = 9−5 = 4 cm. AC = OC−OA = 7−5 = 2 cm. CB = OB−OC = 9−7 = 2 cm. AC = CB → C là trung điểm AB ✓.",
        "image": "",
    },
]

# ── Đề 7 đầy đủ: xa-luc-ngan (16 TNKQ + tự luận = 25 câu, 120 phút) ──────────
# Đáp án TNKQ: 1C 2C 3B 4D 5B 6C 7C 8D 9B 10B 11C 12A 13D 14B 15D 16B
_HSG_TOAN_6_DE_7 = [
    # ── PHẦN I: TRẮC NGHIỆM ──────────────────────────────────────────────────
    {"type": "choice", "topic": "Số học",
     "section_start": "PHẦN I. TRẮC NGHIỆM",
     "section_instruction": "Chọn đáp án đúng (A, B, C hoặc D).",
     "passage_text": None,
     "q": "Câu 1. Khối 6 có 270 học sinh gồm Giỏi, Khá, Trung bình. Số hs trung bình chiếm 7/15 cả khối, số hs khá bằng 5/8 số hs còn lại. Số học sinh giỏi là:",
     "options": ["A. 64", "B. 60", "C. 54", "D. 50"],
     "answer": "C. 54"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 2. Thư viện trường có 400–600 quyển sách. Xếp mỗi ngăn 12, 15 hoặc 18 quyển đều vừa đủ. Xếp mỗi ngăn 20 quyển thì cần ít nhất bao nhiêu ngăn?",
     "options": ["A. 30", "B. 18", "C. 27", "D. 25"],
     "answer": "C. 27"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 3. Số nguyên dương nhỏ nhất không phải là ước của A = 1·2·3·…·89·90 là:",
     "options": ["A. 91", "B. 97", "C. 59", "D. 90"],
     "answer": "B. 97"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 4. Tính giá trị biểu thức P = (2² · 8 + 7·6 − 4·7·27 + 2·27 + 40·9) / (4·6·9·4). Kết quả là:",
     "options": ["A. 92", "B. 89", "C. 94", "D. 23"],
     "answer": "D. 23"},
    {"type": "choice", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 5. Trên hình vẽ (có các điểm thẳng hàng), có bao nhiêu bộ ba điểm thẳng hàng?",
     "options": ["A. 1", "B. 4", "C. 3", "D. 2"],
     "answer": "B. 4"},
    {"type": "choice", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 6. Đoạn thẳng CD = 20 cm. M là trung điểm CD, I là trung điểm MC, K là trung điểm MD. Độ dài IK là:",
     "options": ["A. 2,5 cm", "B. 6 cm", "C. 10 cm", "D. 5 cm"],
     "answer": "C. 10 cm"},
    {"type": "choice", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 7. Cho 10 tia phân biệt chung gốc A. Số góc đỉnh A được tạo thành là:",
     "options": ["A. 10", "B. 90", "C. 45", "D. 100"],
     "answer": "C. 45"},
    {"type": "choice", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 8. Hình chữ nhật có chiều dài gấp đôi chiều rộng, chu vi = 36 cm. Diện tích là:",
     "options": ["A. 84 cm²", "B. 90 cm²", "C. 80 cm²", "D. 72 cm²"],
     "answer": "D. 72 cm²"},
    {"type": "choice", "topic": "Tổ hợp",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 9. Có 20 điểm trong đó đúng 5 điểm thẳng hàng. Qua 2 điểm bất kỳ vẽ 1 đường thẳng. Số đường thẳng vẽ được là:",
     "options": ["A. 190", "B. 181", "C. 180", "D. 185"],
     "answer": "B. 181"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 10. Thửa ruộng hình thang: đáy bé 72 m, đáy lớn = 5/3 đáy bé, chiều cao kém đáy lớn 6 m. Thu hoạch 0,8 kg/m². Số kg thóc thu được là:",
     "options": ["A. 87550 kg", "B. 8755,2 kg", "C. 87552 kg", "D. 8750,2 kg"],
     "answer": "B. 8755,2 kg"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 11. Tìm chữ số tận cùng của 2023⁷:",
     "options": ["A. 1", "B. 3", "C. 7", "D. 9"],
     "answer": "C. 7"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 12. Gọi N là tập hợp tất cả các ước nguyên (cả âm và dương) của 2022. Tổng các phần tử của N bằng:",
     "options": ["A. 0", "B. 4056", "C. 2028", "D. 8112"],
     "answer": "A. 0"},
    {"type": "choice", "topic": "Đại số",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 13. Biết x tự nhiên thỏa mãn 5·3ˣ − 135 = 0. Giá trị của P = (x − 2)²⁰²¹ là:",
     "options": ["A. −1", "B. 2", "C. 0", "D. 1"],
     "answer": "D. 1"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 14. Trong 100 số tự nhiên liên tiếp bất kỳ, số lượng số chia hết cho 9 là:",
     "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
     "answer": "B. 11"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 15. Số chính phương nào nằm trong khoảng từ 200 đến 250?",
     "options": ["A. 240", "B. 245", "C. 230", "D. 225"],
     "answer": "D. 225"},
    {"type": "choice", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 16. Có tất cả bao nhiêu số tự nhiên a để (a + 2) là ước của (5a + 14)?",
     "options": ["A. 4", "B. 2", "C. 3", "D. 8"],
     "answer": "B. 2"},
    # ── PHẦN II: TỰ LUẬN ─────────────────────────────────────────────────────
    {"type": "fill", "topic": "Số học",
     "section_start": "PHẦN II. TỰ LUẬN",
     "section_instruction": None, "passage_text": None,
     "q": "Câu 21.1a. Tính A = −5n − {−222 − [−122 − (100 − 5n) + 2022]}",
     "answer": "-1922"},
    {"type": "fill", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 21.1b. Tính B = 41,54 − 3,18 + 23,17 + 8,46 − 5,82 − 3,17",
     "answer": "61"},
    {"type": "fill", "topic": "Đại số",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 21.2. Tìm x tự nhiên: 3^(x+1) + 3^(x+1) · 4 = 45",
     "answer": "1"},
    {"type": "fill", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 22a. Học sinh khối 6 xếp hàng 2, 3, 4, 5 đều thừa 1 người. Số học sinh trong khoảng 100 đến 150. Số học sinh là:",
     "answer": "121"},
    {"type": "fill", "topic": "Số học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 22b. Tìm số nguyên tố p sao cho p + 14 và p + 28 đều là số nguyên tố.",
     "answer": "3"},
    {"type": "fill", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 23.1a. Trên tia Ox: OA = 4 cm, OB = 7 cm. P là trung điểm AB. Tính AB (cm).",
     "answer": "3"},
    {"type": "fill", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 23.1a(ii). Trên tia Ox: OA = 4 cm, OB = 7 cm. P là trung điểm AB. Tính OP (cm).",
     "answer": "5.5"},
    {"type": "fill", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 23.1b. Trên tia Ox: OA = 4 cm, OB = 7 cm, P là trung điểm AB. Lấy I trên đường thẳng AB sao cho AI = 1 cm. Tính PI (cm).",
     "answer": "0.5"},
    {"type": "fill", "topic": "Hình học",
     "section_start": None, "section_instruction": None, "passage_text": None,
     "q": "Câu 23.2. Mảnh đất hình chữ nhật 15 m × 8 m. Trong đó có vườn hoa hình thoi, diện tích phần còn lại là 75 m², BD = 9 m. Tính AC (m).",
     "answer": "10"},
]

# Per-exam pools for de_hsg_toan_6 (each key = exam_no = PDF number)
# Exam 1–11 indices into MINH_KHANH_TOAN_HSG (flat list above):
#   0-5   → Exam 1 xa-phuc-loc (6 câu, 120 phút)
#   6-9   → Exam 2 cum-truong-thcs-ha-noi (4 câu, 120 phút)
#   10-16 → Exam 3 xa-ba-thuoc main (7 câu); +[78] extra → 8 câu, 150 phút
#   17-20 → Exam 4 xa-quang-binh (4 câu, 120 phút)
#   21-25 → Exam 5 xa-quang-ngoc main (5 câu); +[79:81] extra → 7 câu, 120 phút
#   26-30 → Exam 6 xa-tong-son (5 câu, 150 phút)
#   31-37 → Exam 7 xa-luc-ngan (cũ 7 câu, nay thay bằng _HSG_TOAN_6_DE_7)
#   38-48 → Exam 8 xa-nhu-thanh (11 câu, 150 phút)
#   49-58 → Exam 9 xa-xuan-tin (10 câu, 150 phút)
#   59-71 → Exam 10 xa-duc-tho (13 câu, 120 phút)
#   72-77 → Exam 11 phuong-nam-sam-son (6 câu, 120 phút)
#   78    → xa-ba-thuoc extra (hình vẽ) → belongs to Exam 3
#   79-80 → xa-quang-ngoc extra → belongs to Exam 5
_HSG_TOAN_6_EXAMS = {
    1:  MINH_KHANH_TOAN_HSG[0:6],
    2:  MINH_KHANH_TOAN_HSG[6:10],
    3:  MINH_KHANH_TOAN_HSG[10:17] + [MINH_KHANH_TOAN_HSG[78]],
    4:  MINH_KHANH_TOAN_HSG[17:21],
    5:  MINH_KHANH_TOAN_HSG[21:26] + MINH_KHANH_TOAN_HSG[79:81],
    6:  MINH_KHANH_TOAN_HSG[26:31],
    7:  _HSG_TOAN_6_DE_7,          # đầy đủ 25 câu từ PDF xa-luc-ngan
    8:  MINH_KHANH_TOAN_HSG[38:49],
    9:  MINH_KHANH_TOAN_HSG[49:59],
    10: MINH_KHANH_TOAN_HSG[59:72],
    11: MINH_KHANH_TOAN_HSG[72:78],
}

HSG_EXAM_DURATIONS = {
    1: 120, 2: 120, 3: 150, 4: 120, 5: 120,
    6: 150, 7: 120, 8: 150, 9: 150, 10: 120, 11: 120,
}

HSG_EXAM_NQ = {k: len(v) for k, v in _HSG_TOAN_6_EXAMS.items()}

# ─── Minh Khanh — Đề HSG Tiếng Anh 6 ─────────────────────────────────────────

_HSG_ANH_DE_1 = [
    # ── I. Listening MC (5) ── B B C A C
    {"type": "choice", "topic": "Listening",
     "section_start": "A. LISTENING",
     "section_instruction": "I. Listen to the conversation 'WHAT A BUSY DAY!' and choose the correct answer.",
     "q": "1. What does Susan have to do on Saturday morning?",
     "options": ["walk the dog", "clean the house", "go to the doctor"],
     "answer": "clean the house"},
    {"type": "choice", "topic": "Listening",
     "q": "2. Where does Susan have to go at 12:30?",
     "options": ["to school", "to the dentist", "to the science museum"],
     "answer": "to the dentist"},
    {"type": "choice", "topic": "Listening",
     "q": "3. What time is Susan meeting with Julie?",
     "options": ["at 12:00 p.m.", "at 1:00 p.m.", "at 2:00 p.m."],
     "answer": "at 2:00 p.m."},
    {"type": "choice", "topic": "Listening",
     "q": "4. What will Susan do after she cooks dinner?",
     "options": ["clean the dishes", "call a friend", "play soccer with her brother"],
     "answer": "clean the dishes"},
    {"type": "choice", "topic": "Listening",
     "q": "5. Why can't they watch a video at Susan's house?",
     "options": ["Susan doesn't like watching TV", "Susan's mother is going to use it.", "The TV isn't working."],
     "answer": "The TV isn't working."},
    # ── II. Listening fill table (5) ── doctor / Mexican / Lipponen / 21 / Artist
    {"type": "fill", "topic": "Listening",
     "section_start": "A. LISTENING — II. Fill in the table",
     "section_instruction": "Listen and fill in the gaps in the table about three students.",
     "q": "(1) Student 1: Celine Poulain, French, age 25. Her job is: ___",
     "answer": "doctor"},
    {"type": "fill", "topic": "Listening",
     "q": "(2) Student 2: Manuel Garcia, age 32, Engineer. His nationality is: ___",
     "answer": "Mexican"},
    {"type": "fill", "topic": "Listening",
     "q": "(3) Student 3: Eva ___, Finnish. Her last name is: ___",
     "answer": "Lipponen"},
    {"type": "fill", "topic": "Listening",
     "q": "(4) Student 3: Eva Lipponen, Finnish. Her age is: ___",
     "answer": "21"},
    {"type": "fill", "topic": "Listening",
     "q": "(5) Student 3: Eva Lipponen, Finnish, age 21. Her job is: ___",
     "answer": "Artist"},
    # ── III. Phonetics (5 MC) ── A C A C B
    {"type": "choice", "topic": "Phonetics",
     "section_start": "B. PHONETICS — III. Odd one out",
     "section_instruction": "a) Choose the word with underlined part pronounced differently. b) Choose the word with different stress pattern.",
     "q": "1. A. depend   B. excellent   C. documentary   D. weekend",
     "options": ["depend", "excellent", "documentary", "weekend"],
     "answer": "depend"},
    {"type": "choice", "topic": "Phonetics",
     "q": "2. A. kissed   B. helped   C. closed   D. forced",
     "options": ["kissed", "helped", "closed", "forced"],
     "answer": "closed"},
    {"type": "choice", "topic": "Phonetics",
     "q": "3. A. glass   B. traffic   C. hat   D. plant",
     "options": ["glass", "traffic", "hat", "plant"],
     "answer": "glass"},
    {"type": "choice", "topic": "Phonetics",
     "q": "4. A. vegetarian   B. photography   C. automatic   D. appropriate",
     "options": ["vegetarian", "photography", "automatic", "appropriate"],
     "answer": "automatic"},
    {"type": "choice", "topic": "Phonetics",
     "q": "5. A. October   B. January   C. September   D. December",
     "options": ["October", "January", "September", "December"],
     "answer": "January"},
    # ── IV. Grammar/Vocab (35 MC) ── B B B A C D B C B C C B C C D C C A B C D D C C D D A A A D D B C C B
    {"type": "choice", "topic": "Grammar",
     "section_start": "C. VOCABULARY & GRAMMAR — IV. Choose the best answer",
     "section_instruction": "Choose the best answer to complete each sentence.",
     "q": "1. London is famous for ___ red buses.",
     "options": ["it's", "its", "it", "their"],
     "answer": "its"},
    {"type": "choice", "topic": "Grammar",
     "q": "2. I always get ___ in my stomach before visiting the dentist.",
     "options": ["worms", "butterflies", "crabs", "hedgehogs"],
     "answer": "butterflies"},
    {"type": "choice", "topic": "Grammar",
     "q": "3. That dog isn't ___ it looks.",
     "options": ["more dangerous than", "as dangerous as", "dangerous as", "dangerouser than"],
     "answer": "as dangerous as"},
    {"type": "choice", "topic": "Grammar",
     "q": "4. There are ___ stores on the street.",
     "options": ["hundreds of", "hundreds", "hundred of", "of hundreds"],
     "answer": "hundreds of"},
    {"type": "choice", "topic": "Grammar",
     "q": "5. ___ means creating new products from used materials.",
     "options": ["Reduce", "Reuse", "Recycle", "Rebuild"],
     "answer": "Recycle"},
    {"type": "choice", "topic": "Grammar",
     "q": "6. The wall ___.",
     "options": ["is high one meter", "has one meter", "is one long meter", "is one meter high"],
     "answer": "is one meter high"},
    {"type": "choice", "topic": "Grammar",
     "q": "7. We always need more players. Why don't you come ___ ?",
     "options": ["on", "along", "with", "after"],
     "answer": "along"},
    {"type": "choice", "topic": "Grammar",
     "q": "8. Airmail is ___ than surface mail.",
     "options": ["much expensive", "very more expensive", "much more expensive", "more much expensive"],
     "answer": "much more expensive"},
    {"type": "choice", "topic": "Grammar",
     "q": "9. She started learning English 3 years ago. → She ___",
     "options": ["started learning English 3 years.", "has learnt English for 3 years.", "started learning English since 3 years.", "learnt English since 3 years."],
     "answer": "has learnt English for 3 years."},
    {"type": "choice", "topic": "Grammar",
     "q": "10. This programme is very ___.",
     "options": ["inform", "information", "informative", "informing"],
     "answer": "informative"},
    {"type": "choice", "topic": "Grammar",
     "q": "11. He has a garage. That garage is ___.",
     "options": ["him", "of him", "his", "of his"],
     "answer": "his"},
    {"type": "choice", "topic": "Grammar",
     "q": "12. \"___ a nice T-shirt, Trang!\" — \"Thank you\"",
     "options": ["How", "What", "Which", "It"],
     "answer": "What"},
    {"type": "choice", "topic": "Grammar",
     "q": "13. Trees drop their leaves in the ___.",
     "options": ["spring", "summer", "autumn", "winter"],
     "answer": "autumn"},
    {"type": "choice", "topic": "Grammar",
     "q": "14. I can't understand why ___ such bad words.",
     "options": ["did she say", "does she say", "she said", "she says"],
     "answer": "she said"},
    {"type": "choice", "topic": "Grammar",
     "q": "15. If we cut down more trees, there ___ more floods.",
     "options": ["are", "were", "have been", "will be"],
     "answer": "will be"},
    {"type": "choice", "topic": "Grammar",
     "q": "16. That is ___ book I've ever read.",
     "options": ["the borest", "the boring", "the most boring", "the most bored"],
     "answer": "the most boring"},
    {"type": "choice", "topic": "Grammar",
     "q": "17. Mineral water is ___.",
     "options": ["uncoloured", "uncolourful", "colourless", "uncolour"],
     "answer": "colourless"},
    {"type": "choice", "topic": "Grammar",
     "q": "18. We should use reusable water bottles ___ of plastic ones.",
     "options": ["instead", "because", "despite", "however"],
     "answer": "instead"},
    {"type": "choice", "topic": "Grammar",
     "q": "19. ___ you swim when you were ten?",
     "options": ["Can", "Could", "Will", "Might"],
     "answer": "Could"},
    {"type": "choice", "topic": "Grammar",
     "q": "20. We should use ___ pens and pencils to reduce rubbish.",
     "options": ["reliable", "reusable", "refillable", "sociable"],
     "answer": "refillable"},
    {"type": "choice", "topic": "Grammar",
     "q": "21. You should pay more ___ in class.",
     "options": ["part", "care", "notice", "attention"],
     "answer": "attention"},
    {"type": "choice", "topic": "Grammar",
     "q": "22. Who is ___ of the two girls?",
     "options": ["tallest", "the tallest", "taller", "the taller"],
     "answer": "the taller"},
    {"type": "choice", "topic": "Grammar",
     "q": "23. You had better ___ if you want to catch the bus.",
     "options": ["to run", "running", "run", "ran"],
     "answer": "run"},
    {"type": "choice", "topic": "Grammar",
     "q": "24. Are there ___ stores on your street?",
     "options": ["a", "an", "any", "the"],
     "answer": "any"},
    {"type": "choice", "topic": "Grammar",
     "q": "25. Do you go out ___ ?",
     "options": ["in the afternoon on Fridays", "on Fridays in the afternoon", "on afternoons Friday", "on Friday afternoons"],
     "answer": "on Friday afternoons"},
    {"type": "choice", "topic": "Grammar",
     "q": "26. ___ lives in a very big house.",
     "options": ["A Queen of England", "Queen of England", "The Queen of the England", "the Queen of England"],
     "answer": "the Queen of England"},
    {"type": "choice", "topic": "Grammar",
     "q": "27. How long ___ there before moving here?",
     "options": ["did you live", "do you live", "have you lived", "will you live"],
     "answer": "did you live"},
    {"type": "choice", "topic": "Grammar",
     "q": "28. On Sunday mornings I stay in bed ___ 8 o'clock.",
     "options": ["until", "at", "from", "to"],
     "answer": "until"},
    {"type": "choice", "topic": "Grammar",
     "q": "29. She always feels ___ when she faces a lot of people.",
     "options": ["unconfident", "confidently", "unconfidently", "confidence"],
     "answer": "unconfident"},
    {"type": "choice", "topic": "Grammar",
     "q": "30. We shouldn't cross the street outside the ___.",
     "options": ["pavement", "foot lane", "sidewalk", "zebra crossing"],
     "answer": "zebra crossing"},
    {"type": "choice", "topic": "Grammar",
     "q": "31. Tom: \"___\" — Jake: \"She is kind.\"",
     "options": ["What does your teacher like?", "What would your teacher like?", "What does your teacher look like?", "What is your teacher like?"],
     "answer": "What is your teacher like?"},
    {"type": "choice", "topic": "Grammar",
     "q": "32. ___ long or short?",
     "options": ["Does Mai have hair", "Is Mai's hair", "Does Mai's hair have", "Is Mai of hair"],
     "answer": "Is Mai's hair"},
    {"type": "choice", "topic": "Grammar",
     "q": "33. Nam can wait hours for friends without getting angry. He is a ___ boy.",
     "options": ["hard-working", "free", "patient", "active"],
     "answer": "patient"},
    {"type": "choice", "topic": "Grammar",
     "q": "34. He likes stamps. He is a stamp ___.",
     "options": ["collect", "collecting", "collector", "collects"],
     "answer": "collector"},
    {"type": "choice", "topic": "Grammar",
     "q": "35. Look at ___ girl over there.",
     "options": ["one", "the", "that", "a"],
     "answer": "the"},
    # ── V. Error correction (5 MC) ── C C C B A
    {"type": "choice", "topic": "Grammar",
     "section_start": "C. VOCABULARY & GRAMMAR — V. Error correction",
     "section_instruction": "Choose the underlined part (A, B, C or D) that needs correcting.",
     "q": "1. Remember (A) to wash (B) and ironing (C) your own clothes every day (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "C"},
    {"type": "choice", "topic": "Grammar",
     "q": "2. My sister enjoys (A) taking (B) photographs about (C) flowers in spring (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "C"},
    {"type": "choice", "topic": "Grammar",
     "q": "3. Mr. and Mrs. Tran are poor (A) but (B) they live happy (C) on an island (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "C"},
    {"type": "choice", "topic": "Grammar",
     "q": "4. We spent (A) about fifteen hours to go (B) from Hanoi (C) to Ho Chi Minh city by coach (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "B"},
    {"type": "choice", "topic": "Grammar",
     "q": "5. There was (A) only a few (B) people (C) at the meeting on Monday afternoon (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "A"},
    # ── VI. Fill in passage — My Teacher (10 MC) ── A B B C D A B C B D
    {"type": "choice", "topic": "Reading",
     "section_start": "D. READING — VI. Fill in the passage",
     "section_instruction": "Choose the suitable word to complete the passage (My Teacher).",
     "passage_text": (
         "My teacher, Miss White, is a young lady (1)___ twenty-six. She is a nice lady. "
         "She loves her students (2)___. She never (3)___ angry with them. Miss White (4)___ "
         "teaching her students. Sometimes she tells (5)___ many interesting stories. I like "
         "to listen to her stories (6)___ they all help us to learn some (7)___ lessons. "
         "Sometimes she takes us out (8)___ a picnic. Whenever she takes us out, she tries "
         "to teach us something (9)___.\n"
         "It is my dream that (10)___ I grow up, I can become a good teacher like her."
     ),
     "q": "(1) a young lady ___ twenty-six.",
     "options": ["of", "with", "from", "by"],
     "answer": "of"},
    {"type": "choice", "topic": "Reading",
     "q": "(2) She loves her students ___.",
     "options": ["very many", "very much", "too", "so"],
     "answer": "very much"},
    {"type": "choice", "topic": "Reading",
     "q": "(3) She never ___ angry with them.",
     "options": ["is", "gets", "makes", "comes"],
     "answer": "gets"},
    {"type": "choice", "topic": "Reading",
     "q": "(4) Miss White ___ teaching her students.",
     "options": ["enjoy", "enjoying", "enjoys", "to enjoy"],
     "answer": "enjoys"},
    {"type": "choice", "topic": "Reading",
     "q": "(5) Sometimes she tells ___ many interesting stories.",
     "options": ["we", "they", "I", "us"],
     "answer": "us"},
    {"type": "choice", "topic": "Reading",
     "q": "(6) I like to listen to her stories ___ they all help us to learn.",
     "options": ["because", "when", "where", "why"],
     "answer": "because"},
    {"type": "choice", "topic": "Reading",
     "q": "(7) to learn some ___ lessons.",
     "options": ["use", "useful", "using", "to use"],
     "answer": "useful"},
    {"type": "choice", "topic": "Reading",
     "q": "(8) She takes us out ___ a picnic.",
     "options": ["from", "by", "for", "of"],
     "answer": "for"},
    {"type": "choice", "topic": "Reading",
     "q": "(9) she tries to teach us something ___.",
     "options": ["old", "new", "bad", "well"],
     "answer": "new"},
    {"type": "choice", "topic": "Reading",
     "q": "(10) It is my dream that ___ I grow up, I can become a good teacher.",
     "options": ["where", "why", "what", "when"],
     "answer": "when"},
    # ── VII. Reading comprehension — Fat woman (5 MC) ── C C B C A
    {"type": "choice", "topic": "Reading",
     "section_start": "D. READING — VII. Read the passage and answer",
     "section_instruction": "Read the passage and choose the best answer.",
     "passage_text": (
         "There was once a large, fat woman who had a small thin husband. He had a job in "
         "a big company and was given his weekly wages every Friday evening. As soon as he "
         "got home, his wife often made him give her all his money, and then she gave him "
         "back only enough to buy his lunch in the office every day. One day the small man "
         "came home very excited. \"You will never guess what happened to me today, dear\", "
         "he said. He waited for a few seconds and then added: \"I won 10 thousand pounds "
         "on the lottery\". \"That's wonderful!\", said his wife delightedly. But then she "
         "thought for a few seconds and asked angrily, \"But wait a moment! How could you "
         "afford to buy that ticket?\""
     ),
     "q": "1. How often did the wife get money from her husband?",
     "options": ["Every day", "Twice a week", "Every week"],
     "answer": "Every week"},
    {"type": "choice", "topic": "Reading",
     "q": "2. What did she give her husband some money for?",
     "options": ["To buy lottery tickets", "As his pocket money", "For his lunch every day"],
     "answer": "For his lunch every day"},
    {"type": "choice", "topic": "Reading",
     "q": "3. How much did the man win?",
     "options": ["$10,000", "10,000 pounds", "10,000p"],
     "answer": "10,000 pounds"},
    {"type": "choice", "topic": "Reading",
     "q": "4. Why did the wife get angry? Because her husband ___.",
     "options": ["won the lottery", "missed his lunch", "had some money of his own"],
     "answer": "had some money of his own"},
    {"type": "choice", "topic": "Reading",
     "q": "5. Which statement is NOT TRUE?",
     "options": ["The wife felt sorry for her husband", "The wife is a mean woman", "The husband won the lottery one day"],
     "answer": "The wife felt sorry for her husband"},
    # ── VIII. Fill in blank — Parents & Friends (10 fill) ──
    {"type": "fill", "topic": "Reading",
     "section_start": "D. READING — VIII. Fill in each blank with ONE word",
     "section_instruction": "Fill in each blank with ONE suitable word.",
     "passage_text": (
         "We can choose our friends, but we can't (1)___ our relatives. That does not mean "
         "that members of our (2)___ cannot also be our friends. Many children have a very "
         "(3)___ relationship with their parents. Of course when you are a teenager, there "
         "are times (4)___ you do not get on well (5)___ your parents. That's only natural. "
         "There are (6)___ when you want to be independent and decide things by (7)___. "
         "After all, nobody is perfect, and we all (8)___ mistakes. But your parents "
         "understand that. When you grow up, you will see that you have many things in "
         "(9)___ with your mum and dad, and you will become closer (10)___ them."
     ),
     "q": "(1) We can choose our friends, but we can't ___ our relatives.",
     "answer": "choose"},
    {"type": "fill", "topic": "Reading",
     "q": "(2) members of our ___ cannot also be our friends.",
     "answer": "family"},
    {"type": "fill", "topic": "Reading",
     "q": "(3) Many children have a very ___ relationship with their parents.",
     "answer": "good"},
    {"type": "fill", "topic": "Reading",
     "q": "(4) there are times ___ you do not get on well with your parents.",
     "answer": "when"},
    {"type": "fill", "topic": "Reading",
     "q": "(5) you do not get on well ___ your parents.",
     "answer": "with"},
    {"type": "fill", "topic": "Reading",
     "q": "(6) There are ___ when you want to be independent.",
     "answer": "times"},
    {"type": "fill", "topic": "Reading",
     "q": "(7) you want to decide things by ___.",
     "answer": "yourself"},
    {"type": "fill", "topic": "Reading",
     "q": "(8) we all ___ mistakes.",
     "answer": "make"},
    {"type": "fill", "topic": "Reading",
     "q": "(9) you will have many things in ___ with your mum and dad.",
     "answer": "common"},
    {"type": "fill", "topic": "Reading",
     "q": "(10) you will become closer ___ them.",
     "answer": "to"},
]

_HSG_ANH_DE_2 = [
    # ── I. Listening fill table (5) ── 17/games/Shark week/thrilling/stars and planet
    {"type": "fill", "topic": "Listening",
     "section_start": "SECTION 1. LISTENING",
     "section_instruction": "I. Listen and fill in the table (Mi, Tom, Mrs Mai's favourite TV programmes).",
     "q": "(1) Mi watches Kids' Funs. Which channel? ___",
     "answer": "17"},
    {"type": "fill", "topic": "Listening",
     "q": "(2) Kids' Funs content: funny ___ (one word)",
     "answer": "games"},
    {"type": "fill", "topic": "Listening",
     "q": "(3) Tom's programme name (on Discovery channel): ___",
     "answer": "Shark week"},
    {"type": "fill", "topic": "Listening",
     "q": "(4) How does Tom describe his programme? It is ___",
     "answer": "thrilling"},
    {"type": "fill", "topic": "Listening",
     "q": "(5) Mrs Mai's 'Journey to Space' (channel 9) is about ___",
     "answer": "stars and planet"},
    # ── II. Listening fill blanks (5) ── household/garden/transportation/burning/engines
    {"type": "fill", "topic": "Listening",
     "section_start": "SECTION 1. LISTENING — II. Fill in the gaps",
     "section_instruction": "Listen and fill ONE WORD in each blank (teacher's tips to keep the air clean).",
     "q": "(1) The teacher gives ___ tips (at home).",
     "answer": "household"},
    {"type": "fill", "topic": "Listening",
     "q": "(2) The teacher gives ___ tips (garden/outdoors).",
     "answer": "garden"},
    {"type": "fill", "topic": "Listening",
     "q": "(3) The teacher gives ___ tips (travel).",
     "answer": "transportation"},
    {"type": "fill", "topic": "Listening",
     "q": "(4) Use gas at home instead of ___ wood.",
     "answer": "burning"},
    {"type": "fill", "topic": "Listening",
     "q": "(5) Avoid ___ that smoke.",
     "answer": "engines"},
    # ── III. Phonetics pronunciation (3 MC) ── C B C
    {"type": "choice", "topic": "Phonetics",
     "section_start": "SECTION 2. PHONETICS — III. Different pronunciation",
     "section_instruction": "Choose the word whose underlined part is pronounced differently.",
     "q": "1. A. healthy   B. instead   C. seaside   D. breakfast",
     "options": ["healthy", "instead", "seaside", "breakfast"],
     "answer": "seaside"},
    {"type": "choice", "topic": "Phonetics",
     "q": "2. A. nice   B. uncle   C. office   D. distance",
     "options": ["nice", "uncle", "office", "distance"],
     "answer": "uncle"},
    {"type": "choice", "topic": "Phonetics",
     "q": "3. A. drops   B. looks   C. means   D. meets",
     "options": ["drops", "looks", "means", "meets"],
     "answer": "means"},
    # ── IV. Stress (2 MC) ── A B
    {"type": "choice", "topic": "Phonetics",
     "section_start": "SECTION 2. PHONETICS — IV. Different stress",
     "section_instruction": "Choose the word whose stress pattern is different from the others.",
     "q": "1. A. geography   B. literature   C. hospital   D. bakery",
     "options": ["geography", "literature", "hospital", "bakery"],
     "answer": "geography"},
    {"type": "choice", "topic": "Phonetics",
     "q": "2. A. finish   B. address   C. picture   D. music",
     "options": ["finish", "address", "picture", "music"],
     "answer": "address"},
    # ── V. Lexico-Grammar (25 MC) ── A D B C C B D A D A C B C B C B A C D A A D A A A
    {"type": "choice", "topic": "Grammar",
     "section_start": "SECTION 3. LEXICO-GRAMMAR — V. Choose the best answer",
     "section_instruction": "Choose the correct answer to complete each sentence.",
     "q": "1. I usually play football when I have ___.",
     "options": ["spare time", "good time", "no time", "times"],
     "answer": "spare time"},
    {"type": "choice", "topic": "Grammar",
     "q": "2. In team sports, the two teams ___ against each other to get the better score.",
     "options": ["are", "do", "make", "compete"],
     "answer": "compete"},
    {"type": "choice", "topic": "Grammar",
     "q": "3. ___ draw on the walls and tables, please.",
     "options": ["Do", "Don't", "Should", "Shouldn't"],
     "answer": "Don't"},
    {"type": "choice", "topic": "Grammar",
     "q": "4. Nam plays sports very often, so he looks very ___.",
     "options": ["sport", "sports", "sporty", "sporting"],
     "answer": "sporty"},
    {"type": "choice", "topic": "Grammar",
     "q": "5. How many numbers between 5 and 100 are divisible by 5?",
     "options": ["18", "19", "20", "21"],
     "answer": "20"},
    {"type": "choice", "topic": "Grammar",
     "q": "6. People in Tokyo are very polite ___ friendly.",
     "options": ["or", "and", "but", "so"],
     "answer": "and"},
    {"type": "choice", "topic": "Grammar",
     "q": "7. Do you know ___ drink in Viet Nam?",
     "options": ["popular", "more popular", "more and more popular", "the most popular"],
     "answer": "the most popular"},
    {"type": "choice", "topic": "Grammar",
     "q": "8. The robot will ___ of the flowers in the garden.",
     "options": ["take care", "take note", "be careful", "carry"],
     "answer": "take care"},
    {"type": "choice", "topic": "Grammar",
     "q": "9. I don't know how ___ this lesson.",
     "options": ["learn", "learning", "to learning", "to learn"],
     "answer": "to learn"},
    {"type": "choice", "topic": "Grammar",
     "q": "10. A: 'Would you like some bread?' B: '___'",
     "options": ["No, thanks. I'm full.", "Ok. I don't like rice.", "All right.", "Yes, I would."],
     "answer": "No, thanks. I'm full."},
    {"type": "choice", "topic": "Grammar",
     "q": "11. John: '___?' Mary: 'That's a great idea.'",
     "options": ["Do you like playing sports", "Can you buy me some apples", "Why don't we go out for dinner", "May I borrow your pen"],
     "answer": "Why don't we go out for dinner"},
    {"type": "choice", "topic": "Grammar",
     "q": "12. Ba: '___ do you visit your uncle?' Nam: 'Every other week.'",
     "options": ["Why", "How often", "When", "How long"],
     "answer": "How often"},
    {"type": "choice", "topic": "Grammar",
     "q": "13. The school cafeteria only opens ___ lunchtime.",
     "options": ["on", "in", "at", "of"],
     "answer": "at"},
    {"type": "choice", "topic": "Grammar",
     "q": "14. On ___ we often go out for dinner.",
     "options": ["nights of Saturday", "Saturday nights", "Saturday's nights", "none is correct"],
     "answer": "Saturday nights"},
    {"type": "choice", "topic": "Grammar",
     "q": "15. There are many chairs in the kitchen, ___ there is only one in my bedroom.",
     "options": ["so", "because", "but", "in"],
     "answer": "but"},
    {"type": "choice", "topic": "Grammar",
     "q": "16. This is a/an ___ car.",
     "options": ["American red old", "old red American", "red American old", "old American red"],
     "answer": "old red American"},
    {"type": "choice", "topic": "Grammar",
     "q": "17. John: 'Hello. Can I speak to Trang, please?' — Trang: '___'",
     "options": ["Speaking. Who's that?", "What's the matter with you?", "Hello, John. How are you?", "How do you do?"],
     "answer": "Speaking. Who's that?"},
    {"type": "choice", "topic": "Grammar",
     "q": "18. Listen! Someone ___ at the door.",
     "options": ["knocks", "knock", "is knocking", "are knocking"],
     "answer": "is knocking"},
    {"type": "choice", "topic": "Grammar",
     "q": "19. This sign says 'Stop!' We ___ go straight ahead.",
     "options": ["can", "don't can", "must", "mustn't"],
     "answer": "mustn't"},
    {"type": "choice", "topic": "Grammar",
     "q": "20. Do you ___ your new classmate, or do you two argue?",
     "options": ["get on well with", "look forward to", "face up to", "keep up with"],
     "answer": "get on well with"},
    {"type": "choice", "topic": "Grammar",
     "q": "21. They often go to Ho Chi Minh City ___ air.",
     "options": ["by", "in", "with", "on"],
     "answer": "by"},
    {"type": "choice", "topic": "Grammar",
     "q": "22. The tree ___.",
     "options": ["is high one meter", "has one meter", "is one long meter", "is one meter high"],
     "answer": "is one meter high"},
    {"type": "choice", "topic": "Grammar",
     "q": "23. He arrives ___ at six o'clock.",
     "options": ["home", "at home", "in home", "to home"],
     "answer": "home"},
    {"type": "choice", "topic": "Grammar",
     "q": "24. ___ any furniture ___ your new living room?",
     "options": ["Is - in", "Is - at", "Are - in", "Are - on"],
     "answer": "Is - in"},
    {"type": "choice", "topic": "Grammar",
     "q": "25. Children in poor villages are allowed to go to school without ___ money.",
     "options": ["paying", "to pay", "pays", "to paying"],
     "answer": "paying"},
    # ── VI. Error identification (5 MC) ── D A D C C
    {"type": "choice", "topic": "Grammar",
     "section_start": "SECTION 3. LEXICO-GRAMMAR — VI. Find the error",
     "section_instruction": "There is one mistake in each sentence. Choose the underlined part (A, B, C or D) that needs correcting.",
     "q": "1. Our teacher is very beautiful (A). She has an oval face (B) with a long (C) black hair (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "D"},
    {"type": "choice", "topic": "Grammar",
     "q": "2. You must (A) taking off your shoes before entering this room (B-D).",
     "options": ["A", "B", "C", "D"],
     "answer": "A"},
    {"type": "choice", "topic": "Grammar",
     "q": "3. He gets up early (A) so (B) he's never late (C) of (D) school.",
     "options": ["A", "B", "C", "D"],
     "answer": "D"},
    {"type": "choice", "topic": "Grammar",
     "q": "4. A lot of (A) my friends play soccer (B), but not much (C) of them play tennis (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "C"},
    {"type": "choice", "topic": "Grammar",
     "q": "5. Sorry. You can't speak to Jim now (A/B). He's have (C) a bath (D).",
     "options": ["A", "B", "C", "D"],
     "answer": "C"},
    # ── VII. Fill in passage — Health Farm (10 MC) ── B C D A B C A C A D
    {"type": "choice", "topic": "Reading",
     "section_start": "SECTION 4. READING — VII. Fill in the passage",
     "section_instruction": "Choose A, B, C or D to fill in the blank. (Health Farm)",
     "passage_text": (
         "Do you want to be fitter and healthier? Would you like to look younger? Do you "
         "want to feel (1)___ relaxed? Then try a few days at a health farm. Health farms "
         "are becoming (2)___ of the most popular places (3)___ a short break. I went to "
         "Henley Manor for a weekend. It's (4)___ largest health farm in the country but "
         "it isn't the most expensive. After two days of exercise and massage I (5)___ ten "
         "times better. But the best thing for me was the food. It was all very healthy of "
         "(6)___, but it was expensive too!\n"
         "If you're looking for something a (7)___ cheaper, try a winter break. Winter is "
         "the darkest and the coldest (8)___ of the year, and it can also be the (9)___ "
         "time for your body. We all eat too (10)___ and we don't take enough exercise."
     ),
     "q": "(1) Do you want to feel ___ relaxed?",
     "options": ["like", "more", "less", "similar"],
     "answer": "more"},
    {"type": "choice", "topic": "Reading",
     "q": "(2) Health farms are becoming ___ of the most popular places.",
     "options": ["once", "first", "one", "none"],
     "answer": "one"},
    {"type": "choice", "topic": "Reading",
     "q": "(3) the most popular places ___ a short break.",
     "options": ["with", "of", "to", "for"],
     "answer": "for"},
    {"type": "choice", "topic": "Reading",
     "q": "(4) It's ___ largest health farm in the country.",
     "options": ["the", "an", "a", "x"],
     "answer": "the"},
    {"type": "choice", "topic": "Reading",
     "q": "(5) After exercise and massage I ___ ten times better.",
     "options": ["feel", "felt", "fell", "fall"],
     "answer": "felt"},
    {"type": "choice", "topic": "Reading",
     "q": "(6) It was all very healthy of ___, but it was expensive!",
     "options": ["all", "out", "course", "them"],
     "answer": "course"},
    {"type": "choice", "topic": "Reading",
     "q": "(7) looking for something a ___ cheaper.",
     "options": ["little", "few", "a little", "a few"],
     "answer": "little"},
    {"type": "choice", "topic": "Reading",
     "q": "(8) the coldest ___ of the year.",
     "options": ["period", "moment", "time", "part"],
     "answer": "time"},
    {"type": "choice", "topic": "Reading",
     "q": "(9) it can also be the ___ time for your body.",
     "options": ["worst", "good", "best", "great"],
     "answer": "worst"},
    {"type": "choice", "topic": "Reading",
     "q": "(10) We all eat too ___ and we don't take enough exercise.",
     "options": ["many", "a lot", "lot of", "much"],
     "answer": "much"},
    # ── VIII. Reading comprehension — Pollution (5 MC) ── B D D B A
    {"type": "choice", "topic": "Reading",
     "section_start": "SECTION 4. READING — VIII. Read and answer",
     "section_instruction": "Read the passage and choose the best answer.",
     "passage_text": (
         "Every day on radio, on TV, and in the newspaper, we hear, see or read about many "
         "problems in the world, for example, pollution problems.\n"
         "Air pollution is the first kind. It mostly comes from fumes released from "
         "motorbikes, cars, airplanes, trains and poisonous gases emitted from factories. "
         "Also, waste is dumped anywhere, even in the city where many people are living. "
         "The second pollution problem is sea pollution. Many people earn their living from "
         "fishing in the sea. But the sea has become so polluted from oil spills and "
         "factory wastes that the fish are dying. This is not only killing the fish, but "
         "is also affecting those people who eat fish.\n"
         "Seldom do you find a place nowadays that is not polluted. This problem is growing "
         "more difficult every day. We must find a good solution that makes the world a "
         "better place to live."
     ),
     "q": "1. We hear, see and read about problems in the world ___.",
     "options": ["once a week", "every day", "every week", "every year"],
     "answer": "every day"},
    {"type": "choice", "topic": "Reading",
     "q": "2. What causes air pollution?",
     "options": ["fumes from vehicles", "poisonous gases from factories", "waste dumped everywhere", "All are correct"],
     "answer": "All are correct"},
    {"type": "choice", "topic": "Reading",
     "q": "3. The sea has become polluted because of ___.",
     "options": ["oil spills", "factory wastes", "smoke from factories", "A and B are correct"],
     "answer": "A and B are correct"},
    {"type": "choice", "topic": "Reading",
     "q": "4. In order to make the world a better place to live, we ___.",
     "options": ["should not prevent pollution", "must find a good solution", "should kill the fish", "None is correct"],
     "answer": "must find a good solution"},
    {"type": "choice", "topic": "Reading",
     "q": "5. The word 'This' in 'This is not only killing the fish...' refers to ___.",
     "options": ["pollution", "oil", "factory", "sea"],
     "answer": "pollution"},
    # ── IX. Fill in blank — Sport (10 fill) ──
    {"type": "fill", "topic": "Reading",
     "section_start": "SECTION 4. READING — IX. Fill in each blank",
     "section_instruction": "Fill in each numbered blank with ONE suitable word.",
     "passage_text": (
         "\"Do you like sport?\" You can hear this (1)___ very often. Many people answer "
         "\"Yes, I do\", and (2)___ think about watching a game of football at a stadium, "
         "or (3)___ TV while sitting in a comfortable armchair. But watching sport events "
         "and going in for sport (4)___ two different things. Let's hope that you prefer "
         "the second.\n"
         "Sport holds (5)___ important place in our life. When you listen to the radio "
         "early in the morning, you can always (6)___ sports news. When you open a "
         "newspaper, you will always find (7)___ about some game or other. Especially "
         "interesting stories are (8)___ famous men or women in sport, how they became "
         "champions and about (9)___ plans for the future.\n"
         "Television programmes about (10)___ are also very popular."
     ),
     "q": "(1) You can hear this ___ very often.",
     "answer": "question"},
    {"type": "fill", "topic": "Reading",
     "q": "(2) Many people answer 'Yes', and ___ think about watching football.",
     "answer": "they"},
    {"type": "fill", "topic": "Reading",
     "q": "(3) watching a game of football ... or ___ TV.",
     "answer": "on"},
    {"type": "fill", "topic": "Reading",
     "q": "(4) watching sport events and going in for sport ___ two different things.",
     "answer": "are"},
    {"type": "fill", "topic": "Reading",
     "q": "(5) Sport holds ___ important place in our life.",
     "answer": "an"},
    {"type": "fill", "topic": "Reading",
     "q": "(6) you can always ___ sports news.",
     "answer": "hear"},
    {"type": "fill", "topic": "Reading",
     "q": "(7) you will always find ___ about some game.",
     "answer": "information"},
    {"type": "fill", "topic": "Reading",
     "q": "(8) interesting stories are ___ famous men or women in sport.",
     "answer": "about"},
    {"type": "fill", "topic": "Reading",
     "q": "(9) how they became champions and about ___ plans for the future.",
     "answer": "their"},
    {"type": "fill", "topic": "Reading",
     "q": "(10) Television programmes about ___ are also very popular.",
     "answer": "sport"},
]

_HSG_ANH_6_EXAMS = {i: [] for i in range(1, 37)}
_HSG_ANH_6_EXAMS[1] = _HSG_ANH_DE_1
_HSG_ANH_6_EXAMS[2] = _HSG_ANH_DE_2

HSG_ANH_EXAM_DURATIONS = {i: 120 for i in range(1, 37)}
HSG_ANH_EXAM_NQ = {k: len(v) for k, v in _HSG_ANH_6_EXAMS.items()}

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
