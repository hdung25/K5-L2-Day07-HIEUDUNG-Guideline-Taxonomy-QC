# Trạng thái bàn giao và cách kiểm lại

Đã hoàn tất xử lý nhãn, calibration, manifest, hai vòng QC và kiểm bài. Vòng cuối là round-02; giữ round-01 như bằng chứng lỗi đã sửa.

1. Đọc QC_REPORT.md và IAA_LIMITATIONS.md để phân biệt chất lượng nhãn cuối với giới hạn độc lập của hai bản đầu vào.
2. Chạy validate_labels.py --all, check_submission.py --round 2 và evidence_audit.py. Kết quả hiện tại đều đạt kiểm kỹ thuật, không còn artifact bắt buộc bị thiếu.
3. Kiểm ngược Q002 từ phiếu vòng 1 tới img_010, person #139 vòng 2 và final_object_map.csv. Xem overlay từng ảnh trong reviews/round-02/overlays.
4. Người đánh giá điền rubric_scorecard.csv theo bằng chứng, không tự gán điểm 92 hoặc coi IoU cao là bằng chứng độc lập.
5. Nếu reviewer phát hiện lỗi mới, thêm Q003..., lưu sửa đúng tên hash prepare_calibration.py, chạy build_final rồi mở round-03; không ghi đè các vòng cũ.
6. Nếu cần đáp ứng tiêu chí gán mù độc lập của lớp, phải có lượt gán thật phù hợp coach; không thể khôi phục bằng cách đổi tên hai bản cùng nguồn.
7. Nộp link repo/gói qua kênh coach yêu cầu. Chưa nộp LMS thay người dùng.
