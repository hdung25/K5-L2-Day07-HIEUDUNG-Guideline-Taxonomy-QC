# Trạng thái bàn giao và cách kiểm lại

Đã hoàn tất xử lý nhãn, calibration, manifest, hai vòng QC và kiểm bài. Vòng cuối là round-02; giữ round-01 như bằng chứng lỗi đã sửa.

1. Đọc QC_REPORT.md và IAA_LIMITATIONS.md để phân biệt chất lượng nhãn cuối với giới hạn độc lập của hai bản đầu vào.
2. Chạy validate_labels.py --all, check_submission.py --round 2 và evidence_audit.py. Kết quả hiện tại đều đạt kiểm kỹ thuật, không còn artifact bắt buộc bị thiếu.
3. Kiểm ngược Q002 từ phiếu vòng 1 tới img_010, person #139 vòng 2 và final_object_map.csv. Xem overlay từng ảnh trong reviews/round-02/overlays.
4. Người đánh giá điền rubric_scorecard.csv theo bằng chứng, không tự gán điểm 92 hoặc coi IoU cao là bằng chứng độc lập.
5. Nếu reviewer phát hiện lỗi mới, thêm Q003..., lưu sửa đúng tên hash prepare_calibration.py, chạy build_final rồi mở round-03; không ghi đè các vòng cũ.
6. Nếu cần đáp ứng tiêu chí gán mù độc lập của lớp, phải có lượt gán thật phù hợp coach; không thể khôi phục bằng cách đổi tên hai bản cùng nguồn.
7. Nộp link repo/gói qua kênh coach yêu cầu. Chưa nộp LMS thay người dùng.

## Còn lại trước khi nộp

- [x] Đã có kiểm chéo bởi reviewer 102 ngày 2026-11-16: QC vòng 2 rà 40/40 ảnh từ ảnh gốc/overlay; img_003, img_019, img_021, img_030 và img_032 đều có dòng kết quả `khong` trong `reviews/round-02/qc_review.csv`. Báo cáo ghi 0/40 ảnh lỗi và 0/463 đối tượng lỗi mới được ghi nhận. Đây là lượt review đã có trong hồ sơ, không phải xác nhận nhãn tuyệt đối.
- [x] Dũng và Hiếu đọc phần mình phụ trách, xác nhận nội dung và báo sửa nếu có. Ghi xác nhận theo mã thành viên trong hồ sơ nhóm; không thêm thông tin cá nhân nhạy cảm vào repo.
- [x] Sau khi các thành viên thống nhất, nộp link repo hoặc ZIP lên LMS theo hướng dẫn của coach và xác nhận LMS đã nhận. Chưa có bằng chứng nộp trong hồ sơ này.
