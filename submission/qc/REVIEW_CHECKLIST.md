# Checklist bàn giao và đánh giá

## Kiểm kỹ thuật đã hoàn tất

- [x] Hai guideline cá nhân và hai ghi chú 101/102.
- [x] Guideline v1.0 và taxonomy đã khóa; v1.1 semantic áp dụng cả lô; rules giữ nguyên.
- [x] Hai COCO đúng phân công:40 ảnh/mã, 80/80 lượt về cấu trúc; validate_labels --all đạt.
- [x] Giữ nguyên đầu vào và kết quả so sánh trước calibration, kèm giới hạn IAA.
- [x] C001–C996 có quyết định riêng; Q001 toàn lô và Q002 sửa lỗi sau QC.
- [x] calibration_edits.json lưu từng instance trước/sau; final_object_map.csv nối ID nguồn/ID nhãn cuối.
- [x] COCO sau sửa đúng hash; labels_calibrated.json/.csv và batch_manifest.json khớp checksum.
- [x] Nhãn cuối:40 ảnh, 467 annotation, 463 đối tượng, 4 ignore_region, 0 cờ review.
- [x] QC round-01 duyệt 40 ảnh, ghi nhận1 bỏ sót và1 điều khoản cần chốt; giữ snapshot.
- [x] Đã sửa Q002, cập nhật điều khoản img_011, mở round-02 và đối chiếu 40/40.
- [x] QC vòng 2:0/40 ảnh lỗi, 0/463 đối tượng lỗi, 0 bỏ sót mới ghi nhận; script trả Release.
- [x] check_submission.py --round 2:0 lỗi.
- [x] Kiểm ngược Q002 và kiểm hash đầu vào/artifact/manifest.
- [x] Ảnh overlay cuối đủ40 ảnh trong repo; không kèm work hoặc thông tin đăng nhập.
- [x] Bảng chấm21 tiêu chí, tổng tối đa100, để người đánh giá điền điểm/lý do.

## Giới hạn không được suy diễn

- Hai bộ nhãn đầu vào cùng nguồn, không phải bằng chứng hai người gán mù độc lập. Mã101/102 là vai trò phụ trách/đối chiếu trong hồ sơ chung.
- Chưa có chữ ký riêng của hai cá nhân, biên bản họp hoặc reviewer ngoài nhóm. Không tạo commit giả danh thành viên để lấp yêu cầu hợp tác.
- Không có nhãn chuẩn tuyệt đối; 0 lỗi là kết quả lượt kiểm, reviewer vẫn có thể phát hiện lỗi mới.
- Release nhãn sau QC không tự bảo đảm92 điểm. Chấm đúng từng mục RUBRIC.md và trừ phần thiếu bằng chứng độc lập/hợp tác theo đánh giá.

## Bảng điểm tổng quát

| Mục | Tối đa | Bằng chứng chính |
|---|---:|---|
| Guideline cá nhân |15|guidelines/individual, individual_notes|
| Guideline nhóm/taxonomy |20|v1.0, v1.1, taxonomy, GUIDELINE_DISCUSSION|
| Phân công và gán độc lập |15|assignment, labels; đọc giới hạn độc lập|
| IAA/calibration |25|summary,998 quyết định, edits, nhãn cuối|
| QC/báo cáo |15|round-01/02, QC_REPORT, manifest|
| Tái lập/hợp tác |10|0 lỗi kiểm bài, test_results, hồ sơ bàn giao; giới hạn hợp tác|
|Tổng|100|rubric_scorecard.csv để trống điểm cho người chấm|

Người đánh giá:đọc RUBRIC.md, RULES.md, GUIDE_ALIGNMENT.md, QC_REPORT.md và IAA_LIMITATIONS.md; kiểm trực tiếp ảnh gốc/overlay, từng dấu vết sửa và checksum. Chấm mỗi tiêu chí, dẫn bằng chứng/lý do trừ. Không xem pass của script hoặc IoU cao là xác nhận độc lập.
