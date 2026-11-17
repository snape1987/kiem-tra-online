# TASKS — việc lặp lại của repo

## Task: Check bài kiểm tra giấy cho 3 bạn

Bạn: Bảo Mèo (lớp 2), Minh Khanh (lớp 7), Nhật Khôi (lớp 9).

### Đầu vào
- Ảnh/scan trang bài kiểm tra (sách, đề in, vở).
- Chỉ rõ: bạn nào, môn nào, câu nào cần check (vd "12 câu đầu").

### Quy trình (mỗi câu)
1. Tự giải độc lập TRƯỚC, không nhìn dấu đỏ/đáp án có sẵn trên ảnh.
2. Ghi đáp án mình + lý do ngữ pháp/ngữ âm cụ thể (quy tắc, không chỉ "nghe hợp lý").
3. Đối chiếu dấu trên ảnh (khoanh, ✓, ghi tay). Ghi rõ dấu nào đọc chưa chắc.
4. Gắn mức tin cậy: cao / vừa / thấp / không biết.
5. Gắn cờ câu lỗi đề: 2 đáp án cùng đúng, typo trong đề (vd "Dessert" thay "Desert"), câu thiếu mạo từ.
6. Câu nghi lỗi đề thì KHÔNG phạt bé, báo lại để hỏi giáo viên.

### Nguồn chuẩn ngữ pháp
- Skill `english-check` (`.claude/skills/english-check/SKILL.md`) chứa quy trình và các bẫy ngữ pháp hay gặp. Chưa chạy eval.
- Phát âm/trọng âm: Oxford Learner's Dictionaries hoặc Cambridge Dictionary. Không đoán theo cảm giác.
- Ngữ pháp: Cambridge Grammar / Oxford (reported speech, verb + V-ing, collocation).

### Đầu ra
- File `checks/<ten_be>/<yyyy-mm-dd>_<ten_bai>.md`.
- Bảng: câu | đáp án đúng | bé chọn | kết quả | tin cậy | ghi chú.
- Cuối file: danh sách câu lỗi đề + việc cần xác nhận.

### Đã làm
- [x] Nhật Khôi (đã xác nhận; khoanh đỏ = bé chọn) — Anh 9, Unit 7 Practice Test, câu 1–12: `checks/nhat_khoi/2026-11-17_anh9_unit7_practice_test_q1-12.md`
