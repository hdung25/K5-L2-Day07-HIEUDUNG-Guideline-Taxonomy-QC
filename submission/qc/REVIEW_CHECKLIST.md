# Checklist bàn giao và chấm điểm cho người đánh giá

Đọc từ gốc repo `D:/vinuni/lab03/day07`. Trạng thái hiện tại: **HOLD — đủ hai bản làm việc, chưa hoàn thiện nghiệm thu**. Mã 101 thuộc phần Dũng; mã 102 thuộc phần Hiếu. Không sửa script/ngưỡng để làm bài qua gate.

## Kết quả đã kiểm

| Nội dung | Kết quả |
|---|---|
| Nhãn 101 | 40 ảnh, 453 annotation =450 đối tượng +3 ignore |
| Nhãn 102 | 40 ảnh, 449 annotation =446 đối tượng +3 ignore |
| validate_labels --all | Đạt cả hai file |
| Độ phủ file | 80/80 lượt theo assignment |
| Tính độc lập | Chưa xác nhận; hai bản cùng nguồn prelabel |
| So sánh hai bản | 446 cặp, IoU 0.998757, cùng lớp 100%; chỉ so phiên bản, không chứng minh IAA độc lập |
| Calibration | 996 ca /35 ảnh; 0 ca đã đóng xác nhận |
| Nhãn cuối / manifest / QC | Chưa có; build_final dừng đúng gate |
| check_submission --round 1 | Exit 1; hiện báo 1 lỗi thiếu bằng chứng bàn giao |
| Hash đầu vào, artifact so sánh | Khớp, kiểm bởi evidence_audit.py |
| Ngưỡng rules | Giữ nguyên; cả taxonomy v1.0/v1.1 đạt schema |

Số liệu mới nhất: `evidence_status.json`. Log kiểm bài: `check_submission_latest.txt`. Không dùng tên file `guideline_v1.1_calibrated.md` để suy rằng calibration đã hoàn thành: nội dung ghi rõ đây là đề xuất.

## Checklist hồ sơ hiện có

- [x] TEAM.md có mã nhóm và kết luận Hold.
- [x] Hai guideline cá nhân có lớp, ví dụ, ngưỡng thuộc tính và ca ảnh.
- [x] Hai ghi chú cá nhân 101/102 có phạm vi và giới hạn.
- [x] Guideline v1.0, taxonomy v1.0 và cấu hình CVAT.
- [x] Đề xuất v1.1, taxonomy_v1.1 và guideline_change kind=semantic.
- [x] Bảng đối chiếu khác biệt đặc tả: GUIDELINE_DISCUSSION.md.
- [x] Hai file COCO đầy đủ 40 ảnh, không bỏ năm ảnh trống.
- [x] assignment.csv và danh sách từng mã.
- [x] Kết quả gốc qc_compare: summary, candidates, scores, flagged, consensus draft.
- [x] calibration_context.json và bảng 9 cột calibration_decisions.csv.
- [x] Worklist 996 ca và queue 40 ảnh, trạng thái chờ rõ ràng.
- [x] Báo cáo QC dùng số liệu thật, tách số liệu sơ bộ và nghiệm thu.
- [x] Nhật ký sửa, checksum, nguồn prelabel để đối chiếu.
- [x] Bảng chấm 21 tiêu chí, tổng tối đa 100 điểm, chưa tự điền điểm.

## Checklist cần hoàn thành trước nghiệm thu

- [ ] Xác nhận cách đáp ứng yêu cầu gán độc lập; cùng prelabel không đủ.
- [ ] Xác nhận đặc tả giữa hai phần cá nhân; không dựng biên bản họp.
- [ ] Kiểm từng box/vật bị bỏ sót; không chỉ dựa vào overlay thumbnail.
- [ ] Chốt từng ca C001–C996, gắn quy tắc, người chốt, dấu vết sửa và người kiểm lại.
- [ ] Với semantic, có quyết định phạm vi `lo` và rà toàn bộ 40 ảnh.
- [ ] Khóa guideline/taxonomy v1.1 sau xác nhận; giữ rules.
- [ ] prepare_calibration sinh đúng phạm vi/hash; sửa COCO và dùng đúng tên export.
- [ ] build_final tạo labels_calibrated.json/.csv và batch_manifest.json.
- [ ] Mở vòng QC 1 bằng qc_sample.py; duyệt 40/40 ảnh và ghi từng lỗi/ảnh sạch thực tế.
- [ ] qc_report.py tạo qc_result.json; Hold/Rework/Release có căn cứ.
- [ ] Cập nhật QC_REPORT.md, TEAM.md, ghi chú và checklist theo kết quả cuối.
- [ ] check_submission.py báo 0 lỗi; kiểm ngược một ca bởi người khác.
- [ ] Tạo lại zip sau mọi thay đổi; giữ attribution, không kèm work/.git/thông tin đăng nhập.
- [ ] Nộp qua kênh riêng coach chỉ định; chưa thực hiện nộp trong phiên này.

## Bảng chấm tổng quát

Chi tiết từng tiêu chí nằm trong `rubric_scorecard.csv`. Cột `reviewer_score` và `reviewer_reason` để trống cho người chấm; điểm từng dòng không vượt `max_points`. Tổng tối đa 100. Rubric chính thức là `RUBRIC.md` ở gốc repo.

| Hạng mục | Tối đa | Bằng chứng chính | Điểm cần đặc biệt kiểm |
|---|---:|---|---|
| Guideline cá nhân | 15 | guidelines/individual/ | Lập luận có đúng ảnh; không tự cộng vì dài |
| Guideline nhóm/taxonomy | 20 | guideline v1.0/v1.1, taxonomy, discussion | Bản đề xuất không bằng xác nhận đồng thuận |
| Phân công/gán độc lập | 15 | assignment, labels, provenance | 80/80 cấu trúc không chứng minh độc lập hoặc đúng nhãn |
| IAA/calibration | 25 | summary, limitations, decisions | IoU cao do cùng nguồn; chưa đóng ca và chưa có nhãn cuối |
| QC/báo cáo | 15 | QC_REPORT, evidence_status | Có Hold có căn cứ nhưng chưa có QC cuối |
| Tái lập/hợp tác | 10 | logs, audit, notes, gói zip | Check hiện còn lỗi, chưa xác nhận hợp tác hoặc nộp ngoài |
| **Tổng** | **100** | | **người đánh giá điền sau khi đọc bằng chứng** |

Hold/Rework có căn cứ vẫn được chấm theo chất lượng bằng chứng; không tự cho 0 toàn bài vì Hold, cũng không coi hồ sơ đầy đủ tên file là đủ điểm.

## Prompt dùng để tiếp tục với người đánh giá

> Đọc RUBRIC.md, RULES.md, SUBMISSION.md, submission/qc/REVIEW_CHECKLIST.md, evidence_status.json và IAA_LIMITATIONS.md. Kiểm trực tiếp ảnh gốc/COCO và checksum. Chấm từng dòng rubric_scorecard.csv, ghi điểm, bằng chứng và lý do trừ, rồi tổng hợp /100. Tách lỗi chất lượng nhãn, thiếu artifact và thiếu bằng chứng độc lập. Tiếp tục xử lý các bước trong NEXT_STEPS.md có thể thực hiện, giữ rõ các ca chưa chốt; không dựng quyết định/review hoặc dùng cùng prelabel để tuyên bố gán độc lập. Không sửa script/ngưỡng, không xóa can_review hàng loạt để qua gate. Sau mỗi thay đổi đầu vào, chạy lại pipeline đúng thứ tự và cập nhật báo cáo/zip. Chỉ kết luận Release khi đủ bằng chứng, nếu chưa thì giữ Hold và liệt kê chính xác việc còn lại.
