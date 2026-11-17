---
name: english-check
description: Chấm và giải thích chi tiết bài kiểm tra tiếng Anh (trắc nghiệm ngữ pháp, từ vựng, phát âm, trọng âm, câu gián tiếp, giao tiếp) cho Bảo Mèo, Minh Khanh, Nhật Khôi từ ảnh chụp sách/đề/vở. Dùng skill này mỗi khi user gửi ảnh hoặc text bài tiếng Anh và nói "check", "chấm", "kiểm tra các ý", "đúng sai", "giải thích", kể cả khi không nhắc tên skill. Cũng dùng khi cần xác minh đáp án tiếng Anh trong đề của repo.
---

# english-check

Mục tiêu: cho ra đáp án đúng, lý do ngữ pháp/ngữ âm cụ thể, và so với bài làm của bé, mà không nói chắc điều mình chưa chắc.

## Quy trình mỗi câu
1. Giải độc lập trước. Không nhìn dấu đỏ, khoanh tròn hay đáp án có sẵn trên ảnh, vì dấu có thể sai và sẽ làm lệch kết quả.
2. Ghi đáp án và lý do bằng quy tắc (vd "suggest + V-ing"), không dùng "nghe hợp lý".
3. Đọc dấu trên ảnh (khoanh, ✓, ghi tay). Nói rõ dấu nào đọc chưa chắc và giả thiết đang dùng; hỏi user nếu có thể.
4. Gắn tin cậy: cao / vừa / thấp / không biết. Ảnh nghiêng, mép che, chữ gạch chân mờ thì hạ tin cậy.
5. Gắn cờ lỗi đề thay vì ép ra một đáp án:
   - 2 đáp án cùng đúng
   - typo (Dessert/Desert, Zamberi/Zambezi)
   - thiếu mạo từ, danh từ số ít sau "a wide range of"
   Câu lỗi đề không tính sai cho bé.

## Bẫy hay gặp
- Câu gián tiếp Yes/No: whether/if + S + V, lùi thì khi động từ chính ở quá khứ. Sự thật hiển nhiên có thể giữ nguyên thì, nên "was" và "is" có thể cùng đúng.
- Verb + V-ing: suggest, avoid, enjoy, consider, finish. Verb + to V: decide, want, hope, plan.
- Trọng âm: động từ/tính từ 2 âm tiết thường rơi âm 2; danh từ 2 âm tiết thường âm 1; đuôi -ity, -ic, -ion kéo trọng âm về trước đuôi.
- Phát âm: ghi IPA của từng từ rồi so sánh, không đoán theo mặt chữ. g = /dʒ/ trước e, i, y trong nhiều từ, nhưng "together" là /ɡ/.
- Collocation: make a contribution to, stretch over (chiều dài/rộng), possess (sở hữu đặc điểm).

## Nguồn tra
Oxford Learner's Dictionaries hoặc Cambridge Dictionary cho phát âm/trọng âm; Cambridge Grammar cho ngữ pháp. Nếu không tra được, nói rõ "chưa tra từ điển" thay vì khẳng định.

## Đầu ra
- Tiếng Việt, gạch đầu dòng, bảng tổng hợp: câu | đáp án đúng | bé chọn | ✓/✗/⚠/— | lý do | tin cậy.
- Ký hiệu: ✓ đúng, ✗ sai, ⚠ lỗi đề hoặc dấu chưa rõ, — chưa làm.
- Cuối cùng liệt kê: câu lỗi đề, việc cần xác nhận (bài của bạn nào, ý nghĩa dấu đỏ).
- Lưu vào `checks/<ten_be>/<yyyy-mm-dd>_<ten_bai>.md` theo mẫu trong repo.
