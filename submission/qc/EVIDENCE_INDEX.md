# Chỉ mục bằng chứng cuối

- labels/101.json,102.json và iaa_summary giữ đầu vào/kết quả trước calibration; IAA_LIMITATIONS.md ghi rõ so sánh cùng nguồn.
- calibration_decisions.csv:996 ca nguồn +Q001 toàn lô +Q002 sửa sau QC, tổng998 dòng.
- calibration_edits.json:từng instance trước/sau; final_object_map.csv nối source_id/final_id.
- labels_calibrated_c688aa14116ff474.json:COCO sau sửa đúng phiên bản hiện hành; labels_calibrated_9f2cd4822d7c3802.json là bản vòng đầu, giữ để truy vết.
- labels_calibrated.json/.csv, batch_manifest.json:nhãn cuối40 ảnh,467 annotation và checksum.
- reviews/round-01:ảnh chụp nhãn, manifest, quyết định, phiếu và kết quả Hold, 1 person bỏ sót.
- reviews/round-02:nhãn sau sửa, phiếu40/40, kết quả Release, overlay40 ảnh và visual_review_index.json.
- QC_REPORT.md, evidence_status.json, check_submission_latest.txt:báo cáo cuối, kiểm checksum và0 lỗi kiểm bài.
- SOURCE_VERIFICATION.md:đối chiếu nguồn img_011/024; GUIDE_ALIGNMENT.md:đối chiếu hướng dẫn trực tuyến với script hiện hành.
- test_results.txt, REPRODUCIBILITY.md:kiểm thử công cụ và sửa tái lập Windows/Linux.
- member_101/102 lưu lịch sử sửa trước calibration; log trong member_102/submission_check.txt là lịch sử, không phải kết quả cuối.
- REVIEW_CHECKLIST.md và rubric_scorecard.csv:checklist và21 tiêu chí100 điểm; không tự ghi điểm khi chưa chấm.
