# Thông tin nhóm

- Tên nhóm: HIEUDUNG
- Mã thành viên (ba chữ số): 101, 102
- Người điều phối: 101
- Người review bản cuối: 102 (nhóm 2 người: 101 sửa nhãn thì 102 kiểm, và ngược lại)
- Mốc chốt bài: tag `day07-final-v1.1` trên repo; chưa nộp LMS thay người dùng.

## Kết quả tóm tắt

- Lượt gán hoàn tất / được giao: 80/80 COCO hợp lệ cấu trúc; hai phiên bản cùng nguồn, không xác nhận gán mù độc lập.
- IAA trước calibration (kèm mẫu số): 446 cặp, IoU TB 0.998757, cùng lớp 446/446; chỉ so sánh phiên bản, giới hạn ở submission/qc/IAA_LIMITATIONS.md.
- Số ảnh phải calibration: 35/40 ảnh bị cờ; thay đổi semantic v1.1 đã áp dụng và rà cả 40/40.
- Quyết định calibration: 996 ca nguồn +Q001 toàn lô +Q002 sửa sau QC, tổng 998 dòng có dấu vết.
- Nhãn cuối: 40 ảnh, 467 annotation (463 đối tượng +4 ignore_region); 0 cờ can_review.
- Vòng QC và số ảnh đã duyệt / cả lô: Vòng 2, 40/40; giữ nguyên bằng chứng vòng 1.
- Tỉ lệ lỗi: Vòng 2:0/40 ảnh=0.0%, 0/463 đối tượng=0.0%, 0 bỏ sót mới ghi nhận. Vòng 1 có 1/40 ảnh lỗi và 1 person bỏ sót, đã sửa.
- **Quyết định** (Release / Hold / Rework) và lý do một dòng: **Release** nhãn lô thực hành sau QC vòng 2; giới hạn IAA độc lập vẫn được công khai trong hồ sơ.
- Mốc bàn giao repo: tag day07-final-v1.1; xem lịch sử Git để lấy commit chính xác.
