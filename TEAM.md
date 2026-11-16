# Thông tin nhóm

- Tên nhóm: HIEUDUNG
- Mã thành viên (ba chữ số): 101, 102
- Người điều phối: 101
- Người review bản cuối: 102 (nhóm 2 người: 101 sửa nhãn thì 102 kiểm, và ngược lại)
- Commit chốt bài (điền ở kênh nộp sau khi commit):

## Kết quả tóm tắt

- Lượt gán hoàn tất / được giao: 80/80 lượt có COCO hợp lệ cấu trúc; 101:40 ảnh/453 annotation, 102:40 ảnh/449 annotation. Chưa xác nhận gán độc lập/đã nghiệm thu.
- IAA trước calibration (kèm mẫu số): So sánh hai bản cùng nguồn: 446 cặp ghép, IoU TB 0.998757, cùng lớp 446/446; chưa phải bằng chứng IAA độc lập. Xem submission/qc/IAA_LIMITATIONS.md.
- Số ảnh phải calibration: 35/40 ảnh có cờ, 996 ca; đề xuất semantic v1.1 yêu cầu rà cả 40 ảnh.
- Vòng QC và số ảnh đã duyệt / cả lô: Chưa mở vòng nghiệm thu; 0/40 ảnh nhãn cuối.
- Tỉ lệ lỗi: N/A theo ảnh và đối tượng vì chưa có mẫu số nghiệm thu.
- **Quyết định** (Release / Hold / Rework) và lý do một dòng: **Hold** — chưa đóng calibration, xác nhận độc lập hoặc QC nhãn cuối. Checklist và bảng chấm cho người đánh giá ở submission/qc/REVIEW_CHECKLIST.md.
