# -*- coding: utf-8 -*-
"""Đề KHTN 9 HK1 (cuối học kì 1, năm học 2025–2026) — nguồn thuvienhoclieu.com (bộ 3 đề, có hướng dẫn chấm).

Mọi câu trắc nghiệm đã được tự giải lại và đối chiếu với đáp án gốc. Những chỗ đáp án gốc sai/mơ hồ
được sửa theo kết quả tự giải và ghi rõ "LƯU Ý" trong phần giải thích:
  - Đề 1 câu 15: bảng đáp án ghi C, đúng là A (C₂H₅Br chứa Br, không phải hydrocarbon).
  - Đề 1 câu 23b: đề ghi "thấu kính phân kì (hình 1)" nhưng hình 1 là thấu kính hội tụ; đáp án 30 cm khớp hội tụ.
  - Đề 2 câu 8/9: đáp án gốc đảo nhau (đơn phân DNA là A,T,G,C = B; RNA là A,U,G,C = A).
  - Đề 2 câu 18b: đáp án gốc "Sai", nhưng cơ năng = động năng + thế năng luôn đúng theo định nghĩa → "Đúng".
  - Đề 2 tự luận câu 4b: đáp án gốc 0,81·90% = 0,792 tấn là sai số học; đúng là 0,729 tấn = 729 kg.
  - Đề 3 câu 18: đáp án gốc C (mạch RNA có U); "mạch bổ sung" của gene là mạch DNA nên đúng là A.
Hình vẽ cắt từ file gốc, lưu ở static/khtn_9_hk1_figures/.
"""
DURATION = 60
DURATIONS = {1: 60, 2: 60, 3: 60}
SOURCES = {
    1: 'Đề kiểm tra cuối học kì I môn KHTN 9, năm học 2025–2026, đề 1 (thuvienhoclieu.com – Bộ đề kiểm tra cuối HK1 KHTN 9 năm 25-26)',
    2: 'Đề kiểm tra cuối học kì I môn KHTN 9, năm học 2025–2026, đề 2 (thuvienhoclieu.com – Bộ đề kiểm tra cuối HK1 KHTN 9 năm 25-26)',
    3: 'Đề kiểm tra cuối học kì I môn KHTN 9, năm học 2025–2026, đề 3 (thuvienhoclieu.com – Bộ đề kiểm tra cuối HK1 KHTN 9 năm 25-26)',
}

_F = "khtn_9_hk1_figures/"
_LET = "ABCD"


def _mc(topic, q, opts, ans, expl, section=None, instr=None, image=None):
    """Trắc nghiệm 4 lựa chọn. opts không kèm chữ cái; ans là 'A'..'D'."""
    options = [f"{_LET[i]}. {o}" for i, o in enumerate(opts)]
    d = {"type": "choice", "topic": topic, "section_start": section, "section_instruction": instr,
         "passage_text": None, "q": q, "options": options, "answer": options[_LET.index(ans)],
         "explanation": expl}
    if image:
        d["image"] = _F + image
    return d


def _tf(topic, q, ok, expl, section=None, instr=None):
    """Một ý Đúng/Sai (a, b, c, d) — tách thành 1 entry choice."""
    options = ["A. Đúng", "B. Sai"]
    return {"type": "choice", "topic": topic, "section_start": section, "section_instruction": instr,
            "passage_text": None, "q": q, "options": options,
            "answer": options[0] if ok else options[1], "explanation": expl}


def _fill(topic, q, ans, expl, alt=None, section=None, instr=None, image=None):
    d = {"type": "fill", "topic": topic, "section_start": section, "section_instruction": instr,
         "passage_text": None, "q": q, "answer": ans, "explanation": expl}
    if alt:
        d["alt_answers"] = alt
    if image:
        d["image"] = _F + image
    return d


def _essay(topic, q, expl, lines=8, section=None, instr=None, image=None):
    d = {"type": "essay", "topic": topic, "section_start": section, "section_instruction": instr,
         "passage_text": None, "q": q, "essay_lines": lines, "essay_word_min": None,
         "essay_word_max": None, "answer": "(Bài làm tự chấm tay)", "explanation": expl}
    if image:
        d["image"] = _F + image
    return d


# ───────────────────────────── ĐỀ 1 ─────────────────────────────
_S1_TN = "Phần 1. Trắc nghiệm nhiều lựa chọn (20 câu × 0,25 = 5,0 điểm)"
_S1_TF = "Phần 2. Trắc nghiệm đúng sai (2,0 điểm)"
_S1_TL = "B. PHẦN TỰ LUẬN (3 ĐIỂM)"
_I_TF = "Trong mỗi ý a), b), c), d) ở mỗi câu, em chọn Đúng hoặc Sai."

_DE_1 = [
    _mc("Cơ năng", "Câu 1. Đâu là công thức xác định thế năng trọng trường?",
        ["Wt = 1/2.m.v²", "Wt = F.s", "Wt = A/t", "Wt = 10.m.h"], "D",
        "Thế năng trọng trường của vật khối lượng m ở độ cao h so với mốc thế năng: Wt = P·h = 10·m·h (vì P = 10m). "
        "A là công thức động năng, B là công cơ học (A = F·s), C là công suất (P = A/t).",
        section=_S1_TN, instr="Mỗi câu có 4 phương án trả lời, chỉ có 1 phương án đúng."),
    _mc("Cơ năng", "Câu 2. Trong hệ SI, đơn vị đo động năng là gì?",
        ["Mét trên giây bình phương (m/s²).", "Oát (W).", "Jun (J).", "Niutơn (N)."], "C",
        "Động năng là một dạng năng lượng nên đo bằng jun (J). m/s² là đơn vị gia tốc, W là đơn vị công suất, N là đơn vị lực."),
    _mc("Khúc xạ ánh sáng", "Câu 3. Khi ánh sáng truyền từ không khí vào trong nước thì tia sáng",
        ["phản xạ quay lại không khí tại mặt phân cách giữa hai môi trường.",
         "tiếp tục đi vào trong nước và bị gãy khúc tại mặt phân cách giữa hai môi trường.",
         "đi theo đường thẳng vào trong nước.",
         "biến mất tại mặt phân cách giữa hai môi trường."], "B",
        "Khi truyền xiên góc qua mặt phân cách hai môi trường trong suốt, tia sáng vẫn đi tiếp sang môi trường thứ hai nhưng bị đổi hướng (gãy khúc) — "
        "đó là hiện tượng khúc xạ ánh sáng. Ánh sáng không quay lại hoàn toàn, không đi thẳng khi tới xiên góc và không biến mất."),
    _mc("Động năng", "Câu 4. Một vật đang chuyển động với vận tốc v và vật có khối lượng m thì nó có động năng là Wđ. "
        "Nếu tốc độ của vật tăng lên gấp 3 lần đồng thời khối lượng của vật tăng gấp 2 lần thì động năng của nó khi đó sẽ",
        ["tăng 6 lần.", "tăng 18 lần.", "giảm 6 lần.", "tăng 12 lần."], "B",
        "Wđ = ½·m·v². Sau thay đổi: Wđ' = ½·(2m)·(3v)² = 9·m·v² = 18·(½·m·v²) = 18·Wđ. Vậy động năng tăng 18 lần (tốc độ tăng 3 lần → ×9, khối lượng tăng 2 lần → ×2)."),
    _mc("Cơ năng", "Câu 5. Khi một vật chuyển động rơi tự do từ trên xuống dưới thì:",
        ["thế năng của vật giảm dần", "động năng của vật giảm dần.", "thế năng của vật tăng dần", "Năng lượng của vật giảm dần."], "A",
        "Vật rơi xuống: độ cao giảm nên thế năng giảm dần, vận tốc tăng nên động năng tăng dần. Nếu bỏ qua lực cản, thế năng chuyển hóa thành động năng "
        "và cơ năng (tổng năng lượng) được bảo toàn, không giảm."),
    _mc("Cơ năng", "Câu 6. Cơ năng của vật sẽ không được bảo toàn khi vật:",
        ["chỉ chịu tác dụng của trọng lực.", "chỉ chịu tác dụng của lực đàn hồi của lò xo.",
         "chịu tác dụng của lực cản, lực ma sát.", "không chịu tác dụng của lực ma sát, lực cản."], "C",
        "Cơ năng được bảo toàn khi vật chỉ chịu tác dụng của trọng lực hoặc lực đàn hồi (không có lực cản, ma sát). "
        "Khi có lực cản/ma sát, một phần cơ năng chuyển hóa thành nhiệt năng nên cơ năng không được bảo toàn."),
    _mc("Thấu kính", "Câu 7. Khi nói về thấu kính, câu kết luận nào dưới đây KHÔNG đúng?",
        ["Thấu kính hội tụ có phần rìa mỏng hơn phần giữa.", "Thấu kính phân kì có phần rìa dày hơn phần giữa",
         "Thấu kính phân kì luôn cho ảnh ảo, cùng chiều và nhỏ hơn vật.",
         "Thấu kính hội tụ luôn cho ảnh thật, ngược chiều và nhỏ hơn vật."], "D",
        "A, B, C đều đúng. D sai: thấu kính hội tụ chỉ cho ảnh thật, ngược chiều khi vật nằm ngoài tiêu cự, và ảnh có thể nhỏ hơn, bằng hoặc lớn hơn vật "
        "tùy vị trí của vật; khi vật nằm trong tiêu cự thì cho ảnh ảo, cùng chiều, lớn hơn vật."),
    _mc("Thấu kính", "Câu 8. Đặt một vật sáng PQ hình mũi tên vuông góc với trục chính của thấu kính hội tụ và nằm ngoài khoảng tiêu cự của thấu kính. "
        "Hình vẽ nào vẽ đúng ảnh P'Q' của PQ qua thấu kính?",
        ["Hình A", "Hình B", "Hình C", "Hình D"], "D",
        "Vật ngoài tiêu cự (d > f) của thấu kính hội tụ cho ảnh thật, ngược chiều, nằm ở bên kia thấu kính và xa thấu kính hơn tiêu điểm F' (d' > f). "
        "Hình B và C vẽ ảnh ảo (nét đứt, cùng chiều) — chỉ đúng khi vật nằm trong khoảng OF, nên loại. "
        "Hình A vẽ ảnh nằm trong đoạn OF' (gần thấu kính hơn tiêu điểm) nên sai. "
        "Hình D: tia tới song song trục chính cho tia ló qua F', tia qua quang tâm O truyền thẳng; hai tia ló cắt nhau tại Q' "
        "nên P'Q' là ảnh thật, ngược chiều, nằm ngoài F' → đúng.",
        image="de1_cau8.png"),
    _mc("Kim loại", "Câu 9. (NB) Kim loại có nhiệt độ nóng chảy thấp nhất là",
        ["bạc.", "vàng.", "tungsten.", "thủy ngân."], "D",
        "Thủy ngân (Hg) nóng chảy ở khoảng −39 °C nên là kim loại duy nhất ở thể lỏng ở nhiệt độ thường; bạc, vàng nóng chảy trên 900 °C, tungsten cao nhất (khoảng 3410 °C)."),
    _mc("Kim loại", "Câu 10. (NB) Kim loại tác dụng với ___________ tạo thành oxide.",
        ["hydrogen.", "chlorine.", "oxygen.", "sodium."], "C",
        "Kim loại + oxygen → oxide kim loại, ví dụ 2Mg + O₂ → 2MgO. Kim loại tác dụng với chlorine tạo muối chloride, không phải oxide."),
    _mc("Dãy hoạt động hóa học", "Câu 11. (TH) Dãy chất gồm các kim loại được sắp xếp theo chiều tăng dần về hoạt động hóa học là:",
        ["Cu, Fe, Zn, Al, Na, K", "Al, Na, Fe, Cu, K, Zn", "Fe, Al, Cu, Zn, K, Na", "Fe, Cu, Al, K, Na, Zn."], "A",
        "Dãy hoạt động hóa học (giảm dần): K, Na, Mg, Al, Zn, Fe, (H), Cu, Ag, Au. Sắp xếp tăng dần trong các kim loại đã cho: Cu < Fe < Zn < Al < Na < K → đáp án A."),
    _mc("Điều chế kim loại", "Câu 12. (NB) Phản ứng điều chế kim loại nào sau đây thuộc phương pháp nhiệt luyện?",
        ["2NaCl → 2Na + Cl₂", "3CO + Fe₂O₃ → 2Fe + 3CO₂", "Fe + CuSO₄ → FeSO₄ + Cu", "2Al₂O₃ → 4Al + 3O₂"], "B",
        "Nhiệt luyện: dùng chất khử (CO, H₂, C, Al…) ở nhiệt độ cao để khử oxide kim loại thành kim loại → 3CO + Fe₂O₃ → 2Fe + 3CO₂. "
        "A và D là điện phân nóng chảy; C là phương pháp thủy luyện (kim loại mạnh đẩy kim loại yếu ra khỏi dung dịch muối)."),
    _mc("Liên kết ion", "Câu 13. (TH) Trong phản ứng giữa Mg và Cl₂,",
        ["Mg dễ nhận electron để trở thành ion âm.", "Cl dễ nhường electron để trở thành ion dương",
         "Cl dễ nhận electron để trở thành ion âm.", "Mg dễ nhường electron để trở thành ion âm."], "C",
        "Mg là kim loại (2 electron lớp ngoài cùng) dễ nhường 2 electron tạo ion dương Mg²⁺; Cl là phi kim (7 electron lớp ngoài cùng) dễ nhận 1 electron tạo ion âm Cl⁻. "
        "Hai ion trái dấu hút nhau tạo MgCl₂. Chỉ phát biểu C đúng."),
    _mc("Hợp chất hữu cơ", "Câu 14. (TH) Cho các phát biểu về đặc điểm chung của các phân tử hợp chất hữu cơ:\n"
        "(1) Thành phần nguyên tố chủ yếu là C và H.\n"
        "(2) Có thể chứa nguyên tố khác như Cl, N, P, O.\n"
        "(3) Liên kết hóa học chủ yếu là liên kết cộng hoá trị.\n"
        "(4) Liên kết hoá học chủ yếu là liên kết ion.\n"
        "(5) Dễ bay hơi, khó cháy.\n"
        "(6) Phản ứng hoá học xảy ra nhanh.\n"
        "Các phát biểu đúng là",
        ["(4), (5), (6).", "(1), (2), (3).", "(1), (3), (5).", "(2), (4), (6)."], "B",
        "Hợp chất hữu cơ có thành phần chủ yếu là C, H, ngoài ra có thể có O, N, Cl, P…; liên kết chủ yếu là liên kết cộng hóa trị → (1), (2), (3) đúng. "
        "(4) sai (không phải liên kết ion); (5) sai (thường dễ bay hơi và dễ cháy); (6) sai (phản ứng thường xảy ra chậm, không hoàn toàn)."),
    _mc("Hydrocarbon", "Câu 15. (NB) Dãy các chất nào sau đây đều là hydrocarbon?",
        ["C₂H₆, C₄H₁₀, CH₄.", "CH₄, C₂H₂, C₃H₇Cl.", "C₂H₄, CH₄, C₂H₅Br.", "C₂H₆O, C₃H₈, C₂H₂"], "A",
        "Hydrocarbon là hợp chất chỉ chứa hai nguyên tố C và H. A: C₂H₆, C₄H₁₀, CH₄ đều chỉ có C, H → đúng. B có C₃H₇Cl (chứa Cl); C có C₂H₅Br (chứa Br); D có C₂H₆O (chứa O). "
        "LƯU Ý: bảng đáp án gốc ghi C nhưng sai (C₂H₅Br là dẫn xuất halogen); đáp án đúng là A."),
    _mc("Hợp chất hữu cơ", "Câu 16. (VD) Thành phần phần trăm về khối lượng của nguyên tố C trong C₃H₈O là",
        ["30%.", "40%.", "50%.", "60%."], "D",
        "M(C₃H₈O) = 3·12 + 8·1 + 16 = 60 (g/mol). %C = (3·12)/60 · 100% = 36/60 · 100% = 60%."),
    _mc("Di truyền Mendel", "Câu 17. Tính trạng trội biểu hiện ra kiểu hình khi",
        ["Có kiểu gene đồng hợp lặn hoặc dị hợp.", "Có kiểu gene đồng hợp trội hoặc dị hợp.",
         "Có kiểu gene đồng hợp trội.", "Có kiểu gene đồng hợp lặn."], "B",
        "Allele trội át allele lặn nên tính trạng trội biểu hiện ở cả kiểu gene đồng hợp trội (AA) và dị hợp (Aa)."),
    _mc("Di truyền Mendel", "Câu 18. Tính trạng lặn biểu hiện ra kiểu hình khi",
        ["Có kiểu gene đồng hợp lặn hoặc dị hợp.", "Có kiểu gene đồng hợp trội hoặc dị hợp.",
         "Có kiểu gene đồng hợp trội.", "Có kiểu gene đồng hợp lặn."], "D",
        "Ở thể dị hợp, allele trội át allele lặn; tính trạng lặn chỉ biểu hiện khi không có allele trội, tức kiểu gene đồng hợp lặn (aa)."),
    _mc("Tái bản DNA", "Câu 19. Quá trình tái bản DNA dựa trên nguyên tắc nào?",
        ["Nguyên tắc bổ sung.", "Nguyên tắc bán bảo toàn.", "Nguyên tắc bảo toàn.", "Cả A và B."], "D",
        "Tái bản DNA diễn ra theo nguyên tắc bổ sung (A–T, G–C) và nguyên tắc bán bảo toàn (mỗi DNA con có 1 mạch cũ của DNA mẹ và 1 mạch mới tổng hợp) → cả A và B."),
    _mc("Tái bản DNA", "Câu 20. (VD) Một DNA tái bản 3 lần. Số DNA con được tạo ra là",
        ["2.", "3.", "8.", "16"], "C",
        "Một DNA tái bản k lần tạo 2ᵏ DNA con. Với k = 3: 2³ = 8 DNA con."),

    # ── Phần 2: Đúng/Sai ──
    _tf("Cơ năng", "Câu 21a. Một viên gạch có trọng lượng 10 N nằm yên trên sân thượng tầng 2 của tòa nhà cao 10 m so với mặt đất. "
        "Cho viên gạch rơi tự do dưới tác dụng của lực hút Trái Đất xuống đất từ sân thượng tòa nhà.\n"
        "a) So với mặt đất, viên gạch có thế năng trọng trường.", True,
        "Viên gạch ở độ cao 10 m so với mặt đất nên có thế năng trọng trường: Wt = P·h = 10·10 = 100 J.",
        section=_S1_TF, instr=_I_TF),
    _tf("Cơ năng", "Câu 21b. (Viên gạch trọng lượng 10 N nằm yên trên sân thượng cao 10 m, sau đó rơi tự do xuống đất.)\n"
        "b) So với sân thượng viên gạch không có động năng vì nó nằm yên không chuyển động.", True,
        "Trước khi thả, viên gạch nằm yên (v = 0) nên động năng Wđ = ½mv² = 0."),
    _tf("Cơ năng", "Câu 21c. (Viên gạch trọng lượng 10 N nằm yên trên sân thượng cao 10 m, sau đó rơi tự do xuống đất.)\n"
        "c) Cơ năng của viên gạch bằng 200 J.", False,
        "Cơ năng = động năng + thế năng = 0 + 10·10 = 100 J (khi còn nằm yên trên sân thượng), không phải 200 J."),
    _tf("Công cơ học", "Câu 21d. (Viên gạch trọng lượng 10 N nằm yên trên sân thượng cao 10 m, sau đó rơi tự do xuống đất.)\n"
        "d) Công của lực hút Trái Đất khi gạch rơi xuống đất bằng 100 J.", True,
        "Công của trọng lực khi rơi xuống độ cao h: A = P·h = 10·10 = 100 J (bằng độ giảm thế năng)."),
    _tf("Di truyền Mendel", "Câu 22a. Các phát biểu sau đây phát biểu nào đúng, phát biểu nào sai?\n"
        "A. Cặp nhân tố di truyền phân li độc lập, không hòa lẫn vào nhau trong quá trình hình thành giao tử.", True,
        "Theo Mendel, các nhân tố di truyền trong một cặp không hòa trộn vào nhau mà phân li về các giao tử, mỗi giao tử chỉ chứa một nhân tố của cặp — phát biểu đúng theo đáp án."),
    _tf("Di truyền Mendel", "Câu 22b. Các phát biểu sau đây phát biểu nào đúng, phát biểu nào sai?\n"
        "B. Phép lai phân tích là phép lai giữa cá thể mang tính trạng lặn cần xác định kiểu gen với cá thể mang tính trạng trội.", False,
        "Sai: phép lai phân tích là phép lai giữa cá thể mang tính trạng TRỘI cần xác định kiểu gene với cá thể mang tính trạng LẶN (đồng hợp lặn). Phát biểu đã đảo ngược."),
    _tf("Di truyền Mendel", "Câu 22c. Các phát biểu sau đây phát biểu nào đúng, phát biểu nào sai?\n"
        "C. Khi cho P: Aa × aa kết quả phép lai sẽ là 3 trội : 1 lặn.", False,
        "Aa × aa → 1/2 Aa : 1/2 aa, tức tỉ lệ 1 trội : 1 lặn (không phải 3 : 1; tỉ lệ 3 : 1 là của Aa × Aa)."),
    _tf("Di truyền Mendel", "Câu 22d. Các phát biểu sau đây phát biểu nào đúng, phát biểu nào sai?\n"
        "D. Cặp tính trạng tương phản là hai trạng thái biểu hiện trái ngược của cùng một loại tính trạng.", True,
        "Đúng — đó là định nghĩa cặp tính trạng tương phản (ví dụ hoa tím – hoa trắng, thân cao – thân thấp)."),

    # ── Phần B: Tự luận ──
    _essay("Thấu kính", "Câu 23 (1 điểm). a) Vẽ ảnh của vật sáng AB đặt trước thấu kính trong các trường hợp hình dưới đây (hình 1: thấu kính hội tụ; hình 2: thấu kính phân kì).",
        "Hướng dẫn chấm gốc: vẽ đúng hình (0,5 điểm). Hình 1 (hội tụ, vật trong khoảng OF): vẽ tia tới song song trục chính cho tia ló qua F' và tia qua O truyền thẳng; "
        "hai tia ló phân kì nên kéo dài ngược chúng (nét đứt) cắt nhau tại B' → ảnh A'B' là ảnh ảo, cùng chiều, lớn hơn vật, cùng phía với vật. "
        "Hình 2 (phân kì): tia tới song song trục chính cho tia ló có đường kéo dài qua F; tia qua O truyền thẳng; giao điểm của các đường kéo dài là B' → ảnh ảo, cùng chiều, nhỏ hơn vật, nằm trong khoảng OF.",
        lines=4, section=_S1_TL, image="de1_cau23.png"),
    _fill("Thấu kính", "Câu 23 (1 điểm). b) Cho f = 15 cm; vật cách thấu kính một khoảng 10 cm. Xác định khoảng cách từ ảnh đến thấu kính (hình 1).\n"
        "[Lưu ý: đề gốc ghi 'thấu kính phân kì (hình 1)' nhưng hình 1 vẽ thấu kính hội tụ, đáp án gốc 30 cm khớp với thấu kính hội tụ.]\n"
        "Nhập khoảng cách (cm), chỉ gõ số.",
        "30",
        "Hình 1 là thấu kính hội tụ, vật AB cách thấu kính d = 10 cm < f = 15 cm nên cho ảnh ảo. Công thức thấu kính (ảnh ảo): 1/f = 1/d − 1/d' ⇒ 1/d' = 1/10 − 1/15 = 1/30 ⇒ d' = 30 cm. "
        "Có thể dùng tam giác đồng dạng: d'/d = f/(f − d) = 15/5 = 3 ⇒ d' = 30 cm. "
        "(Nếu thật sự là thấu kính phân kì như chữ trong đề thì 1/d' = 1/f + 1/d = 1/15 + 1/10 = 1/6 ⇒ d' = 6 cm; nhưng hình 1 và đáp án gốc đều ứng với thấu kính hội tụ nên đáp số là 30 cm.)",
        alt=["30cm", "30 cm"], image="de1_cau23.png"),
    _essay("Phương trình hóa học", "Câu 24 (1 điểm). Dùng 14,874 lít khí CO ở điều kiện chuẩn để khử vừa đủ một lượng oxide Fe₂O₃ (được lấy từ một mẫu quặng và đã qua giai đoạn làm giàu quặng) "
        "đến khi sau phản ứng chỉ thu được m gam chất rắn (là kim loại Fe) và V lít khí CO₂ (đo ở đkc).\na) Viết phương trình hoá học xảy ra.",
        "3CO + Fe₂O₃ → 2Fe + 3CO₂ (nhiệt độ cao). (0,25 điểm)", lines=3),
    _fill("Tính theo phương trình hóa học", "Câu 24 (1 điểm). b) Tính m gam Fe và V lít khí CO₂ (ở đkc).\n"
        "Nhập dạng m;V (m tính bằng gam, V tính bằng lít, dùng dấu phẩy thập phân), ví dụ 5,6;1,2.",
        "22,4;14,874",
        "n(CO) = 14,874 : 24,79 = 0,6 mol. PTHH: 3CO + Fe₂O₃ → 2Fe + 3CO₂. Tỉ lệ mol 3 : 1 : 2 : 3, nên n(Fe₂O₃) = 0,2 mol; n(Fe) = 0,4 mol; n(CO₂) = 0,6 mol. "
        "Vậy m(Fe) = 0,4·56 = 22,4 g; V(CO₂) = 0,6·24,79 = 14,874 lít.",
        alt=["22,4g;14,874l", "22,4;14,874l"]),
    _essay("RNA", "Câu 25 (1 điểm). Nêu cấu trúc của phân tử RNA? Các loại RNA có chức năng như thế nào?",
        "a) Cấu trúc RNA (0,5 điểm): cấu trúc một mạch, cấu tạo theo nguyên tắc đa phân gồm các đơn phân là A, U, G, C liên kết với nhau bằng liên kết cộng hóa trị tạo thành mạch RNA. "
        "b) Chức năng (0,5 điểm): mRNA truyền đạt thông tin di truyền từ nhân ra tế bào chất, làm khuôn cho quá trình dịch mã tổng hợp chuỗi polypeptide; "
        "tRNA vận chuyển amino acid tự do đến nơi tổng hợp protein; rRNA là thành phần chủ yếu cấu tạo nên ribosome – nơi tổng hợp protein.", lines=8),
]

# ───────────────────────────── ĐỀ 2 ─────────────────────────────
_S2_TN = "DẠNG THỨC 1. Trắc nghiệm nhiều phương án lựa chọn (16 câu × 0,25 = 4,0 điểm)"
_S2_TF = "DẠNG THỨC 2. Trắc nghiệm đúng/sai"
_S2_TL = "II. TỰ LUẬN"

_DE_2 = [
    _mc("Hợp kim", "Câu 1. Gang và thép là hợp kim của",
        ["aluminum và copper.", "iron và carbon.", "carbon và silicon.", "iron và aluminum."], "B",
        "Gang và thép đều là hợp kim của sắt (iron) với carbon; gang có hàm lượng C từ 2% đến 5%, thép có hàm lượng C dưới 2%.",
        section=_S2_TN, instr="Mỗi câu chỉ có một lựa chọn đúng."),
    _mc("Kim loại", "Câu 2. Trong các kim loại sau đây, kim loại dẫn điện tốt nhất là:",
        ["Al.", "Ag.", "Cu.", "Fe."], "B",
        "Thứ tự dẫn điện giảm dần: Ag > Cu > Au > Al > Fe. Bạc (Ag) dẫn điện tốt nhất (nhưng đắt nên dây dẫn thường dùng Cu, Al)."),
    _mc("Kim loại", "Câu 3. Các kim loại được dùng làm đồ trang sức vì có ánh kim rất đẹp, đó là các kim loại:",
        ["Ag, Al.", "Au, Ag.", "Au, Cu.", "Cu, Al."], "B",
        "Vàng (Au) và bạc (Ag) có ánh kim rất đẹp, bền, ít bị oxi hóa nên được dùng làm đồ trang sức."),
    _mc("Hydrocarbon", "Câu 4. Chất nào sau đây là hydrocarbon?",
        ["CH₂O.", "C₂H₅Br.", "C₆H₆.", "CH₃COOH"], "C",
        "Hydrocarbon chỉ gồm C và H. C₆H₆ (benzene) là hydrocarbon; CH₂O và CH₃COOH có O, C₂H₅Br có Br."),
    _mc("Dãy hoạt động hóa học", "Câu 5. Dãy kim loại được sắp xếp theo chiều hoạt động hóa học giảm dần:",
        ["Na, Mg, Zn.", "Al, Zn, Na.", "Mg, Al, Na.", "Pb, Al, Mg."], "A",
        "Dãy hoạt động hóa học: K, Na, Mg, Al, Zn, Fe, Pb, (H), Cu… Chỉ dãy Na > Mg > Zn đúng chiều giảm dần. "
        "B (Al, Zn, Na), C (Mg, Al, Na) và D (Pb, Al, Mg) đều đang sắp xếp tăng dần hoặc lộn xộn."),
    _mc("Kim loại tác dụng với muối", "Câu 6. Có một mẫu dung dịch MgSO₄ bị lẫn tạp chất là ZnSO₄, có thể làm sạch mẫu dung dịch này bằng kim loại",
        ["Zn.", "Mg.", "Fe.", "Cu."], "B",
        "Dùng Mg dư: Mg + ZnSO₄ → MgSO₄ + Zn↓ (Mg hoạt động mạnh hơn Zn nên đẩy được Zn ra khỏi muối); lọc bỏ Zn và Mg dư thu được dung dịch MgSO₄ tinh khiết. "
        "Zn, Fe, Cu đều kém hoạt động hơn Mg nên không phản ứng với MgSO₄ và không loại được ZnSO₄ (Zn không đẩy được chính Zn)."),
    _mc("Kim loại tác dụng với muối", "Câu 7. Ngâm 1 viên zinc (Zn) sạch trong dung dịch CuSO₄. Câu trả lời nào sau đây đúng nhất cho hiện tượng quan sát được?",
        ["Không có hiện tượng nào xảy ra.",
         "Một phần viên zinc bị hòa tan, có một lớp màu đỏ bám ngoài viên zinc và màu xanh lam của dung dịch bị nhạt dần.",
         "Không có chất mới nào sinh ra, chỉ có 1 phần viên zinc bị hòa tan.",
         "Kim loại Cu màu đỏ bám ngoài viên Zn, viên Zn không bị hòa tan."], "B",
        "Zn + CuSO₄ → ZnSO₄ + Cu. Zn mạnh hơn Cu nên tan dần; Cu màu đỏ bám ngoài viên Zn; Cu²⁺ (màu xanh lam) giảm dần nên màu dung dịch nhạt dần."),
    _mc("DNA", "Câu 8. Bốn loại đơn phân cấu tạo DNA có kí hiệu là",
        ["A, U, G, C.", "A, T, G, C.", "A, D, R, T.", "U, R, D, C."], "B",
        "DNA gồm 4 loại nucleotide A (adenine), T (thymine), G (guanine), C (cytosine). "
        "LƯU Ý: bảng đáp án gốc ghi A (đảo với câu 9); đáp án đúng là B."),
    _mc("RNA", "Câu 9. Bốn loại đơn phân cấu tạo RNA có kí hiệu là",
        ["A, U, G, C.", "A, T, G, C.", "A, D, R, T.", "U, R, D, C."], "A",
        "RNA gồm 4 loại nucleotide A, U (uracil), G, C — uracil thay thế thymine. "
        "LƯU Ý: bảng đáp án gốc ghi B (đảo với câu 8); đáp án đúng là A."),
    _mc("Di truyền Mendel", "Câu 10. Đặc điểm nào dưới đây của đậu Hà Lan là KHÔNG đúng?",
        ["Tự thụ phấn chặt chẽ.", "Có thể tiến hành giao phấn giữa các cá thể khác nhau.",
         "Thời gian sinh trưởng khá dài.", "Có nhiều cặp tính trạng tương phản."], "C",
        "Đậu Hà Lan tự thụ phấn nghiêm ngặt, dễ giao phấn nhân tạo, có nhiều cặp tính trạng tương phản rõ rệt và có thời gian sinh trưởng NGẮN, nên thuận lợi cho Mendel nghiên cứu. "
        "Vì vậy đặc điểm 'thời gian sinh trưởng khá dài' là không đúng."),
    _mc("Di truyền Mendel", "Câu 11. Nội dung nào sau đây KHÔNG thuộc phương pháp nghiên cứu của Mendel?",
        ["Kiểm tra độ thuần chủng của bố mẹ trước khi đem lai.",
         "Theo dõi sự di truyền đồng thời của tất cả tính trạng trên con cháu của từng cặp bố mẹ.",
         "Dùng toán thống kê để phân tích các số liệu thu được, từ đó rút ra quy luật di truyền các tính trạng đó của bố mẹ cho các thế hệ sau.",
         "Lai các cặp bố mẹ thuần chủng khác nhau về một hoặc vài cặp tính trạng tương phản."], "B",
        "Mendel chỉ theo dõi sự di truyền của một hoặc một vài cặp tính trạng tương phản (không theo dõi đồng thời tất cả tính trạng), sau đó dùng toán thống kê để xử lí số liệu. "
        "Các ý A, C, D đều thuộc phương pháp của ông."),
    _mc("Công suất", "Câu 12. Công suất là:",
        ["Công thực hiện được trong một giây.", "Công thực hiện được trong một ngày.",
         "Công thực hiện được trong một giờ.", "Công thực hiện được trong một đơn vị thời gian."], "D",
        "Công suất P = A/t là công thực hiện được trong một đơn vị thời gian (giây, giờ, ngày… tùy chọn đơn vị). A, B, C chỉ là trường hợp riêng với một đơn vị thời gian cụ thể nên không đầy đủ."),
    _mc("Công suất", "Câu 13. Đơn vị của công suất là",
        ["Oát (W)", "Kilôoát (kW)", "Jun trên giây (J/s)", "Cả ba đơn vị trên"], "D",
        "Đơn vị công suất trong SI là oát (W), 1 W = 1 J/s; 1 kW = 1000 W. Cả ba đều là đơn vị công suất."),
    _mc("Cơ năng", "Câu 14. Đơn vị đo của thế năng trọng trường là gì?",
        ["Niutơn (N)", "Jun (J)", "Kilôgam (kg)", "Mét trên giây bình phương (m/s²)"], "B",
        "Thế năng là một dạng năng lượng nên đo bằng jun (J)."),
    _mc("Công suất", "Câu 15. Một động cơ thực hiện 1000 J trong thời gian 5 giây. Công suất của động cơ là bao nhiêu?",
        ["125 W.", "500 W.", "200 W.", "600 W."], "C",
        "P = A/t = 1000 J : 5 s = 200 W."),
    _mc("Khúc xạ ánh sáng", "Câu 16. Khi nhìn một hòn sỏi trong chậu nước, ta thấy hòn sỏi như được “nâng lên”. Hiện tượng này liên quan đến",
        ["sự truyền thẳng của ánh sáng.", "sự khúc xạ của ánh sáng.", "sự phản xạ của ánh sáng.", "khả năng quan sát của mắt người."], "B",
        "Ánh sáng từ hòn sỏi truyền qua mặt phân cách nước – không khí bị khúc xạ (gãy khúc); mắt nhìn theo hướng tia khúc xạ nên thấy ảnh của hòn sỏi ở vị trí cao hơn vị trí thật."),

    # ── Dạng thức 2: Đúng/Sai ──
    _tf("Di truyền phân li độc lập", "Câu 17a. Giả sử ở một loài thực vật, cơ thể P có n cặp gene dị hợp quy định n tính trạng di truyền phân li độc lập. Hãy xác định các phát biểu dưới đây là đúng hay sai?\n"
        "a) Khi cơ thể P giảm phân sẽ tạo ra 2ⁿ loại giao tử.", True,
        "Mỗi cặp gene dị hợp cho 2 loại giao tử; n cặp phân li độc lập cho 2ⁿ loại giao tử.",
        section=_S2_TF, instr="Trong mỗi ý a), b), c), d), em chọn Đúng hoặc Sai. (1 ý đúng: 0,1 đ; 2 ý: 0,25 đ; 3 ý: 0,5 đ; cả 4 ý: 1,0 đ)"),
    _tf("Di truyền phân li độc lập", "Câu 17b. (Cơ thể P có n cặp gene dị hợp quy định n tính trạng phân li độc lập.)\n"
        "b) Khi cho P tự thụ phấn sẽ thu được số loại kiểu gene là 4ⁿ.", False,
        "Mỗi cặp Aa × Aa cho 3 kiểu gene (AA, Aa, aa) nên n cặp cho 3ⁿ kiểu gene. 4ⁿ là số tổ hợp giao tử, không phải số loại kiểu gene."),
    _tf("Di truyền phân li độc lập", "Câu 17c. (Cơ thể P có n cặp gene dị hợp quy định n tính trạng phân li độc lập.)\n"
        "c) Nếu cho P lai phân tích, tỷ lệ kiểu hình ở đời con sẽ là (3:1)ⁿ.", False,
        "Lai phân tích (P × đồng hợp lặn): mỗi cặp Aa × aa cho tỉ lệ kiểu hình 1 : 1 nên n cặp cho (1 : 1)ⁿ, không phải (3 : 1)ⁿ (đó là tỉ lệ của phép tự thụ phấn)."),
    _tf("Di truyền phân li độc lập", "Câu 17d. (Cơ thể P có n cặp gene dị hợp quy định n tính trạng phân li độc lập.)\n"
        "d) Số loại kiểu hình thu được ở đời con là 2ⁿ khi cho P tự thụ phấn.", True,
        "Mỗi cặp Aa × Aa cho 2 loại kiểu hình (3 trội : 1 lặn, với trội hoàn toàn) nên n cặp cho 2ⁿ loại kiểu hình."),
    _tf("Cơ năng và công suất", "Câu 18a. Một cửa hàng sách cần chuyển một lô sách từ tầng 1 lên tầng 5. Mỗi hộp sách có trọng lượng là 15 N và cửa hàng sử dụng một thang máy nhỏ để chuyển. "
        "Mỗi chuyến thang máy chỉ có thể chứa 10 hộp sách và mất 20 giây cho mỗi chuyến, với độ cao tổng cộng từ tầng 1 đến tầng 5 là 16 m.\n"
        "a) Đặt 10 hộp sách trên sàn thang máy, khi thang máy đi từ tầng 1 lên tầng 5 thì 10 hộp sách có cả thế năng và động năng.", True,
        "Khi thang máy đi lên, các hộp sách ở độ cao so với mặt đất (có thế năng) và đang chuyển động (có động năng)."),
    _tf("Cơ năng và công suất", "Câu 18b. (Mỗi hộp sách nặng 15 N; thang máy chở 10 hộp từ tầng 1 lên tầng 5 cao 16 m trong 20 s.)\n"
        "b) Khi thang máy dừng hẳn lại ở tầng 5, cơ năng của 10 hộp sách bằng tổng động năng và thế năng.", True,
        "Cơ năng của vật luôn bằng tổng động năng và thế năng (W = Wđ + Wt). Khi thang máy dừng hẳn thì Wđ = 0 nên cơ năng bằng đúng thế năng, nhưng phát biểu vẫn đúng. "
        "LƯU Ý: đáp án gốc ghi 'Sai' (có thể hiểu nhầm là lúc dừng chỉ còn thế năng); theo định nghĩa cơ năng thì phát biểu này đúng."),
    _tf("Cơ năng và công suất", "Câu 18c. (Mỗi hộp sách nặng 15 N; thang máy chở 10 hộp từ tầng 1 lên tầng 5 cao 16 m trong 20 s.)\n"
        "c) Thế năng trọng trường của 10 hộp sách khi thang máy dừng lại ở tầng 5 là 150 N.", False,
        "Sai hai chỗ: thế năng đo bằng jun (J), không phải niutơn (N); và giá trị là Wt = P·h = (10·15)·16 = 150·16 = 2400 J, không phải 150."),
    _tf("Cơ năng và công suất", "Câu 18d. (Mỗi hộp sách nặng 15 N; thang máy chở 10 hộp từ tầng 1 lên tầng 5 cao 16 m trong 20 s.)\n"
        "d) Công suất của thang máy khi vận chuyển 10 hộp sách từ tầng 1 lên tầng 5 là 120 W.", True,
        "Công nâng 10 hộp: A = P·h = 150·16 = 2400 J. Công suất P = A/t = 2400 : 20 = 120 W."),
    _tf("Kim loại", "Câu 19a. Khi để lâu trong không khí, thép (thành phần chính là sắt) bị han gỉ trong khi vàng vẫn sáng bóng.\n"
        "a) Vàng phản ứng với oxygen trong không khí, còn sắt không phản ứng.", False,
        "Ngược lại: sắt phản ứng với oxygen (và hơi nước) trong không khí tạo gỉ sắt, còn vàng không phản ứng nên vẫn sáng bóng."),
    _tf("Kim loại", "Câu 19b. (Thép bị han gỉ trong không khí, vàng vẫn sáng bóng.)\n"
        "b) Vàng có ánh kim, còn thép không có ánh kim.", False,
        "Sai: kim loại nào cũng có ánh kim, thép (hợp kim của sắt) cũng có ánh kim. Sự khác biệt ở đây là do tính chất hóa học, không phải ánh kim."),
    _tf("Kim loại", "Câu 19c. (Thép bị han gỉ trong không khí, vàng vẫn sáng bóng.)\n"
        "c) Vàng trơ về mặt hoá học.", True,
        "Vàng rất kém hoạt động hóa học (đứng cuối dãy hoạt động), không bị oxi hóa trong không khí nên vẫn sáng bóng."),
    _tf("Kim loại", "Câu 19d. (Thép bị han gỉ trong không khí, vàng vẫn sáng bóng.)\n"
        "d) Sắt hoạt động hoá học mạnh hơn vàng.", True,
        "Sắt đứng trước vàng trong dãy hoạt động hóa học nên hoạt động hóa học mạnh hơn, dễ bị oxi hóa (gỉ) trong không khí ẩm."),

    # ── Tự luận ──
    _essay("Công cơ học", "Câu 1 (1,5 điểm). Trong các trường hợp dưới đây, lực nào thực hiện công cơ học?\n"
        "a) Đầu tàu hỏa đang kéo đoàn tàu chuyển động.\n"
        "b) Quả bưởi rơi từ trên cây xuống.\n"
        "c) Người công nhân dùng ròng rọc cố định kéo vật nặng lên cao (hình vẽ).",
        "Lực thực hiện công khi có lực tác dụng lên vật và vật chuyển dời theo phương của lực. "
        "a) Lực kéo của đầu tàu thực hiện công (0,5 điểm). "
        "b) Trọng lực thực hiện công (0,5 điểm). "
        "c) Lực kéo của người công nhân thực hiện công (0,5 điểm).",
        lines=6, section=_S2_TL, image="de2_cau1.png"),
    _essay("Di truyền Mendel", "Câu 2 (0,25 điểm). Trình bày nội dung quy luật phân li của Mendel.",
        "Mỗi tính trạng do một cặp nhân tố di truyền (cặp allele) quy định. Khi giảm phân hình thành giao tử, các allele trong cặp phân li đồng đều về các giao tử "
        "nên mỗi giao tử chỉ chứa một allele của cặp.", lines=4),
    _fill("DNA", "Câu 3 (0,75 điểm). Phân tử DNA có tổng số 1500 cặp nucleotide và 3900 liên kết hydrogen. Tính chiều dài và số nucleotide mỗi loại của DNA.\n"
        "Nhập dạng chiều dài(Å);số nucleotide loại A;số nucleotide loại G, ví dụ 3400;500;700.",
        "5100;600;900",
        "Tổng số nucleotide N = 1500 × 2 = 3000. Chiều dài L = 1500 × 3,4 = 5100 Å. "
        "Có A + G = 1500 và H = 2A + 3G = 3900. Lấy 2A + 3G − 2(A + G) = 3900 − 3000 ⇒ G = 900, suy ra A = 1500 − 900 = 600. "
        "Vậy A = T = 600 nucleotide; G = C = 900 nucleotide."),
    _essay("Điều chế kim loại", "Câu 4 (1,0 điểm). Điện phân nóng chảy 1,53 tấn Al₂O₃.\nA) Viết phương trình hóa học xảy ra.",
        "2Al₂O₃ → 4Al + 3O₂ (điện phân nóng chảy, xúc tác criolit). (0,5 điểm)", lines=3),
    _fill("Tính theo phương trình hóa học", "Câu 4 (1,0 điểm). Điện phân nóng chảy 1,53 tấn Al₂O₃.\nB) Giả thiết hiệu suất 90%, thì thu được khối lượng nhôm là bao nhiêu kilogam?\n"
        "Nhập số kg (chỉ gõ số).",
        "729",
        "2Al₂O₃ → 4Al + 3O₂: cứ 2·102 = 204 g Al₂O₃ cho 4·27 = 108 g Al. Với 1,53 tấn Al₂O₃: m(Al) lí thuyết = 1,53 · 108 : 204 = 0,81 tấn. "
        "Hiệu suất 90% ⇒ m(Al) thực tế = 0,81 · 90/100 = 0,729 tấn = 729 kg. "
        "LƯU Ý: hướng dẫn chấm gốc ghi 0,792 tấn = 792 kg là sai số học (0,81 × 0,9 = 0,729).",
        alt=["0,729", "729kg", "0,729tấn"]),
]

# ───────────────────────────── ĐỀ 3 ─────────────────────────────
_S3_TN = "Phần I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu × 0,25 = 5,0 điểm)"
_S3_TF = "Phần II. Câu trắc nghiệm đúng sai (2,0 điểm)"
_S3_TL = "Phần III. Tự luận (3,0 điểm)"

_DE_3 = [
    _mc("Khúc xạ ánh sáng", "Câu 1. Theo định luật khúc xạ thì",
        ["tia khúc xạ và tia tới nằm trong cùng một mặt phẳng.", "góc khúc xạ bao giờ cũng khác 0.",
         "góc tới tăng bao nhiêu lần thì góc khúc xạ tăng bấy nhiêu lần.", "góc tới luôn luôn lớn hơn góc khúc xạ."], "A",
        "Định luật khúc xạ: tia khúc xạ nằm trong mặt phẳng tới (cùng mặt phẳng với tia tới và pháp tuyến). "
        "B sai (tia tới vuông góc mặt phân cách thì góc khúc xạ bằng 0); C sai (góc tới và góc khúc xạ không tỉ lệ thuận); D sai (khi ánh sáng đi từ nước ra không khí thì góc tới nhỏ hơn góc khúc xạ).",
        section=_S3_TN, instr="Mỗi câu chỉ chọn một phương án."),
    _mc("Khúc xạ ánh sáng", "Câu 2. Trong hiện tượng khúc xạ ánh sáng, góc khúc xạ (r) là góc tạo bởi",
        ["tia khúc xạ và pháp tuyến tại điểm tới.", "tia khúc xạ và tia tới.", "tia khúc xạ và mặt phân cách.", "tia khúc xạ và điểm tới."], "A",
        "Góc khúc xạ r là góc hợp bởi tia khúc xạ và pháp tuyến tại điểm tới (tương tự góc tới i là góc giữa tia tới và pháp tuyến)."),
    _mc("Khúc xạ ánh sáng", "Câu 3. Chiết suất tuyệt đối của một môi trường là chiết suất tỉ đối của môi trường đó so với",
        ["chính nó.", "chân không.", "không khí.", "nước."], "B",
        "Chiết suất tuyệt đối của một môi trường là chiết suất tỉ đối của môi trường đó đối với chân không (chiết suất tuyệt đối của chân không bằng 1)."),
    _mc("Thấu kính", "Câu 4. Tia tới song song với trục chính của thấu kính hội tụ cho tia ló",
        ["đi qua tiêu điểm chính của thấu kính.", "song song với trục chính của thấu kính.",
         "cắt trục chính của thấu kính tại một điểm bất kì.", "có đường kéo dài đi qua tiêu điểm của thấu kính."], "A",
        "Tính chất của thấu kính hội tụ: tia tới song song với trục chính cho tia ló đi qua tiêu điểm F'. "
        "(Đáp án D là tính chất của thấu kính phân kì: tia ló có đường kéo dài đi qua tiêu điểm.)"),
    _mc("Định luật Ôm", "Câu 5. Để tìm hiểu sự phụ thuộc của cường độ dòng điện vào hiệu điện thế giữa hai đầu dây dẫn ta tiến hành thí nghiệm",
        ["Đo hiệu điện thế giữa hai đầu dây dẫn với những cường độ dòng điện khác nhau.",
         "Đo cường độ dòng điện chạy qua dây dẫn ứng với các hiệu điện thế khác nhau đặt vào hai đầu dây dẫn.",
         "Đo điện trở của dây dẫn với những hiệu điện thế khác nhau.",
         "Đo điện trở của dây dẫn với những cường độ dòng điện khác nhau."], "B",
        "Muốn khảo sát I phụ thuộc U ta thay đổi hiệu điện thế U đặt vào hai đầu dây dẫn (cùng một dây) và đo cường độ dòng điện I tương ứng; từ đó rút ra I tỉ lệ thuận với U."),
    _mc("Định luật Ôm", "Câu 6. Mắc một dây dẫn có điện trở R = 12 Ω vào hiệu điện thế 3 V thì cường độ dòng điện qua nó là",
        ["36 A.", "4 A.", "2,5 A.", "0,25 A."], "D",
        "I = U/R = 3 : 12 = 0,25 A."),
    _mc("Dãy hoạt động hóa học", "Câu 7. Dãy kim loại được sắp xếp theo chiều hoạt động hoá học giảm dần là:",
        ["Ag, Fe, Zn, Al, Mg, K.", "K, Mg, Al, Zn, Fe, Ag.", "Ag, Al, Zn, Fe, Mg, K.", "K, Mg, Fe, Zn, Al, Ag."], "B",
        "Dãy hoạt động hóa học: K, Na, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au. Giảm dần: K > Mg > Al > Zn > Fe > Ag → dãy B."),
    _mc("Tính chất vật lí của kim loại", "Câu 8. Aluminium (nhôm) được dùng làm giấy gói thực phẩm, bánh kẹo… vì có tính chất sau:",
        ["Dẫn nhiệt", "Tính dẫn điện", "Tính ánh kim", "Tính dẻo"], "D",
        "Nhôm có tính dẻo nên có thể cán thành lá mỏng (giấy bạc) để gói thực phẩm, bánh kẹo."),
    _mc("Kim loại tác dụng với muối", "Câu 9. Cho hỗn hợp kim loại Al, Fe và Cu vào dung dịch Cu(NO₃)₂ dư, chất rắn thu được sau phản ứng là",
        ["Fe.", "Al.", "Cu.", "Al và Cu."], "C",
        "Al và Fe hoạt động mạnh hơn Cu nên đều phản ứng với Cu(NO₃)₂ dư và tan hết: 2Al + 3Cu(NO₃)₂ → 2Al(NO₃)₃ + 3Cu; Fe + Cu(NO₃)₂ → Fe(NO₃)₂ + Cu. "
        "Cu ban đầu không phản ứng. Chất rắn sau phản ứng chỉ gồm Cu (cả Cu ban đầu và Cu mới sinh ra)."),
    _mc("Kim loại tác dụng với muối", "Câu 10. Ngâm một viên Zinc (kẽm) sạch trong dung dịch CuSO₄. Câu trả lời nào sau đây là đúng nhất cho hiện tượng quan sát được?",
        ["Không có hiện tượng nào xảy ra.",
         "Một phần viên kẽm bị hòa tan, có một lớp màu đỏ bám ngoài viên kẽm và màu xanh lam của dung dịch nhạt dần.",
         "Không có chất mới nào sinh ra, chỉ có một phần viên kẽm bị hòa tan.",
         "Kim loại đồng màu đỏ bám ngoài viên kẽm, viên kẽm không bị hòa tan."], "B",
        "Zn + CuSO₄ → ZnSO₄ + Cu. Kẽm tan một phần, đồng màu đỏ bám ngoài viên kẽm, dung dịch CuSO₄ xanh lam nhạt màu dần vì Cu²⁺ bị khử thành Cu."),
    _mc("Nhôm tác dụng với acid", "Câu 11. Cho 1,08 gam Aluminium (nhôm) tác dụng với hydrochloric acid dư, sau phản ứng thu được V lít khí H₂ ở đkc. Giá trị của V là",
        ["1,487 lít", "2,479 lít", "3,719 lít", "4,958 lít"], "A",
        "n(Al) = 1,08 : 27 = 0,04 mol. PTHH: 2Al + 6HCl → 2AlCl₃ + 3H₂ ⇒ n(H₂) = 0,04 · 3/2 = 0,06 mol. V(H₂) = 0,06 · 24,79 = 1,4874 ≈ 1,487 lít."),
    _mc("Carbon", "Câu 12. Do có tính hấp phụ, nên carbon vô định hình được dùng làm",
        ["điện cực, chất khử.", "trắng đường, mặt nạ phòng hơi độc.", "ruột bút chì, chất bôi trơn.", "mũi khoan, dao cắt kính."], "B",
        "Carbon vô định hình (than gỗ, than hoạt tính) có tính hấp phụ nên dùng khử màu (trắng đường) và làm mặt nạ phòng độc. "
        "Ruột bút chì, chất bôi trơn là graphite; mũi khoan, dao cắt kính là kim cương; điện cực là graphite."),
    _mc("Hợp chất của phi kim", "Câu 13. Chất được dùng để tẩy trắng giấy và bột giấy trong công nghiệp là",
        ["N₂O.", "CO₂.", "SO₂.", "NO₂."], "C",
        "Khí sulfur dioxide (SO₂) có tính tẩy màu nên được dùng tẩy trắng giấy, bột giấy trong công nghiệp."),
    _mc("Chlorine", "Câu 14. Trong các chất sau, chất nào được ứng dụng để sản xuất nước Javel, chất tẩy rửa?",
        ["Carbon.", "Lưu huỳnh.", "Silicon.", "Chlorine."], "D",
        "Nước Javel (NaCl + NaClO + H₂O) được sản xuất bằng cách cho chlorine tác dụng với dung dịch NaOH: Cl₂ + 2NaOH → NaCl + NaClO + H₂O."),
    _mc("Chlorine", "Câu 15. Khi mở vòi nước máy, nếu chú ý một chút sẽ phát hiện mùi lạ. Đó là do nước máy còn lưu giữ vết tích của thuốc sát trùng. "
        "Đó chính là chlorine và người ta giải thích khả năng diệt khuẩn là do",
        ["chlorine độc nên có tính sát trùng.", "chlorine có tính oxi hóa mạnh.",
         "chlorine tác dụng với nước tạo ra HClO chất này có tính oxi hóa mạnh.", "một nguyên nhân khác."], "C",
        "Cl₂ + H₂O ⇌ HCl + HClO. Acid hypochlorous (HClO) có tính oxi hóa mạnh nên diệt khuẩn; đó là cách giải thích chính xác nhất cho khả năng sát trùng của nước chlorine."),
    _mc("Phi kim", "Câu 16. Cho thông tin sau:\n"
        "- Khí X rất độc, không cháy, hoà tan trong nước, nặng hơn không khí và có tính tẩy màu.\n"
        "- Khí Y rất độc, cháy trong không khí với ngọn lửa màu xanh sinh ra chất khí làm đục nước vôi trong.\n"
        "- Khí Z không cháy, nặng hơn không khí, làm đục nước vôi trong.\n"
        "X, Y, Z lần lượt là",
        ["Cl₂, CO, CO₂.", "Cl₂, SO₂, CO₂.", "SO₂, H₂, CO₂.", "H₂, CO, SO₂."], "A",
        "X: Cl₂ (khí độc, tan trong nước, tẩy màu khi có nước, không cháy). Y: CO (rất độc, cháy ngọn lửa xanh tạo CO₂ làm đục nước vôi trong). "
        "Z: CO₂ (không cháy, nặng hơn không khí, làm đục nước vôi trong). B sai vì SO₂ không cháy; C, D sai vì H₂ không độc, nhẹ hơn không khí."),
    _mc("Di truyền học", "Câu 17. Di truyền học là",
        ["khoa học nghiên cứu về tính di truyền và biến dị ở các sinh vật.", "khoa học nghiên cứu về tính sinh sản và sinh trưởng ở sinh vật.",
         "khoa học nghiên cứu về tính di truyền và sinh sản ở các sinh vật.", "khoa học nghiên cứu về tính sinh sản và biến dị ở các sinh vật."], "A",
        "Di truyền học là khoa học nghiên cứu về tính di truyền và biến dị của sinh vật."),
    _mc("Gene và DNA", "Câu 18. Một gene chứa đoạn mạch có trình tự nucleotide là\n"
        "3'… A – G – C – T – T – A – G – C – A …5'.\nTrình tự nucleotide tương ứng trên mạch bổ sung là",
        ["5'… T – C – G – A – A – T – C – G – T …3'", "3'… T – C – G – A – A – T – C – G – T …5'",
         "5'… U – C – G – A – A – U – C – G – U …3'", "5'… U – C – T – A – A – U – C – G – U …3'"], "A",
        "Mạch bổ sung bắt cặp theo nguyên tắc A–T, G–C và đối song song với mạch đã cho: A→T, G→C, C→G, T→A, T→A, A→T, G→C, C→G, A→T, "
        "đọc được T–C–G–A–A–T–C–G–T, đầu 3' của mạch đã cho đối diện đầu 5' của mạch bổ sung ⇒ 5'…T–C–G–A–A–T–C–G–T…3'. "
        "B sai chiều (3'…5'); C, D chứa U nên là RNA chứ không phải mạch DNA. "
        "LƯU Ý: đáp án gốc ghi C (trình tự mRNA). Với lời hỏi 'mạch bổ sung' của gene thì đáp án đúng là A; chỉ khi đề hỏi trình tự trên mRNA (mạch đã cho làm khuôn) mới chọn C."),
    _mc("Đột biến gene", "Câu 19. Đột biến nào sau đây xảy ra trên gene không làm thay đổi số nucleotide của gene nhưng làm thay đổi số lượng liên kết hydrogen trong gene?",
        ["Mất một cặp nucleotide.", "Thêm một cặp nucleotide.", "Thay cặp nucleotide A – T bằng cặp T – A.", "Thay cặp nucleotide A – T bằng cặp G – C."], "D",
        "Thay cặp nucleotide giữ nguyên tổng số nucleotide. Cặp A–T có 2 liên kết hydrogen, cặp G–C có 3 liên kết hydrogen nên thay A–T bằng G–C làm số liên kết hydrogen tăng 1. "
        "Thay A–T bằng T–A không đổi số liên kết hydrogen; mất hoặc thêm một cặp làm đổi số nucleotide."),
    _mc("Di truyền Mendel", "Câu 20. Theo quan niệm của Mendel, mỗi tính trạng của cơ thể do",
        ["một cặp nhân tố di truyền quy định.", "hai nhân tố di truyền khác loại quy định.",
         "một nhân tố di truyền quy định.", "hai cặp nhân tố di truyền quy định."], "A",
        "Theo Mendel, mỗi tính trạng do một cặp nhân tố di truyền (nay gọi là cặp allele) quy định."),

    # ── Phần II: Đúng/Sai ──
    _tf("Cơ năng", "Câu 1a. Thả một vật có khối lượng 0,5 kg từ một độ cao cách mặt đất 5 m. Chọn gốc thế năng ở mặt đất, biết toàn bộ thế năng của vật chuyển hóa thành động năng của vật. Bỏ qua lực cản của không khí.\n"
        "a) Ở độ cao 5 m so với mặt đất thì thế năng của vật tính bằng công thức Wt = P·h.", True,
        "Thế năng trọng trường Wt = P·h = 10·m·h, với P là trọng lượng của vật, h là độ cao so với mốc thế năng.",
        section=_S3_TF, instr="Trong mỗi ý a), b), c), d) ở mỗi câu, em chọn Đúng hoặc Sai. (1 ý đúng: 0,1 đ; 2 ý: 0,25 đ; 3 ý: 0,5 đ; cả 4 ý: 1,0 đ)"),
    _tf("Cơ năng", "Câu 1b. (Vật 0,5 kg thả từ độ cao 5 m, gốc thế năng ở mặt đất, bỏ qua lực cản.)\n"
        "b) Khi vật chạm đất thì cơ năng của vật chỉ có ở dạng động năng.", True,
        "Chạm đất: độ cao h = 0 nên thế năng bằng 0; cơ năng được bảo toàn nên toàn bộ cơ năng (25 J, xem câu d) chuyển thành động năng."),
    _tf("Cơ năng", "Câu 1c. (Vật 0,5 kg thả từ độ cao 5 m, gốc thế năng ở mặt đất, bỏ qua lực cản.)\n"
        "c) Trong quá trình vật đang rơi, thế năng của vật giảm, động năng của vật tăng.", True,
        "Vật rơi: độ cao giảm nên thế năng giảm; vận tốc tăng nên động năng tăng; thế năng chuyển hóa dần thành động năng."),
    _tf("Cơ năng", "Câu 1d. (Vật 0,5 kg thả từ độ cao 5 m, gốc thế năng ở mặt đất, bỏ qua lực cản.)\n"
        "d) Thế năng của vật ở độ cao 5 m là 2,5 J.", False,
        "Trọng lượng P = 10·m = 10·0,5 = 5 N. Thế năng Wt = P·h = 5·5 = 25 J, không phải 2,5 J."),
    _tf("Di truyền phân li độc lập", "Câu 2a. Cơ sở tế bào học của quy luật phân li độc lập:\n"
        "a) Các cặp gene dị hợp nằm trên các nhiễm sắc thể tương đồng khác nhau.", True,
        "Mỗi cặp gene nằm trên một cặp nhiễm sắc thể tương đồng riêng; vì các cặp nhiễm sắc thể phân li độc lập nên các cặp gene cũng phân li độc lập."),
    _tf("Di truyền phân li độc lập", "Câu 2b. (Cơ sở tế bào học của quy luật phân li độc lập.)\n"
        "b) Sự phân li của các cặp gene không liên quan đến sự phân li của các nhiễm sắc thể.", False,
        "Sai: gene nằm trên nhiễm sắc thể nên sự phân li của các cặp gene gắn liền với sự phân li của các cặp nhiễm sắc thể tương đồng trong giảm phân."),
    _tf("Di truyền phân li độc lập", "Câu 2c. (Cơ sở tế bào học của quy luật phân li độc lập.)\n"
        "c) Các cặp gene luôn di truyền cùng nhau.", False,
        "Sai: các cặp gene phân li độc lập, tổ hợp tự do; chỉ các gene liên kết (cùng nằm trên một nhiễm sắc thể) mới di truyền cùng nhau."),
    _tf("Di truyền phân li độc lập", "Câu 2d. (Cơ sở tế bào học của quy luật phân li độc lập.)\n"
        "d) Sự tổ hợp ngẫu nhiên của các giao tử trong quá trình thụ tinh cho tỉ lệ kiểu hình F₂ là 9 : 3 : 3 : 1.", True,
        "Các giao tử (4 loại, tỉ lệ bằng nhau) tổ hợp ngẫu nhiên khi thụ tinh cho 16 tổ hợp, F₂ có tỉ lệ kiểu hình 9 : 3 : 3 : 1 (với hai cặp tính trạng, trội hoàn toàn)."),

    # ── Phần III: Tự luận ──
    _essay("Thấu kính", "Câu 1 (0,5 điểm). Sử dụng các tia sáng tới thấu kính hội tụ dựng ảnh của vật (điểm sáng A) trong hình sau.",
        "Vẽ hai trong ba tia đặc biệt xuất phát từ A: tia tới song song với trục chính cho tia ló đi qua tiêu điểm F' (bên kia thấu kính); "
        "tia tới qua quang tâm O truyền thẳng. Hai tia ló cắt nhau tại A' (phía dưới trục chính, bên phải thấu kính) — A' là ảnh thật của A. "
        "(Vật A nằm ngoài khoảng tiêu cự nên cho ảnh thật.)",
        lines=4, section=_S3_TL, image="de3_tl_cau1.png"),
    _fill("Định luật Ôm", "Câu 2 (0,5 điểm). Khi đặt vào hai đầu dây dẫn một hiệu điện thế 6 V thì cường độ dòng điện qua nó là 0,5 A. "
        "Nếu hiệu điện thế đặt vào hai đầu dây dẫn là 24 V thì cường độ dòng điện qua nó là bao nhiêu ampe?\nNhập số (A).",
        "2",
        "Điện trở của dây dẫn: R = U/I = 6 : 0,5 = 12 Ω (không đổi). Khi U' = 24 V: I' = U'/R = 24 : 12 = 2 A. "
        "(Cũng có thể dùng I tỉ lệ thuận với U: U tăng 4 lần thì I tăng 4 lần → 0,5 × 4 = 2 A.)",
        alt=["2a", "2 a"]),
    _fill("Kim loại tác dụng với acid", "Câu 3 (1 điểm). Cho 10,5 gam hỗn hợp hai kim loại Zn, Cu vào dung dịch H₂SO₄ loãng dư, người ta thu được 2,479 lít khí (đkc). "
        "Tính thành phần phần trăm theo khối lượng mỗi kim loại trong hỗn hợp ban đầu.\n"
        "Nhập dạng %Zn;%Cu (làm tròn 1 chữ số thập phân, dấu phẩy thập phân, không gõ ký hiệu %), ví dụ 50,5;49,5.",
        "61,9;38,1",
        "n(H₂) = 2,479 : 24,79 = 0,1 mol. Chỉ Zn phản ứng: Zn + H₂SO₄ → ZnSO₄ + H₂↑ ⇒ n(Zn) = 0,1 mol (Cu không tác dụng với H₂SO₄ loãng). "
        "m(Zn) = 0,1·65 = 6,5 g ⇒ %m(Zn) = 6,5/10,5 · 100% ≈ 61,9%; %m(Cu) = 100% − 61,9% = 38,1%.",
        alt=["61,9%;38,1%", "61,90;38,10"]),
    _essay("Di truyền Mendel", "Câu 4 (1 điểm). Trình bày phép lai phân tích của Mendel.",
        "Mendel đem cây hoa tím chưa biết kiểu gene lai với cây hoa trắng thuần chủng (đồng hợp lặn), rồi phân tích thế hệ lai để kết luận về kiểu gene của cây hoa tím (0,25 điểm). "
        "Nếu cây hoa tím đồng hợp (thuần chủng) thì kết quả lai đồng tính: 100% hoa tím (0,25 điểm). "
        "Nếu cây hoa tím dị hợp (không thuần chủng) thì kết quả lai phân tính: 50% hoa tím : 50% hoa trắng (0,25 điểm). "
        "Viết được sơ đồ lai (0,25 điểm): AA × aa → 100% Aa (hoa tím); Aa × aa → 1 Aa (hoa tím) : 1 aa (hoa trắng).", lines=8),
]

EXAMS = {1: _DE_1, 2: _DE_2, 3: _DE_3}
