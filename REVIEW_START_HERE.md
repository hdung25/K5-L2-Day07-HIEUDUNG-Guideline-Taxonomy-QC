# Bàn giao Day 07 — HIEUDUNG

**Nhãn sau calibration đã hoàn tất kiểm kỹ thuật: QC vòng 2 Release, check_submission --round 2 báo 0 lỗi.**

- 40 ảnh, 467 annotation:463 đối tượng +4 ignore_region; không còn cờ can_review trong nhãn cuối.
- 996 ca C001–C996 đã có quyết định; Q001 áp dụng semantic toàn lô; Q002 sửa thiếu người phát hiện ở QC vòng 1.
- Vòng 1 được giữ nguyên:1/40 ảnh có lỗi, 1 người bỏ sót; vòng 2:0/40 ảnh và 0/463 đối tượng có lỗi mới ghi nhận.
- Giới hạn:hai bản đầu vào cùng nguồn; không xác nhận gán mù độc lập giữa hai người. Kết luận Release này dành cho nhãn sau xử lý chung, không phải bằng chứng hoàn thành tiêu chí độc lập hoặc điểm 92.

Mở submission/qc/QC_REPORT.md, batch_manifest.json và evidence_status.json để xem bằng chứng. Checklist nằm ở REVIEW_CHECKLIST.md, phiếu chấm 21 tiêu chí /100 ở rubric_scorecard.csv. Các cột điểm để trống cho người chấm.

Ảnh overlay cuối được kèm trong submission/qc/reviews/round-02/overlays; source_id nối final_id bằng final_object_map.csv. data/ATTRIBUTION.csv giữ ghi công ảnh. work/ không được đưa vào repo/gói nộp.

Chạy lại từ gốc repo:

```powershell
python -X utf8 scripts/validate_labels.py --all
python -X utf8 scripts/check_submission.py --round 2
python -X utf8 submission/qc/evidence_audit.py
```

Hồ sơ công cụ và khác biệt Windows/Linux ở REPRODUCIBILITY.md; đối chiếu hướng dẫn trực tuyến ở GUIDE_ALIGNMENT.md. Chưa thực hiện nộp LMS hoặc xác nhận thay coach.
