# Guideline cá nhân — 102

- Ngày: 2026-11-16.
- Người thực hiện: Hiếu (102).
- Trạng thái: bản cá nhân cần chốt cùng đặc tả nhóm; chưa xác nhận hoàn tất Pha 2.
- Căn cứ: xem sơ bộ 40 ảnh overlay; xem riêng ảnh gốc 007, 014, 022, 037. Thành viên 102 cần đọc, sửa và xác nhận trước khi nộp.

## 1. Mục tiêu và giới hạn

Phát hiện người và phương tiện thật trên ảnh 2D bằng box phần nhìn thấy. Ưu tiên tránh bỏ sót người thật và tránh gán tượng, đồ chơi, hình in thành vật thật. Không suy luận số chỗ, khả năng chạy hay loại động cơ nếu ảnh không cung cấp bằng chứng.

## 2. Định nghĩa lớp đề xuất

| Lớp | Dấu hiệu dùng được trên ảnh | Ví dụ / phản ví dụ |
|---|---|---|
| car | Sedan, hatchback, SUV; khoang hành khách liền thân | SUV img_012; không phải pickup img_037 |
| truck | Cabin và thùng/khoang chở hàng tách nhau, kể cả thùng có nắp | Hai xe tải img_007, pickup img_037 |
| van | Thân hộp liền cabin, mũi ngắn; phân biệt bằng hình dáng | Xe trắng img_005; không ép minibus vào van |
| bus | Thân chở khách dài, nhiều cửa sổ hông hoặc cửa khách riêng | img_009; xe xanh phía sau pickup img_037 |
| motorcycle | Xe hai bánh có động cơ, gồm mô tô gắn thuyền như ngoại lệ | img_022; không phải xe đạp img_029 |
| bicycle | Khung, bàn đạp và bánh xe đạp quan sát được | img_029; không suy từ việc người đội mũ |
| three_wheeler | Tuk-tuk, xích lô, ba gác; dùng cấu trúc xe, không yêu cầu thấy cả ba bánh | img_004, 023, 035 |
| person | Người thật nhìn trực tiếp, mỗi người một box | Người qua đường img_014; không gồm tượng img_017 |
| ignore_region | Cụm vật thật nhỏ/dày không tách được | Nền xa img_021; không dùng cho ma-nơ-canh img_033 |

Ngoài taxonomy thì không ép vào lớp gần nhất. Không phân loại theo hãng xe hoặc đoán số ghế không nhìn thấy.

## 3. Thuộc tính có ngưỡng

- `occluded_level`: phần diện tích ước lượng bị vật khác che: 0 khi <10%, 1 khi 10–<40%, 2 khi 40–<80%, 3 khi ≥80% và vẫn nhận ra lớp. Đây là ước lượng quan sát, không phải số đo tự động từ diện tích bbox giao nhau.
- `truncated=yes`: vật tiếp tục ra ngoài mép ảnh. Chỉ chạm biên chưa đủ kết luận.
- `can_review=true`: cần chốt lớp, mức che, ranh giới hoặc việc chọn vật. Ca chưa thể đặt box ghi vấn đề cấp ảnh.
- `ignore_region` không mang thuộc tính đối tượng.

## 4. Quy tắc và ca khó

1. Box ôm phần nhìn thấy; không vẽ bù phần bị che. Người và xe luôn có box riêng nếu đều đủ điều kiện; xe không người không được thêm person.
2. Người đi xe máy: bao đầu/mũ, thân và chân thấy được; xe bao bánh, thân, tay lái. Các box chữ nhật có thể giao nhau.
3. Box cao <20 px không gán riêng. Cụm ≥3 vật nhỏ hoặc không tách được biên dùng ignore; vật rõ ở hàng trước vẫn gán riêng.
4. Xe chở ô tô img_002: một truck cho xe chở và car riêng cho từng ô tô nhận ra được, kể cả khi đang được chở. Hàng cố định theo quy tắc nhóm; không đếm hàng thành lớp xe nếu là tượng.
5. Loại tượng img_017/027, ma-nơ-canh img_033, đồ chơi img_038, hình in img_018, phản chiếu và xe chủ img_020. Giữ ảnh không đối tượng trong COCO.
6. Người nhìn qua kính xe kín không gán theo phạm vi v1.0. Người trên xe hở chỉ gán khi thực sự thấy người.

| Ảnh | Quyết định đề xuất | Lý do / việc cần chốt |
|---|---|---|
| img_007 | Hai truck; không giữ hai box cho cùng pickup | Cabin và thùng của pickup là một xe |
| img_011 | Mô tô kim loại cần review | Bánh và yên chưa chứng minh vật là phương tiện hoạt động; tránh khẳng định ngoài ảnh |
| img_014 | Hai người rõ; người/xe nhòe cần review theo R-17 | Không tự coi mọi vệt nhòe là nền |
| img_019 | Xe diễu hành car; người lái person; chuột không gán | Ranh giới ignore không được nuốt người rõ hàng đầu |
| img_022 | Một motorcycle bao thuyền; không thêm person | Ảnh gốc cho thấy xe đỗ, không có người; ví dụ v1.0 cần sửa |
| img_024 | Không tự kết luận xe vàng là mô hình chỉ vì đặt cao | Cần xác minh kích thước/nguồn; ghi review trước calibration |
| img_028 | Truck bao hàng cố định theo v1.0; không box ngựa riêng | Phân biệt hàng trong box và đối tượng của lớp đích |
| img_030/032 | Rà cụm dày và người/xe rõ hàng đầu | Không sử dụng ignore để che việc bỏ sót |
| img_037 | Pickup có nắp là truck; xe xanh phía sau là bus | Nắp thùng không biến pickup thành van |

## 5. QC và khác biệt cần thảo luận

Giữ nguyên toàn bộ ngưỡng `rules` trong taxonomy. IoU và đồng thuận lớp chỉ có ý nghĩa khi hai lượt gán thực sự độc lập. Hai bản sao cùng prelabel không đáp ứng điều này.

Đề xuất làm rõ v1.0: ngoại lệ sidecar ở R-03 (không áp máy móc quy tắc đếm bánh); xung đột túi đeo giữa R-04/R-12; kính trong suốt và phản chiếu ở R-01; mô hình và phương tiện ở img_011/024; ví dụ person ở img_022. Chưa tự sửa đặc tả đã khóa, chưa khai báo đây là kết quả họp nhóm.
