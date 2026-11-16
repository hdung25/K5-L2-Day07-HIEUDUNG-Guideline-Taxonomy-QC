# Báo cáo QC — HIEUDUNG

## 1. Mục đích, dữ liệu và phiên bản

- Mục đích và giới hạn sử dụng: Nhãn box 2D cho bài thực hành 40 ảnh. Kết luận Release áp dụng bản sau xử lý/QC; không xác nhận hai người gán mù độc lập và không đánh giá độ đại diện cho dữ liệu vận hành.
- Nguồn và phép sử dụng dữ liệu: data/ATTRIBUTION.csv; giữ nguyên ảnh và ghi công/giấy phép. Hai ca vật thật/vật giả được đối chiếu trang nguồn trong SOURCE_VERIFICATION.md.
- Manifest và checksum nhãn cuối: submission/qc/batch_manifest.json; submission/qc/labels_calibrated.json SHA-256 00d255ffb685a7226fb25f17a74df75d536e08b461c5285470ea662943396198. CSV, ảnh gốc và đầu vào phiên bản đều được khóa trong manifest.
- Guideline và taxonomy khi gán / khi bàn giao: Đầu vào v1.0 được giữ nguyên; bản bàn giao v1.1, taxonomy_v1.1.json. guideline_change.json là semantic, quyết định Q001 phạm vi lo đã áp dụng và kiểm lại cả 40 ảnh; ngưỡng rules không đổi.

## 2. Phân công và so sánh trước calibration

- Lượt hoàn thành / được giao: 80/80 lượt có COCO đúng phân công, mỗi mã 40 ảnh. Hai bản được xử lý trong hồ sơ chung từ cùng nguồn, không có bằng chứng 80 lượt gán mù riêng giữa hai người.
- Số cặp box ghép, IoU TB, đồng thuận lớp và mẫu số: 446 cặp; IoU TB 0.998757; cùng lớp 446/446=100%; cùng mức che 351/446≈78.70%; cùng truncated 446/446=100%. Đây là so sánh hai phiên bản cùng nguồn, không dùng để tuyên bố IAA độc lập. Xem IAA_LIMITATIONS.md.
- Box chưa ghép, loại do ignore, bất đồng vùng ignore: Chưa ghép 101:4, 102:0; bỏ qua do ignore:0; ca bất đồng ignore:0. Không suy rằng ignore đã đúng chỉ từ số 0.
- Ca hai người có thể cùng sai sau khi đối chiếu tham chiếu: Ví dụ v1.0 img_022 ghi person nhưng ảnh không có người; source #163 img_011 nằm trên cổ/tay tượng. Đã sửa ví dụ và loại box giả. img_024 xe vàng được mô tả tác giả xác nhận là đồ chơi. Đây là đối chiếu ảnh/nguồn, không phải nhãn chuẩn coach.

## 3. Calibration và kiểm lại

- Ca đã xử lý, rule ID, bản sửa và người xác nhận: 996 ca C001–C996 có quyết định riêng; Q001 áp dụng semantic toàn lô; Q002 sửa person bỏ sót img_010. calibration_decisions.csv có 998 dòng quyết định. Vai trò phụ trách 101, đối chiếu 102 trong lượt xử lý chung; không phải xác nhận hai cá nhân làm độc lập. calibration_edits.json lưu từng instance trước/sau và lý do; final_object_map.csv nối ID nguồn với nhãn cuối.
- Tác động v1.1 lên nhãn và ảnh: 40/40 ảnh được rà; 28 box mới, 14 box loại từ bản làm việc, cùng 4 box img_014 tiếp nhận từ bản 101. Sửa box, lớp và mức che theo từng instance; nhãn cuối gồm 467 annotation =463 đối tượng +4 vùng ignore. Không có cờ can_review trong nhãn cuối; cờ của hai bản đầu vào được giữ nguyên.
- Tham chiếu bằng chứng khi Rework: Vòng 1 lưu snapshots, review và kết quả Hold: 1/40 ảnh có lỗi =2.5%, 1 person bỏ sót và một điều khoản cần làm rõ. Q002 bổ sung người điều khiển áo nâu/mũ trắng ở img_010; điều khoản img_011 được chốt theo nguồn. Vòng 2 kiểm lại ảnh sửa, đối chiếu nội dung snapshot 39 ảnh còn lại với lượt rà toàn lô; không ghi đè vòng 1.

## 4. Kết quả duyệt

- Vòng QC: 2
- Người review và ngày: Vai trò 102, ngày 2026-11-16; kiểm theo ảnh gốc/overlay và snapshot. Chưa có xác nhận gán độc lập hoặc chữ ký riêng của hai thành viên.
- Đã duyệt / cả lô: 40/40 ảnh; ca khó 35/35, phần còn lại 5/5. Năm ảnh trống 017/020/027/033/038 vẫn có trong COCO.
- Ảnh lỗi / ảnh đã duyệt: 0/40=0.0% lỗi ghi nhận ở vòng 2; vòng 1:1/40=2.5%. Đây là kết quả lượt kiểm, không phải khẳng định có nhãn chuẩn tuyệt đối.
- Annotation đối tượng hiện có bị lỗi / annotation đối tượng đã duyệt: 0/463=0.0% ở vòng 2; ignore_region không nằm trong mẫu số đối tượng.
- Vật bỏ sót, ảnh và vùng: Vòng 1 có 1 person người điều khiển ở xe máy bên trái img_010; Q002 đã sửa. Vòng 2 không ghi nhận bỏ sót mới:0.
- Ca khó / phần còn lại, lỗi lặp và ví dụ: Vòng 2 ca khó:0/35 ảnh lỗi, phần còn lại:0/5; không ghi nhận lỗi lặp. img_019 đã bổ sung người hàng trước và thu ignore; img_030 giữ một box cho cả xe Dream, không tách phần đầu/đuôi thành instance riêng.
- Một lỗi máy chặn được và một lỗi cần người đọc ảnh: Validator chặn box vượt biên/lớp lạ/ảnh thiếu; đọc ảnh mới phát hiện source #163 là tượng, box trùng và người lái bị sót img_010. Test công cụ không thay cho kiểm nhãn bằng ảnh.

## 5. Quyết định bàn giao

- Quyết định: Release
- Lý do, người nhận và phạm vi sử dụng: Đủ 40 ảnh sau sửa, manifest khớp, 998 quyết định có dấu vết, QC vòng 2 duyệt 40/40 và không ghi nhận lỗi mới, phù hợp ngưỡng của lô thực hành. Giao nhóm/coach để đánh giá; giới hạn IAA cùng nguồn và vai trò xử lý chung vẫn áp dụng. Không suy ra mức điểm 92 hoặc hoàn thành tiêu chí độc lập từ kết luận QC này.
- Nếu còn việc: Không còn ca calibration mở hoặc lỗi cấu trúc trong gói; việc đánh giá độc lập và điểm số thuộc reviewer/coach. Chưa nộp LMS thay người dùng.
- Kiểm ngược từ báo cáo tới ảnh, rule và nhãn: Q002 → reviews/round-01/qc_review.csv → img_010.jpg → R-04/R-06 → calibration_edits.json → final_object_map.csv → person #139 của labels_calibrated.json → reviews/round-02/qc_review.csv. Đã tự kiểm đường dẫn và nội dung; chưa có reviewer ngoài nhóm ký xác nhận.
