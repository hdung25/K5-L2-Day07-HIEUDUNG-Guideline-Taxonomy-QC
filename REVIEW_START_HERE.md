# Bàn giao bài Day 07 — HIEUDUNG

Phần 101 và 102 đã có guideline, ghi chú và COCO hợp lệ cấu trúc; gói hiện tại là **Hold**, chưa hoàn thiện nhãn cuối/QC.

1. Mở `submission/qc/REVIEW_CHECKLIST.md` để xem checklist, bảng tiêu chí và prompt chấm.
2. Xem `submission/qc/evidence_status.json` và `check_submission_latest.txt` để biết kết quả kiểm thực tế.
3. Đọc `submission/qc/IAA_LIMITATIONS.md` trước số liệu IAA: hai bản dùng cùng nguồn prelabel.
4. Chấm `submission/qc/rubric_scorecard.csv` (21 tiêu chí, tối đa 100), điền điểm và lý do theo RUBRIC.md.
5. Tiếp tục `submission/qc/NEXT_STEPS.md`; 996 ca còn chờ trong calibration_decisions.csv, có worklist và queue để xử lý.

Kiểm lại từ gốc repo:

```powershell
python -m pip install -r requirements.txt
python -X utf8 submission/qc/evidence_audit.py
python -X utf8 scripts/viz_disagreement.py --images flagged
```

`work/` không nằm trong zip; tạo lại overlay bằng lệnh trên. Ảnh gốc, attribution và script được kèm trong gói. Hàm ghi đường dẫn checksum đã được sửa để tái lập Windows/Linux; xem `submission/qc/REPRODUCIBILITY.md`. Không thay công thức hoặc ngưỡng QC. Không ghi 0 lỗi hoặc Release khi chưa đủ calibration, manifest và QC.
