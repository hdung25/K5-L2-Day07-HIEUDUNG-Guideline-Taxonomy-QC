# Chỉ mục bằng chứng

- `evidence_status.json`: kết quả kiểm hiện hành; `validate_labels_latest.txt` đạt, `check_submission_latest.txt` còn 1 lỗi do chưa có vòng QC nhãn cuối.
- `iaa_summary.json/.md`, `calibration_candidates.csv`, `image_scores.csv`, `flagged_images.txt`, `consensus_draft.json`: đầu ra gốc của script, không sửa tay. Đọc kèm `IAA_LIMITATIONS.md`.
- `calibration_decisions.csv`: 996 ca, chưa có quyết định được xác nhận; ô trống thể hiện việc còn lại. Không thay bằng dòng tự xác nhận.
- `calibration_context.json`: khóa summary hiện hành; thay đầu vào phải lưu hồ sơ cũ và tái tạo.
- `calibration_worklist.csv`: 996 gợi ý thao tác/rule, không phải quyết định đã chốt.
- `calibration_image_queue.csv`: 40 ảnh, giúp đi theo từng ảnh; không phải 40 phiếu đã nghiệm thu.
- `source_labels.json`: nguồn nguyên bản dùng chung cho hai file nháp, được giữ để đối chiếu SHA-256. Không chứng minh độc lập.
- `member_101/changes.csv`, `member_102/changes.csv`: nhật ký sửa sơ bộ; `provenance.json` trong từng thư mục khóa checksum của bản làm việc.
- `member_102/observations.md`: quan sát sơ bộ nguồn trước sửa 101; các box đề cập cần đối chiếu bản nhãn hiện hành.
- `member_102/submission_check.txt`: log lịch sử thời điểm chưa bổ sung 101; dùng `check_submission_latest.txt` cho trạng thái hiện tại.
- `QC_REPORT.md`, `GUIDELINE_DISCUSSION.md`, `NEXT_STEPS.md`: báo cáo Hold, đối chiếu đặc tả và thứ tự tiếp tục.
- `REVIEW_CHECKLIST.md`, `rubric_scorecard.csv`: checklist và phiếu chấm 21 tiêu chí /100; điểm để trống cho người đánh giá.

Tên `guideline_v1.1_calibrated.md` và `labels_final.json` theo quy ước pipeline; nội dung v1.1 hiện là **đề xuất chưa xác nhận**, không phải kết quả calibration đã hoàn tất. Các file nhãn cuối/manifest/QC chưa được tạo vì gate calibration chưa đạt.
