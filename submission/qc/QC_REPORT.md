# Báo cáo QC — HIEUDUNG

## 1. Mục đích, dữ liệu và phiên bản

- Mục đích và giới hạn sử dụng: Thực hành nhãn box 2D trên 40 ảnh. Hai bản làm việc cùng nguồn; chưa nghiệm thu hoặc chứng minh IAA độc lập.
- Nguồn và phép sử dụng dữ liệu: Giữ data/ATTRIBUTION.csv và giấy phép từng ảnh; không sửa ảnh gốc.
- Manifest và checksum nhãn cuối: Chưa có batch_manifest.json vì chưa xong calibration. Checksum bản làm việc ở member_101/provenance.json và member_102/provenance.json; iaa_summary.json khóa đầu vào so sánh.
- Guideline và taxonomy khi gán / khi bàn giao: v1.0 là bản gốc đã khóa cho so sánh; có đề xuất v1.1 semantic và taxonomy_v1.1.json, chưa xác nhận calibration và chưa áp vào nhãn cuối.

## 2. Phân công và đồng thuận trước calibration

- Lượt hoàn thành / được giao: 80/80 lượt có COCO hợp lệ cấu trúc (101:40, 102:40); 0/80 được xác nhận độc lập/đã nghiệm thu. Đủ file không đồng nghĩa đủ kiểm chất lượng.
- Số cặp box ghép, IoU TB, đồng thuận lớp và mẫu số: 446 cặp ghép, IoU TB 0.998757; cùng lớp 446/446=100%, cùng mức che 351/446≈78.70%, cùng truncated 446/446=100%. Chỉ so sánh hai bản cùng nguồn; không diễn giải là IAA độc lập đạt yêu cầu. Xem IAA_LIMITATIONS.md.
- Box chưa ghép, loại do ignore, bất đồng vùng ignore: 101 có 4 box chưa ghép, 102 có 0; bỏ qua do ignore 0, ca bất đồng ignore 0. Không suy ranh giới ignore đã đúng từ số 0 này.
- Ca hai người có thể cùng sai sau khi đối chiếu tham chiếu: Chưa có tham chiếu coach. Ảnh gốc img_022 không có người nhưng ví dụ v1.0 ghi person; cả hai có thể loại nhầm xe vàng img_024 hoặc dùng ignore quá rộng img_019. Đồng thuận cao không phát hiện được mọi lỗi chung.

## 3. Calibration và kiểm lại

- Ca đã xử lý, rule ID, bản sửa và người xác nhận: Hai changes.csv lưu sửa sơ bộ; chưa có ca calibration xác nhận đóng. calibration_decisions.csv có đủ 996 dòng theo ca, các trường chốt còn trống có chủ ý.
- Tác động v1.1 lên nhãn và ảnh: Đề xuất semantic về cấu trúc xe, túi đeo/cầm rời, thật/giả; sửa ví dụ sidecar. Cần chốt phạm vi lo và rà lại toàn bộ 40 ảnh; xem GUIDELINE_DISCUSSION.md.
- Tham chiếu bằng chứng khi Rework: Chưa mở vòng QC cuối. Worklist và queue chỉ là chuẩn bị calibration, không phải phiếu nghiệm thu.

## 4. Kết quả duyệt

- Vòng QC: 1
- Người review và ngày: Rà sơ bộ ảnh gốc/overlay ngày 2026-11-16 theo phần 101/102; chưa có reviewer xác nhận vòng QC 1.
- Đã duyệt / cả lô: 0/40 ảnh nghiệm thu nhãn cuối; đã xem sơ bộ 40/40 ảnh gốc và overlay nguồn. Hai phạm vi khác nhau.
- Ảnh lỗi / ảnh đã duyệt: N/A, mẫu số nghiệm thu 0; không ghi 0%.
- Annotation đối tượng hiện có bị lỗi / annotation đối tượng đã duyệt: N/A. Bản 101 có 450 đối tượng +3 ignore, bản 102 có 446 đối tượng +3 ignore; 902 annotation là hai lượt nhãn, không phải 902 vật duy nhất.
- Vật bỏ sót, ảnh và vùng: Bốn box #456–459 ở người/xe nhòe hai rìa img_014 chỉ có trong 101, cần xác nhận; không coi mọi box chưa ghép là lỗi bỏ sót thật.
- Ca khó / phần còn lại, lỗi lặp và ví dụ: 996 ca trên 35 ảnh =896 cờ review +95 thuộc tính +4 chưa ghép +1 IoU thấp. Năm ảnh không cờ là ảnh trống 017/020/027/033/038. 35/40 là tỉ lệ ảnh có cờ, không phải tỉ lệ lỗi QC.
- Một lỗi máy chặn được và một lỗi cần người đọc ảnh: Máy chặn bbox vượt biên/lớp lạ/thiếu ảnh; đọc ảnh mới biết box bao sai vật, cả hai cùng bỏ sót hoặc ví dụ guideline sai. Giữ nguyên script và gate calibration.

## 5. Quyết định bàn giao

- Quyết định: Hold
- Lý do, người nhận và phạm vi sử dụng: Chưa đóng 996 ca, chưa xác nhận độc lập, chưa áp v1.1 toàn lô, chưa có nhãn cuối/manifest/vòng QC. Bàn giao hồ sơ hiện có cho nhóm/người đánh giá đánh giá, chưa Release.
- Nếu còn việc: Xử lý theo NEXT_STEPS.md, chốt phiên bản, sửa nhãn, tạo manifest, review toàn lô và chạy lại kiểm bài. Không khôi phục được tính độc lập chỉ bằng tạo hai file khác nhau từ cùng nguồn.
- Kiểm ngược từ báo cáo tới ảnh, rule và nhãn: img_037 → data/images/img_037.jpg → R-02 → annotation #423 bus trong hai file nhãn → hai changes.csv. Đã đối chiếu ảnh gốc; chưa có người ngoài nhóm kiểm ngược hoặc nghiệm thu toàn lô.
