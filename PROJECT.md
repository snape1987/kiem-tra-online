# PROJECT.md — Kiem Tra Online SuKhoiKem

## A. Định danh
1. **Tên:** Kiem Tra Online SuKhoiKem
2. **Key:** kiemtra
3. **Mô tả:** Webapp tạo đề kiểm tra (30/45/60/90 phút) cho HS lớp 1-9, đa môn, chấm điểm, lưu lịch sử
4. **Owner:** doanthaithien@gmail.com
5. **Loại:** webapp

## B. Mục tiêu
6. **Vấn đề:** Con cần luyện tập online, có chấm điểm và tổng kết điểm qua từng lần thi. Đề phải mix random không trùng lặp.
7. **KPI:** Con làm bài đều đặn, điểm trung bình tăng theo thời gian
8. **Deadline:** MVP lớp 1 - Toán: 15 phút (gấp). Mở rộng dần sau.
9. **Out-of-scope (MVP):** Multi-user, đăng nhập, in PDF — để sau

## C. Kỹ thuật
10. **Stack:** Python + Flask + SQLite + HTML/CSS thuần
11. **DB:** SQLite file `kiemtra.db` — bảng `attempts` (id, student, grade, subject, duration, score, total, created_at)
12. **API cần:** Không (offline)
13. **Secrets:** Không
14. **Port:** 5000

## D. Vận hành
15. **Backup:** Copy `kiemtra.db` định kỳ
16. **Rollback:** Git (nếu init)
17. **Log:** Flask default + console

## E. Ghi chú tự do (điền dần)
18. Cấu trúc đề: random N câu từ pool theo độ khó
19. Lớp 1 Toán: cộng/trừ trong 10, 20, 100; đếm; so sánh
20. Lớp 2 Toán: bảng cửu chương 2-5, +/- có nhớ
21. (todo) Thêm môn Tiếng Việt, Tiếng Anh
22. (todo) Trang dashboard tổng kết điểm
23. (todo) Chống trùng đề: lưu hash đề đã ra, không lặp trong N lần gần nhất
24. (todo) Timer countdown trên frontend
25. (todo) Random theo seed để reproducible khi cần
