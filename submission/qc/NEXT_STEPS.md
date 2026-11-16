# Việc còn lại sau khi bổ sung 101 và 102

Trạng thái **Hold**. Hai COCO đã có đủ 40 ảnh, không còn thiếu nhãn/ghi chú 101. Hai bản dùng chung nguồn prelabel nên chưa có bằng chứng gán độc lập.

1. Đọc IAA_LIMITATIONS.md trước iaa_summary.md. Nếu cần IAA độc lập, tổ chức lại lượt gán theo coach. Không coi cùng prelabel là hai lượt độc lập. Đổi đầu vào thì lưu hồ sơ cũ, chạy so sánh lại và tạo bảng calibration mới.
2. Đi từng ca C001–C996 theo calibration_worklist.csv và từng ảnh theo calibration_image_queue.csv. Các bảng này là danh sách xử lý, không phải quyết định đã đóng. Kiểm R-06 trên 95 bất đồng mức che, R-17 trên bốn box img_014, R-05 trên car img_019; xem ảnh gốc và overlay.
3. Xác nhận/sửa đề xuất guideline và taxonomy v1.1 theo GUIDELINE_DISCUSSION.md. Thay đổi semantic cần quyết định phạm vi lo và kiểm lại toàn bộ 40 ảnh; không sửa rules.
4. Điền đủ 9 cột calibration_decisions.csv theo quyết định thực: người chốt, dấu vết sửa, người kiểm lại. Không điền hàng loạt “đã kiểm” để script qua.
5. Chốt quyết định/phiên bản rồi chạy:

```powershell
python -X utf8 scripts/validate_labels.py --all
python -X utf8 scripts/prepare_calibration.py
```

Lệnh thứ hai in đường dẫn COCO có hash. Sửa đúng phạm vi và export đúng đường dẫn. Quyết định/guideline/taxonomy đổi thì phải chuẩn bị lại, dùng hash mới.

```powershell
python -X utf8 scripts/build_final.py
python -X utf8 scripts/qc_sample.py --round 1
```

6. Duyệt 40 ảnh overlay trong work/review/round-01, điền phiếu QC đúng object_id/rule/vùng. Chỉ tắt can_review khi đã xử lý ca; người kiểm nên khác người sửa, ghi rõ vai trò thực.

```powershell
python -X utf8 scripts/qc_report.py --round 1
python -X utf8 scripts/check_submission.py --round 1
python -X utf8 submission/qc/evidence_audit.py
```

7. Cập nhật QC_REPORT.md, TEAM.md, checklist và gói zip. Rework thì giữ vòng cũ, mở vòng mới. 0 lỗi cấu trúc không thay kiểm nội dung hoặc xác nhận độc lập.
8. người đánh giá chấm theo REVIEW_CHECKLIST.md và rubric_scorecard.csv; ghi điểm từng tiêu chí, dẫn bằng chứng và lý do trừ. Không tự cho điểm vì đủ tên file.

Dùng -X utf8 trên Windows tránh lỗi in tiếng Việt. Không nộp work/, .git/, token hoặc thông tin đăng nhập. Gói hiện tại là hồ sơ Hold.
