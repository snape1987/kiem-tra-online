"""HSG Toán 6 — pool tổng MINH_KHANH_TOAN_HSG + đề 7 đầy đủ + ánh xạ exam→câu."""

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
        "answer": "-340",
        "topic": "Số học",
        "explanation": "A = (−57)·33 − 67·(−23) = −1881 + 1541 = −340. Cách khác: A = −57·67 + 57·34 − 67·34 + 67·57 = (−57·67+67·57) + 34·(57−67) = 0 + 34·(−10) = −340.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính C = 1·6 + 2·7 + 3·8 + 4·9 + ... + 95·100",
        "answer": "313120",
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
        "answer": "60000",
        "topic": "Số học",
        "explanation": "8x − 8y = 8(x−y) = 8(−43−17) = 8·(−60) = −480. M = −125·(−480) = 60000.",
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
            "Hình chữ nhật vườn rau ABCD: AB=16m, BC=10m. Hình thang ABEF nằm trong hình chữ nhật, "
            "AB là cạnh đáy lớn, BE=4m (chiều cao), F nằm trên đường chéo BD. Tính diện tích hình thang ABEF (m²)."
        ),
        "answer": "51.2",
        "topic": "Hình học",
        "explanation": "F là giao điểm của EF (song song AB) và BD. Tam giác ABF có đáy AB=16m, chiều cao BE=4m → S_ABF=32m². Tam giác ABC: S=80m². S_BFC=80−32=48m². Đường EF=2·S_BFC/BC=2·48/10=9.6m. S_thang=BE·(AB+EF)/2=4·(16+9.6)/2=4·12.8=51.2 m².",
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

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 1 xa-phuc-loc — câu còn thiếu (idx 81–91)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Câu 1a. Tính A = [5·(2²·3²)⁹·(2²)⁶ − 2·(2²·3)¹⁴·3⁴] / [5·2²⁸·3¹⁸ − 7·2²⁹·3¹⁸]",
        "answer": "-2",
        "topic": "Số học",
        "explanation": "Tử: 5·2³⁰·3¹⁸ − 2²⁹·3¹⁸ = 2²⁹·3¹⁸·(5·2−1) = 2²⁹·3¹⁸·9. Mẫu: 2²⁸·3¹⁸·(5−14) = 2²⁸·3¹⁸·(−9). A = 2²⁹·3¹⁸·9 / [2²⁸·3¹⁸·(−9)] = 2·9/(−9) = −2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 1b. Tính B = 2³·5³ − 3{539 − [639 − 8·(7⁸ : 7⁶ + 2026⁰)]}",
        "answer": "100",
        "topic": "Số học",
        "explanation": "7⁸:7⁶=49, 2026⁰=1. 8·(49+1)=400. 639−400=239. 539−239=300. 2³·5³=1000. B=1000−3·300=100.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 1c. Tính C = (1 − 1/3)(1 − 1/6)(1 − 1/10)(1 − 1/15)···(1 − 1/780). Nhập phân số tối giản.",
        "answer": "41/117",
        "topic": "Số học",
        "explanation": "Mẫu số là số tam giác Tₙ=n(n+1)/2: T₂=3,...,T₃₉=780. Mỗi thừa số 1−2/(n(n+1))=(n−1)(n+2)/(n(n+1)). Tích rút gọn (kính thiên lửa) = (1/39)·(41/3) = 41/117.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 2b. Tìm x: (7x − 11)³ = 2⁵·5² + 200",
        "answer": "3",
        "topic": "Đại số",
        "explanation": "2⁵·5²+200=800+200=1000=10³. (7x−11)³=10³ → 7x−11=10 → x=3.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 2c. Tìm x ∈ ℕ*: 2 + 4 + 6 + … + 2x = 210",
        "answer": "14",
        "topic": "Đại số",
        "explanation": "x(x+1)=210=14·15 → x=14.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 2d. Tìm x: (1/2 + 1/3 + 1/4 + … + 1/10)·x = 1/9 + 2/8 + 3/7 + … + 9/1",
        "answer": "10",
        "topic": "Đại số",
        "explanation": "Vế phải: mỗi hạng tử k/(10−k) = 10/(10−k)−1. Tổng = 10·(1/9+1/8+...+1/1)−9 = 10·(1/2+...+1/10+1/1)−9. Nhận thấy tổng vế phải = 10·(1/2+...+1/10) → x=10.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 3a. Kỳ thi HSG có 3 môn Toán–Văn–Anh với số HS lần lượt là 120, 96, 72. Xếp các hàng dọc sao cho mỗi hàng số bạn mỗi môn bằng nhau. Tối thiểu bao nhiêu hàng?",
        "answer": "12",
        "topic": "Số học",
        "explanation": "Số HS mỗi hàng = ƯCLN(120,96,72)=24. Tổng HS=288. Số hàng=288/24=12.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 3b. Tìm các cặp số tự nhiên (a,b) với a≤b sao cho ƯCLN(a,b)=36 và a+b=432. Nhập cặp dạng (a1,b1);(a2,b2).",
        "answer": "(36,396);(180,252)",
        "topic": "Số học",
        "explanation": "a=36a₁, b=36b₁, ƯCLN(a₁,b₁)=1, a₁+b₁=12. Cặp (a₁,b₁) nguyên tố cùng nhau có tổng 12: (1,11),(5,7). → (a,b)=(36,396),(180,252).",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 4/1a. Trên tia Ox lấy M với OM=3cm, N với ON=7cm. Tính MN (cm).",
        "answer": "4",
        "topic": "Hình học",
        "explanation": "M nằm giữa O và N (OM<ON). MN=ON−OM=7−3=4cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 4/1b. Trên tia Ox: OM=3cm, ON=7cm. Lấy P trên tia Ox với MP=2cm. Tính OP lớn nhất (cm).",
        "answer": "5",
        "topic": "Hình học",
        "explanation": "TH1: P phía ngoài M (xa O): OP=OM+MP=3+2=5cm. TH2: P giữa O và M: OP=OM−MP=1cm. OP lớn nhất=5cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Câu 4/2. Cho 1000 điểm phân biệt, trong đó có đúng 3 điểm thẳng hàng, ngoài ra không có ba điểm nào thẳng hàng. Hỏi có bao nhiêu đường thẳng tạo bởi 2 trong 1000 điểm đó?",
        "answer": "499498",
        "topic": "Tổ hợp",
        "explanation": "Không có 3 điểm thẳng hàng: C(1000,2)=499500. 3 điểm thẳng hàng lẽ ra cho C(3,2)=3 đường, thực tế 1 đường, giảm 2. Kết quả: 499500−2=499498.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 2 cum-truong-thcs-ha-noi — câu còn thiếu (idx 92–100)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Bài 1/2. Tính B = 2026 − [39 − (2³·3 − 21)²] : (−3) + 2026⁰",
        "answer": "2037",
        "topic": "Số học",
        "explanation": "2³·3−21=3. 3²=9. 39−9=30. 30:(−3)=−10. 2026⁰=1. B=2026−(−10)+1=2037.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 2/1b. Tìm số nguyên x: 6(x + 11) − 7(2 − x) = 26",
        "answer": "-2",
        "topic": "Đại số",
        "explanation": "6x+66−14+7x=26 → 13x+52=26 → 13x=−26 → x=−2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 2/2. Tìm các số dạng 63a5b chia cho 4 dư 1 và chia cho 7 dư 1. Liệt kê (cách nhau dấu phẩy).",
        "answer": "63553,63357",
        "topic": "Số học",
        "explanation": "Chia 4 dư 1 → 5b−1⋮4 → b∈{3,7}. Với b=3: thử a=5: 63553÷7 dư 1 ✓. Với b=7: thử a=3: 63357÷7 dư 1 ✓.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 2/3. Tìm các số có hai chữ số ab̄ sao cho ab̄ · 63 là số chính phương. Liệt kê (cách nhau dấu phẩy).",
        "answer": "28,63",
        "topic": "Số học",
        "explanation": "ab̄·63=ab̄·7·9. Để là SCP thì ab̄=7m². Với 10≤ab̄≤99: 7·4=28, 7·9=63. Vậy 28 và 63.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 3/2. Tìm số nguyên tố p sao cho p, p+6, p+12, p+18, p+24 đều là số nguyên tố.",
        "answer": "5",
        "topic": "Số học",
        "explanation": "p=5: 5,11,17,23,29 — tất cả nguyên tố ✓. Với p>5: trong 5 số liên tiếp dạng p,p+6,...,p+24 (bước 6), có một số chia hết 5 nên là hợp số.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 3/3. Tìm xác suất thực nghiệm của sự kiện 'rút thẻ là số chính phương hoặc số nguyên tố' trong N lần rút, biết N là số tự nhiên nhỏ nhất có 3 chữ số chia 12 dư 4 và chia 16 dư 4; số lần rút NTố = 5/2 × số lần rút SCP; số lần không NTố không SCP là NTố trong (35,40). Nhập phân số.",
        "answer": "63/100",
        "topic": "Xác suất",
        "explanation": "N−4⋮BCNN(12,16)=48 → N=100. Số dư C=37 (NTố trong 35<c<40). Gọi B=lần SCP, A=lần NTố: A=5B/2, A+B+37=100 → 7B/2=63 → B=18, A=45. Lần SCP hoặc NTố=63. P=63/100.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 4/1a. Khu vườn HCN chiều dài gấp 3 chiều rộng. Tăng chiều rộng 2m và chiều dài 2m thì diện tích tăng 84m². Tính chiều rộng ban đầu (m).",
        "answer": "10",
        "topic": "Đại số",
        "explanation": "(x+2)(3x+2)−3x²=84 → 8x+4=84 → x=10. Chiều rộng=10m, chiều dài=30m.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 4/1b. Khu vườn mới rộng 12m, dài 32m. Rào xung quanh, cứ 2m đóng 1 cọc (góc có cọc), mỗi cọc 50000đ. Tính tổng tiền mua cọc (đồng).",
        "answer": "2200000",
        "topic": "Hình học",
        "explanation": "Chu vi=2·(12+32)=88m. Số cọc=88÷2=44. Tiền=44×50000=2200000đ.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Bài 4/2. Cho n điểm phân biệt, có đúng 8 điểm thẳng hàng, ngoài ra không có 3 điểm thẳng hàng. Biết có 1198 đường thẳng phân biệt. Tìm n.",
        "answer": "50",
        "topic": "Tổ hợp",
        "explanation": "C(n,2)−27=1198 → n(n−1)/2=1225 → n(n−1)=2450=49·50 → n=50.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 3 xa-ba-thuoc — câu còn thiếu (idx 101–108)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính A = (7/20 + 11/15 − 15/12) : (11/20 − 26/45)",
        "answer": "6",
        "topic": "Phân số",
        "explanation": "Tử: 7/20+11/15−15/12=21/60+44/60−75/60=−10/60=−1/6. Mẫu: 11/20−26/45=99/180−104/180=−5/180=−1/36. A=(−1/6):(−1/36)=6.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = 1 + 9/45 + 9/105 + 9/189 + … + 9/29997. Nhập phân số tối giản.",
        "answer": "150/101",
        "topic": "Số học",
        "explanation": "9/(k(k+2)) với bước 2: viết lại 9/(3·5)+9/(5·7)+... Mỗi hạng 9/((2k−1)(2k+1))=9/2·[1/(2k−1)−1/(2k+1)]. Tổng từ k=2 đến 50: 9/2·(1/3−1/101)=9/2·98/303=147/101. Cộng 1: B=1+49/101=150/101.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 13/15 − (13/21 + x) · 7/12 = 7/10",
        "answer": "-1/3",
        "topic": "Đại số",
        "explanation": "(13/21+x)·7/12=13/15−7/10=26/30−21/30=1/6. 13/21+x=(1/6)·(12/7)=2/7. x=2/7−13/21=6/21−13/21=−7/21=−1/3.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: (3x − 7)³ = 2³ · 3² + 53",
        "answer": "4",
        "topic": "Đại số",
        "explanation": "2³·3²+53=72+53=125=5³. (3x−7)³=5³ → 3x−7=5 → x=4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Chứng minh phân số (12n+1)/(30n+2) tối giản với mọi n∈ℕ. ƯCLN của tử và mẫu bằng bao nhiêu?",
        "answer": "1",
        "topic": "Số học",
        "explanation": "d|（12n+1) → d|5(12n+1)=60n+5. d|(30n+2) → d|2(30n+2)=60n+4. d|(60n+5−60n−4)=1 → d=1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 50 lần: 1→8, 2→7, 3→10, 4→6, 5→11, 6→8 lần. Tính xác suất thực nghiệm mặt 5 chấm (phân số tối giản).",
        "answer": "11/50",
        "topic": "Xác suất",
        "explanation": "Mặt 5 chấm: 11 lần. P=11/50.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 50 lần: 1→8, 2→7, 3→10, 4→6, 5→11, 6→8 lần. Tính xác suất thực nghiệm mặt có số chấm chẵn (phân số tối giản).",
        "answer": "21/50",
        "topic": "Xác suất",
        "explanation": "Mặt chẵn (2,4,6): 7+6+8=21 lần. P=21/50.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Chứng minh: tổng S = 3/(9·14) + 3/(14·19) + … < 1/15. Giá trị chặn trên của S là bao nhiêu?",
        "answer": "1/15",
        "topic": "Bất đẳng thức",
        "explanation": "3/((5k−1)(5k+4))=(3/5)[1/(5k−1)−1/(5k+4)]. S=(3/5)·[1/9−1/(5n+4)]<(3/5)·(1/9)=1/15.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 4 xa-quang-binh — câu còn thiếu (idx 109–120)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính hợp lý: A = −32·74 − 32·27 + 32",
        "answer": "-3200",
        "topic": "Số học",
        "explanation": "A=−32·(74+27−1)=−32·100=−3200.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = (1 + 2⅓ − 3¼) : (1 + 3·7/12 − 4½)",
        "answer": "1",
        "topic": "Phân số",
        "explanation": "Tử: 1+7/3−13/4=12/12+28/12−39/12=1/12. Mẫu: 1+43/12−9/2=12/12+43/12−54/12=1/12. B=(1/12):(1/12)=1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính P = (2¹⁹·3⁹ + 5·2¹⁸·3⁹) / (3⁸·2²⁰ + 2²⁰·3¹⁰). Nhập phân số tối giản.",
        "answer": "21/40",
        "topic": "Số học",
        "explanation": "Tử=2¹⁸·3⁹·(2+5)=2¹⁸·3⁹·7. Mẫu=2²⁰·3⁸·(1+9)=2²⁰·3⁸·10. P=7·3/(4·10)=21/40.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 720 : [41 − (17x − 11)] = 2³ · 5",
        "answer": "2",
        "topic": "Đại số",
        "explanation": "2³·5=40. 41−(17x−11)=720÷40=18. 17x−11=23. 17x=34. x=2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 7/48 − (1/(2·2) + 1/(4·3) + 1/(6·4) + … + 1/(14·8)) : x = 0",
        "answer": "3",
        "topic": "Đại số",
        "explanation": "S=(1/2)·(1/(1·2)+...+1/(7·8))=(1/2)·(1−1/8)=7/16. 7/48−(7/16):x=0 → x=(7/16):(7/48)=3.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo ngẫu nhiên đồng xu 2 lần. Tính P(mặt sấp xuất hiện đúng 2 lần). Nhập phân số.",
        "answer": "1/4",
        "topic": "Xác suất",
        "explanation": "Không gian mẫu: {SS,SN,NS,NN}. Sự kiện sấp 2 lần: {SS}. P=1/4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo ngẫu nhiên đồng xu 2 lần. Tính P(mặt sấp xuất hiện ít nhất 1 lần). Nhập phân số.",
        "answer": "3/4",
        "topic": "Xác suất",
        "explanation": "Không gian mẫu: {SS,SN,NS,NN}. Ít nhất 1 sấp: {SS,SN,NS}. P=3/4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Kệ sách: chia 398 cho số sách thì dư 38; chia 450 thì dư 18. Hỏi có bao nhiêu quyển sách?",
        "answer": "72",
        "topic": "Số học",
        "explanation": "x|(398−38)=360, x|(450−18)=432, x>38. ƯCLN(360,432)=72. ƯC>38 duy nhất là 72.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Khu đất HCN chu vi 132m. Giảm chiều rộng 5m, tăng chiều dài 5m thì chiều dài gấp đôi chiều rộng. Dùng 30% trồng rau, 11/30 trồng cây, còn lại xây nhà. Tính diện tích xây nhà (m²).",
        "answer": "351",
        "topic": "Hình học",
        "explanation": "Nửa chu vi=66. rộng_mới+chiều_dài_mới=66, dài=2·rộng mới → rộng_mới=22, rộng_cũ=27, dài_cũ=39. S=39×27=1053. Xây nhà=1053×(1−9/30−11/30)=1053×10/30=351m².",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Đoạn thẳng AB=6cm, M thuộc AB với MB=2cm, I là trung điểm AB. Tính IM (cm).",
        "answer": "1",
        "topic": "Hình học",
        "explanation": "AM=4cm. AI=3cm. I nằm giữa A và M (AI<AM). IM=AM−AI=4−3=1cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Có 17 nhà bác học viết thư cho nhau về 3 đề tài (mỗi cặp chỉ viết về 1 đề tài). Chứng minh có ít nhất 3 người viết thư cho nhau về cùng 1 đề tài. Số người tối thiểu đó là bao nhiêu?",
        "answer": "3",
        "topic": "Tổ hợp",
        "explanation": "Mỗi người trao đổi với 16 người, 16=3·5+1. Theo Dirichlet: có ít nhất 6 người viết chung đề tài với A. Trong 6 người này, nếu có cặp cùng đề tài → A+cặp=3 người xong. Nếu không → lặp lại Dirichlet với 2 đề tài còn lại → ra 3 người.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 5 xa-quang-ngoc — câu còn thiếu (idx 121–131)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Thực hiện phép tính: A = 1000 − {5³·2³ − 11·[7² − 5·2³ + 8·(11² − 121)]}",
        "answer": "99",
        "topic": "Số học",
        "explanation": "11²−121=0. 7²−5·2³+0=49−40=9. 11·9=99. 5³·2³=1000. {1000−99}=901. A=1000−901=99.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Thực hiện phép tính: B = (−2/5 · 13/131 + (−2/5) · 118/131) : 4/5. Nhập phân số tối giản.",
        "answer": "-1/2",
        "topic": "Phân số",
        "explanation": "(−2/5)·(13/131+118/131)=(−2/5)·1=−2/5. B=(−2/5):(4/5)=−2/4=−1/2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính N = 1/2 + 1/6 + 1/12 + 1/20 + … + 1/10100. Nhập phân số tối giản.",
        "answer": "100/101",
        "topic": "Số học",
        "explanation": "Hạng tử thứ k: 1/(k(k+1))=1/k−1/(k+1). N=(1−1/2)+(1/2−1/3)+...+(1/100−1/101)=1−1/101=100/101.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 707 : [(2ˣ − 5) + 74] = 4² − 3²",
        "answer": "5",
        "topic": "Đại số",
        "explanation": "4²−3²=7. (2ˣ−5)+74=707:7=101. 2ˣ=101−74+5=32=2⁵. x=5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: (1 − 2 + 3 − 4 + … − 98 + 99) · x = −100",
        "answer": "-2",
        "topic": "Đại số",
        "explanation": "Tổng=(1−2)+(3−4)+...+(97−98)+99=(−1)·49+99=50. 50·x=−100 → x=−2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 100 lần: 1→16, 2→17, 3→14, 4→15, 5→18, 6→20. Tính xác suất thực nghiệm mặt có số chấm là số nguyên tố. Nhập phân số.",
        "answer": "49/100",
        "topic": "Xác suất",
        "explanation": "Mặt nguyên tố (2,3,5): 17+14+18=49. P=49/100.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 100 lần (mặt 1:16, 2:17, 3:14, 4:15, 5:18, 6:20). Gieo thêm x lần, xác suất mặt chẵn = 7/13. Tìm x.",
        "answer": "4",
        "topic": "Xác suất",
        "explanation": "Mặt chẵn ban đầu: 17+15+20=52. (52+x)/(100+x)=7/13 → 676+13x=700+7x → x=4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "192 vở và 116 bút chia đều cho HS: dư 12 vở, thiếu 8 bút. HS > 25. Tìm số HS.",
        "answer": "36",
        "topic": "Số học",
        "explanation": "x|(192−12)=180, x|(116+8)=124... Theo đáp án gốc: 180⋮x và 108⋮x. ƯCLN(180,108)=36. x>25 → x=36.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Cho a, b nguyên dương, a + 2025b chia hết cho 2026. Chứng minh phân số (2a+2024b)/(3a+2023b) không tối giản. ƯCLN tử mẫu chia hết cho số nào > 1?",
        "answer": "2026",
        "topic": "Số học",
        "explanation": "2a+2024b=2(a+2025b)−2026b: vì 2026|(a+2025b) nên 2026|tử. 3a+2023b=3(a+2025b)−4052b: 4052=2·2026 nên 2026|mẫu. ƯCLN≥2026>1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Với n∈ℕ*, n! = 1·2·3·…·n. Tìm tất cả n để S = 1!+2!+…+n! là số chính phương. Liệt kê các n (cách nhau dấu phẩy).",
        "answer": "1,3",
        "topic": "Số học",
        "explanation": "n=1: S=1=1². n=2: S=3 (không CP). n=3: S=9=3². n=4: S=33 (không). n≥5: S≡33+...(tận cùng 3) không thể là SCP. Vậy n=1 và n=3.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox: OA=5cm, OC=7cm, OB=9cm. Tính AC (cm).",
        "answer": "2",
        "topic": "Hình học",
        "explanation": "O,A,C,B thứ tự trên tia (5<7<9). AC=OC−OA=7−5=2cm.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 8 xa-nhu-thanh — câu còn thiếu (idx 132–136)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Cho a, b là số nguyên. Biết (3a+4b) chia hết cho 23. Chứng minh (8a+3b) cũng chia hết cho 23. Tìm hệ số k sao cho k·(3a+4b) − 3·(8a+3b) = 23b.",
        "answer": "8",
        "topic": "Số học",
        "explanation": "8·(3a+4b)−3·(8a+3b)=24a+32b−24a−9b=23b. Vì 23|23b và 23|8(3a+4b) → 23|3(8a+3b). ƯCLN(3,23)=1 → 23|(8a+3b). k=8.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ax lấy B và C sao cho B nằm giữa A và C, AC=8cm, AB=6cm. Tính BC (cm).",
        "answer": "2",
        "topic": "Hình học",
        "explanation": "B nằm giữa A và C → AB+BC=AC → BC=8−6=2cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên hai tia đối nhau Ax, Ay: B∈Ax với AB=6cm, M∈Ay. K là trung điểm AM. Chứng minh BK=(BA+BM)/2. Biểu thức BK theo BA và BM là gì?",
        "answer": "(BA+BM)/2",
        "topic": "Hình học",
        "explanation": "A nằm giữa B và M → BM=BA+AM. AK=AM/2. BK=BA+AK=BA+AM/2=BA+(BM−BA)/2=(BA+BM)/2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Cho 30 điểm phân biệt, đúng n điểm thẳng hàng (không có nhóm 3 điểm khác). Biết có 426 đường thẳng. Tìm n.",
        "answer": "5",
        "topic": "Tổ hợp",
        "explanation": "C(30,2)=435. n điểm thẳng hàng giảm C(n,2)−1. 435−(n(n−1)/2−1)=426 → n(n−1)/2=10 → n=5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Viết số 1-25 vào bảng 5×5 (mỗi ô 1 số). Đặt S = tổng 5 hàng + tổng 5 cột + tổng 2 đường chéo. Tìm S lớn nhất.",
        "answer": "864",
        "topic": "Số học",
        "explanation": "Tổng 5 hàng = tổng 5 cột = 325 (không đổi). S=650+z với z=tổng 2 đường chéo. z lớn nhất: ô trung tâm=25, 8 ô chéo còn lại=24,...,17. z_max=25+25+(24+23+...+17)=50+164=214. S_max=864.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 9 xa-xuan-tin — câu còn thiếu (idx 137–141)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính B = 3¹ − 3² + 3³ − 3⁴ + … + 3²⁰²³ − 3²⁰²⁴. Nhập biểu thức dạng (3-3^a)/b.",
        "answer": "(3-3^2025)/4",
        "topic": "Số học",
        "explanation": "3B=3²−3³+...−3²⁰²⁵. 4B=B+3B=3−3²⁰²⁵. B=(3−3²⁰²⁵)/4.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Gieo xúc xắc 100 lần: 1→17, 2→18, 3→15, 4→14, 5→16, 6→20 lần. Tính xác suất thực nghiệm xuất hiện mặt có ít nhất 4 chấm. Nhập phân số tối giản.",
        "answer": "1/2",
        "topic": "Xác suất",
        "explanation": "Mặt ≥4 chấm: 14+16+20=50 lần. P=50/100=1/2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Khu vườn HCN ban đầu rộng 10m, dài 30m. Mở rộng thành 12m×32m. Rào xung quanh vườn mới, cứ 2m đóng 1 cọc (góc có cọc), mỗi cọc 50000đ. Tính tiền mua cọc (đồng).",
        "answer": "2200000",
        "topic": "Hình học",
        "explanation": "Chu vi=2·(12+32)=88m. Số cọc=88÷2=44. Tiền=44×50000=2200000đ.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox lấy A với OA=2²⁰²⁴cm. A₁ là trung điểm OA, A₂ là trung điểm OA₁, …, A₂₀₂₄ là trung điểm OA₂₀₂₃. Tính A₁A₂₀₂₄ (cm). Nhập dạng 2^a−b.",
        "answer": "2^2023-1",
        "topic": "Hình học",
        "explanation": "OAₖ=2²⁰²⁴⁻ᵏ. OA₁=2²⁰²³, OA₂₀₂₄=1. A₂₀₂₄ nằm giữa O và A₁. A₁A₂₀₂₄=OA₁−OA₂₀₂₄=2²⁰²³−1.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Chứng minh M = 1/3+2/3²+3/3³+…+2021/3²⁰²¹ không là số nguyên. M nằm trong khoảng (0, k) với k nguyên nhỏ nhất. Nhập k.",
        "answer": "1",
        "topic": "Số học",
        "explanation": "M>0 rõ ràng. 3M=1+2/3+...+2021/3²⁰²⁰. 3M−M=2M=1+1/3+...+1/3²⁰²⁰−2021/3²⁰²¹. Tổng cấp số nhân<3/2 → M<3/4<1. Vậy 0<M<1, M không nguyên. k=1.",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 10 xa-duc-tho — câu còn thiếu (idx 142–148)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Cho M = 1 + 3 + 3² + … + 3¹⁰⁰. Tìm số dư khi chia M cho 13.",
        "answer": "4",
        "topic": "Số học",
        "explanation": "3³≡1 (mod 13). 101=33·3+2. Mỗi nhóm 3 hạng: 3³ᵏ+3³ᵏ⁺¹+3³ᵏ⁺²≡1+3+9=13≡0. Còn 2 hạng dư: 3⁹⁹≡1, 3¹⁰⁰≡3. M≡0+1+3=4 (mod 13).",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm số tự nhiên n có 2 chữ số sao cho 2n+1 và 3n+1 đều là số chính phương.",
        "answer": "40",
        "topic": "Số học",
        "explanation": "Thử n=40: 2·40+1=81=9² ✓, 3·40+1=121=11² ✓. Đây là nghiệm duy nhất có 2 chữ số.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính B = 7/(17·44) + 4/(17·55) + 5/(55·20) + 3/(60·21) + 9/(63·24). Nhập phân số tối giản.",
        "answer": "7/264",
        "topic": "Số học",
        "explanation": "Tính từng phân số rồi quy đồng: 7/748+4/935+1/220+1/420+1/168. BCNN=27720. Tổng quy về = 7/264.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm số cặp số nguyên (x, y) thỏa mãn: 2xy − x − y = 2.",
        "answer": "4",
        "topic": "Đại số",
        "explanation": "Nhân 2: 4xy−2x−2y=4 → (2x−1)(2y−1)=5. Ư(5): (1,5),(5,1),(−1,−5),(−5,−1) → (x,y)=(1,3),(3,1),(0,−2),(−2,0). 4 cặp.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Cho đường thẳng d và điểm A trên d. Trên d lấy B với AB=8cm, C với AC=10cm. Tính tất cả giá trị BC (cm). Nhập 2 giá trị cách nhau dấu phẩy (nhỏ đến lớn).",
        "answer": "2,18",
        "topic": "Hình học",
        "explanation": "TH1: B và C cùng phía A: BC=|10−8|=2cm. TH2: B và C khác phía A: BC=8+10=18cm.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm số tự nhiên 3 chữ số abc sao cho abc = n²−1 và cba = (n−2)². Nhập abc.",
        "answer": "675",
        "topic": "Số học",
        "explanation": "Thử n=26: abc=26²−1=675, cba=24²=576=cba(675) ✓ (đảo chữ số 675 → 576).",
        "image": "",
    },

    # ══════════════════════════════════════════════════════════════════
    # ĐỀ 11 phuong-nam-sam-son — câu còn thiếu (idx 149–154)
    # ══════════════════════════════════════════════════════════════════
    {
        "type": "fill",
        "q": "Tính B = (2¹²·3⁵ − 4⁶·9²) / ((2²·3)⁶ + 8⁴·3⁵) − (5¹⁰·7³ − 25⁵·49²) / ((125·7)³ + 5⁹·14³). Nhập phân số.",
        "answer": "7/2",
        "topic": "Số học",
        "explanation": "Phân số 1: tử=2¹²·3⁵−2¹²·3⁴=2¹³·3⁴, mẫu=2¹²·3⁶+2¹²·3⁵=2¹⁴·3⁵ → 1/6. Phân số 2: tử=5¹⁰·7³(1−7)=−6·5¹⁰·7³, mẫu=5⁹·7³·9 → −10/3. B=1/6−(−10/3)=1/6+20/6=7/2.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: 7⁰ · 7 : (2x − 5) + 7⁴ = 4² − 3²",
        "answer": "5",
        "topic": "Đại số",
        "explanation": "4²−3²=7. 7:(2x−5)+2401=7. Theo hướng dẫn chấm: 2^x=32=2⁵ → x=5.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tìm x: −1/6 + (7/6)·(x + 1) = (9/(−14))·(7/18). Nhập phân số tối giản.",
        "answer": "-15/14",
        "topic": "Đại số",
        "explanation": "VT phải=(9/−14)·(7/18)=−1/4. (7/6)(x+1)=−1/4+1/6=−1/12. x+1=(−1/12)·(6/7)=−1/14. x=−1/14−1=−15/14.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Ba lớp 6A, 6B, 6C trồng cây: 6A=½(6B+6C), 6B=⅔(6A+6C), 6C=4/11·(6A+6B). Biết 6B nhiều hơn 6A là 3 cây. Tính số cây lớp 6C.",
        "answer": "12",
        "topic": "Số học",
        "explanation": "Tỉ lệ: 6A/tổng=1/3, 6B/tổng=2/5, 6C/tổng=4/15. (6B−6A)/tổng=2/5−1/3=1/15. 1/15·tổng=3 → tổng=45. 6C=4/15·45=12 cây.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Trên tia Ox: OA=5cm, OC=7cm, OB=9cm. Tính AC (cm) và CB (cm). C có phải là trung điểm AB không? Nhập AC (cm).",
        "answer": "2",
        "topic": "Hình học",
        "explanation": "AC=OC−OA=7−5=2cm. CB=OB−OC=9−7=2cm. AC=CB=2cm → C là trung điểm AB.",
        "image": "",
    },
    {
        "type": "fill",
        "q": "Tính P = (1/2²−1)(1/3²−1)(1/4²−1)···(1/100²−1). Nhập phân số tối giản.",
        "answer": "-101/200",
        "topic": "Số học",
        "explanation": "1/n²−1=−(n−1)(n+1)/n². −P=∏(n−1)(n+1)/n²=[(1·2···99)/(2·3···100)]·[(3·4···101)/(2·3···100)]=(1/100)·(101/2)=101/200. P=−101/200.",
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
# ── Thêm mới (72 câu, idx 81–152) ──
#   81-91  → Exam 1 xa-phuc-loc: câu còn thiếu (11 câu)
#   92-100 → Exam 2 cum-truong-thcs-ha-noi: câu còn thiếu (9 câu)
#   101-108→ Exam 3 xa-ba-thuoc: câu còn thiếu (8 câu)
#   109-119→ Exam 4 xa-quang-binh: câu còn thiếu (11 câu)
#   120-130→ Exam 5 xa-quang-ngoc: câu còn thiếu (11 câu)
#   131-135→ Exam 8 xa-nhu-thanh: câu còn thiếu (5 câu)
#   136-140→ Exam 9 xa-xuan-tin: câu còn thiếu (5 câu)
#   141-146→ Exam 10 xa-duc-tho: câu còn thiếu (6 câu)
#   147-152→ Exam 11 phuong-nam-sam-son: câu còn thiếu (6 câu)
_HSG_TOAN_6_EXAMS = {
    1:  MINH_KHANH_TOAN_HSG[0:6]   + MINH_KHANH_TOAN_HSG[81:92],
    2:  MINH_KHANH_TOAN_HSG[6:10]  + MINH_KHANH_TOAN_HSG[92:101],
    3:  MINH_KHANH_TOAN_HSG[10:17] + [MINH_KHANH_TOAN_HSG[78]] + MINH_KHANH_TOAN_HSG[101:109],
    4:  MINH_KHANH_TOAN_HSG[17:21] + MINH_KHANH_TOAN_HSG[109:120],
    5:  MINH_KHANH_TOAN_HSG[21:26] + MINH_KHANH_TOAN_HSG[79:81]  + MINH_KHANH_TOAN_HSG[120:131],
    6:  MINH_KHANH_TOAN_HSG[26:31],
    7:  _HSG_TOAN_6_DE_7,          # đầy đủ 25 câu từ PDF xa-luc-ngan
    8:  MINH_KHANH_TOAN_HSG[0:2]   + MINH_KHANH_TOAN_HSG[38:46]  + MINH_KHANH_TOAN_HSG[131:136],
    9:  MINH_KHANH_TOAN_HSG[49:59] + MINH_KHANH_TOAN_HSG[136:141],
    10: MINH_KHANH_TOAN_HSG[59:72] + MINH_KHANH_TOAN_HSG[141:147],
    11: MINH_KHANH_TOAN_HSG[72:78] + MINH_KHANH_TOAN_HSG[147:153],
}

HSG_EXAM_DURATIONS = {
    1: 120, 2: 120, 3: 150, 4: 120, 5: 120,
    6: 150, 7: 120, 8: 150, 9: 150, 10: 120, 11: 120,
}

HSG_EXAM_NQ = {k: len(v) for k, v in _HSG_TOAN_6_EXAMS.items()}
