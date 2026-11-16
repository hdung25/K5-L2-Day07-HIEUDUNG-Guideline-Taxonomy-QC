# Guideline gán nhãn — v1.0 (thống nhất) — Nhóm HIEUDUNG

- Phiên bản: **v1.0** (khóa cho lượt gán độc lập Pha 3)
- Ngày: 2026-11-16
- Người viết ghi trong bản có sẵn: 101 · Người duyệt dự kiến: 102 (chưa có xác nhận duyệt trong artifact)
- Taxonomy đi kèm: `submission/taxonomy.json` (`version: v1.0`) → `cvat/labels_generated.json`
- Nguồn hiện kiểm chứng được: `individual/guideline_101.md`. Bản này đã tồn tại trước khi tạo bản cá nhân của Hiếu (102), `individual/guideline_102.md`; chưa có bằng chứng hợp nhất/họp hai thành viên. Giữ nguyên quy tắc để truy vết; các điểm cần chốt nằm ở `submission/qc/member_102/observations.md`.

> Mọi quy tắc có mã `R-xx`. Khi ghi `can_review`, `image_issues.csv`, `calibration_decisions.csv` hay phiếu QC,
> luôn dẫn mã quy tắc. Ca chưa có quy tắc → tick `can_review`, **không tự đặt luật mới** trong lúc gán.

## 1. Mục tiêu

Nhãn huấn luyện mô hình **phát hiện người và phương tiện thật** trên ảnh đường phố 2D (camera giao thông, hỗ trợ lái).

| Sai | Hậu quả | Mức nghiêm trọng |
|---|---|---|
| Bỏ sót người / xe 2–3 bánh thật | mô hình không thấy người đi đường | **cao nhất** |
| Gán vật giả (tượng, ma-nơ-canh, poster, phản chiếu, đồ chơi) | báo động giả, phanh gấp | cao |
| Sai lớp giữa các loại xe | ước lượng sai kích thước / tốc độ | trung bình |
| Box lỏng / thiếu phần | sai khoảng cách | trung bình |

## 2. Lớp và thuộc tính

### R-01 — Phạm vi: chỉ gán vật **thật**

Một vật được gán khi **cả hai** điều sau đúng:
1. Là người thật hoặc phương tiện thật **kích thước thật**, có cấu tạo để chở người/hàng (bánh, yên/ghế, tay lái).
2. Nhìn **trực tiếp** (không qua gương, kính phản chiếu, màn hình, poster, tranh in).

Phép thử: *"Nếu vật này ở trên đường, nó có tự di chuyển / chở người được không?"* Không → không gán.

### Bảng lớp

| Lớp | Định nghĩa (một câu) | Ví dụ | Phản ví dụ / dễ nhầm |
|---|---|---|---|
| `car` | Ô tô chở người ≤ 9 chỗ: sedan, hatchback, SUV, crossover, taxi, coupe, xe mui trần. | img_015, img_023, img_031, img_032 | pickup → `truck`; Hiace → `van` |
| `van` | Xe **một khối** thân hộp cao (nắp ca-pô ngắn), 10–16 chỗ hoặc chở hàng thùng kín liền cabin. | img_005, img_016 | minibus Coaster dài → `bus` |
| `truck` | Xe có **khoang hàng tách khỏi cabin** (thùng hở, thùng kín, mui bạt, nắp thùng): pickup, xe tải, đầu kéo, xe chở ô tô. | img_001, img_002, img_007, img_012, img_028, img_036, img_037 | SUV (khoang hành lý liền cabin) → `car` |
| `bus` | Xe chở khách > 16 chỗ: buýt, minibus, coach; nhận ra bằng thân dài, ≥ 4 cửa sổ hông liên tiếp hoặc cửa lên xuống riêng. | img_009, img_031, img_037, img_040 | `van` |
| `motorcycle` | Xe 2 bánh có động cơ (xe số, tay ga, mô tô, xe điện 2 bánh), kể cả mô tô gắn thuyền (sidecar). | img_006, img_010, img_021, img_022, img_026 | xe đạp → `bicycle` |
| `bicycle` | Xe đạp 2 bánh đạp chân, không động cơ. | img_003, img_006, img_029, img_034 | xe máy |
| `three_wheeler` | Xe 3 bánh chở người hoặc hàng: tuk-tuk, auto-rickshaw, xích lô, xe ba gác. | img_004, img_016, img_023, img_035, img_040 | `motorcycle` |
| `person` | Người thật ở mọi tư thế: đi bộ, đứng, ngồi, **người lái / người ngồi sau trên xe hở**. | img_014, img_026, img_034 | tượng, ma-nơ-canh, người trên poster/billboard, linh vật |
| `ignore_region` | **Vùng** (không phải vật) chứa vật thật không gán được từng cái (R-08, R-09). Bỏ sót trong vùng này không tính lỗi. | đám đông img_019 | không dùng cho vật giả |

### R-02 — Phân biệt xe 4 bánh (theo thứ tự)

1. Có khoang hàng **tách** khỏi cabin (nhìn thấy khe/vách giữa cabin và thùng)? → `truck`.
2. Thân dài, chở khách, ≥ 4 cửa sổ hông liên tiếp hoặc cửa khách riêng? → `bus`.
3. Thân một khối, mũi ngắn, cao hơn ô tô con rõ rệt? → `van`.
4. Còn lại → `car`.

Taxi là `car` (img_040). Pickup có nắp thùng (img_037) vẫn là `truck` vì khoang hàng tách cabin.

### R-03 — Xe 2–3 bánh

- Đếm **bánh chạm đất**: 2 bánh có động cơ → `motorcycle`; 2 bánh đạp → `bicycle`; 3 bánh → `three_wheeler`.
- Mô tô gắn thuyền (img_022): 1 box `motorcycle` bao cả thuyền (thuyền gắn cố định, đi cùng xe).
- Xích lô (img_023): 1 box `three_wheeler` bao cả ghế khách và người đạp **không** nằm trong box xe — người đạp là `person` riêng (R-04).

### Vật không thuộc lớp nào

| Vật | Xử lý |
|---|---|
| Xe đẩy, xe hàng rong, xe lăn, ngựa/động vật, cọc tiêu, rào chắn | không gán (không phải lớp đích) |
| Vật giả theo R-10 | không gán, **không** đặt `ignore_region` (để làm mẫu âm) |
| Không xác định được (quá tối/mờ) | ghi `image_issues.csv`, không đoán |

### Thuộc tính

| Thuộc tính | Mức | Ngưỡng / nghĩa |
|---|---|---|
| `occluded_level` (R-06) | `0` | phần bị che < 10% diện tích ước lượng của vật |
| | `1` | 10% – < 40% |
| | `2` | 40% – < 80% |
| | `3` | ≥ 80% bị che nhưng **vẫn nhận ra lớp** |
| `truncated` (R-07) | `yes` | vật bị **mép ảnh** cắt (box chạm mép ảnh và vật tiếp tục ra ngoài khung) |
| | `no` | vật nằm trọn trong ảnh (bị vật khác che không tính là truncated) |
| `can_review` (R-16) | tick | không chắc lớp / có gán hay không / ranh giới box. Bắt buộc ghi mã quy tắc nghi ngờ ở mục 4 của nhật ký nhóm |

Ước lượng che: tưởng tượng toàn bộ vật, ước phần trăm bị vật **khác** che (không tính phần ra ngoài ảnh — phần đó là `truncated`).
Khi phân vân giữa hai mức, chọn **mức cao hơn**.

## 3. Quy tắc vẽ box

| Mã | Quy tắc |
|---|---|
| **R-04** | **Người trên xe = 2 loại box riêng.** `person` bao từ đỉnh mũ bảo hiểm/đầu tới bàn chân thấy được (gồm túi đeo, áo mưa). Box xe bao bánh, thân, tay lái, gương; **không** kéo lên để bao đầu người. Mỗi người ngồi trên xe (kể cả trẻ em, người ngồi sau) là 1 `person`. Ví dụ img_026: 2 `person` + 1 `motorcycle`. |
| **R-05** | Box ôm sát **phần nhìn thấy** (modal), không đoán phần bị che. Sai lệch cho phép ≤ 2 px mỗi cạnh. Gương chiếu hậu, cần ăng-ten mảnh **không** kéo box nếu làm box rộng thêm > 10%. |
| **R-06** | Che khuất: dùng ngưỡng `occluded_level` ở trên. Vật bị che ≥ 80% mà **không** nhận ra lớp → không gán (nếu là cụm ≥ 3 → R-09). |
| **R-07** | Cắt mép ảnh: vẽ box tới mép ảnh, `truncated=yes`. |
| **R-08** | **Vật nhỏ:** box cao < 20 px → không vẽ box riêng. Nếu ≥ 3 vật nhỏ liền nhau → 1 `ignore_region` bao cụm. 1–2 vật nhỏ lẻ → bỏ qua. |
| **R-09** | **Đám đông / cụm dày:** ≥ 3 vật thật cùng chỗ mà không tách được từng biên (che lẫn nhau ≥ 80%) → 1 `ignore_region` bao cả cụm. Vật ở **rìa trước** cụm, tách được biên, cao ≥ 20 px → vẫn gán riêng. |
| **R-10** | **Không phải vật thật → không gán:** tượng (img_017, 027), ma-nơ-canh (img_033), người/xe trên poster, billboard, tranh tường (img_018, 026 nền tranh, 030 poster), đồ chơi và mô hình thu nhỏ (img_024 xe vàng trên nóc, img_038), phản chiếu trong gương/kính (img_020), linh vật/hình nộm (img_019 chuột trắng), tượng động vật (img_028 ngựa). |
| **R-11** | **Xe chở xe / chở hàng:** xe chở là 1 box bao cả khung/thùng **và hàng chằng cố định** (img_002 khung chở ô tô; img_035 đống hàng trên nóc rickshaw). Xe **thật** đang được chở vẫn gán lớp của nó, mỗi xe 1 box (img_002: các `car` trên giá). |
| **R-12** | Vật **cầm tay / vác / gánh** (ống dài img_029, quang gánh img_003, túi xách) không nằm trong box người hay xe. |
| **R-13** | **Người trong xe kín** chỉ thấy qua kính (cabin ô tô, xe tải, buýt): không gán. **Xe hở** (tuk-tuk, xích lô, mui trần, xe máy): người nhìn thấy trực tiếp → `person` (img_004, img_016, img_019). |
| **R-14** | **Xe chủ (ego):** phần xe của người chụp (gương, cửa, ca-pô — img_020) không gán. |
| **R-15** | **Xe trang trí / diễu hành / độ:** nếu chạy được và có kích thước thật → gán theo hình dáng thân xe (img_019 xe vàng → `car`; img_011 mô tô độ kim loại → `motorcycle`). Bảo tàng / triển lãm xe thật đỗ (img_024) → vẫn gán. |
| **R-16** | **`can_review` & vấn đề cấp ảnh:** tick `can_review` khi phân vân, vẫn phải chọn lớp tốt nhất. Vùng không vẽ được box → ghi `image, annotator, region, note` để gom vào `submission/qc/image_issues.csv` sau khi khóa nhãn. |
| **R-17** | **Mờ chuyển động / tối:** gán nếu nhận ra lớp; box bao phần lõi rõ nhất, không bao vệt nhòe kéo dài (img_014 xe máy nhòe, img_015 xe nhòe phía sau). Không nhận ra lớp → R-16. |

### Thứ tự thao tác cho mỗi ảnh (để hai người ra cùng số box)

1. Quét ảnh tìm **vật giả** (R-10) → đánh dấu trong đầu là không gán.
2. Đặt `ignore_region` cho cụm dày / vật nhỏ (R-08, R-09).
3. Gán `person` từ gần tới xa.
4. Gán xe từ gần tới xa, áp R-02 / R-03.
5. Đặt `occluded_level`, `truncated` cho từng box; tick `can_review` nếu cần.
6. Ảnh không có vật nào → vẫn lưu (ảnh trống vẫn phải có trong COCO).

## 4. Ca khó (đã chốt cho v1.0)

| Ảnh | Tình huống | Rule ID | Quyết định | Lý do |
|---|---|---|---|---|
| img_001 | Xe tải nhỏ Suzuki thùng lửng + người ngồi quán | R-02, R-13 | xe → `truck`; người ngồi quán/đứng cạnh xe → `person` | thùng tách cabin |
| img_002 | Xe tải chở ~9 ô tô | R-11, R-02 | 1 `truck` (đầu kéo + rơ-moóc giá chở); mỗi ô tô trên giá cao ≥ 20 px → `car`, che theo % | xe thật được chở vẫn là xe |
| img_003 | Người gánh hàng, xe đạp, xe máy đỗ | R-04, R-12 | `person` không bao quang gánh; xe đạp `bicycle`; xe máy xa nhỏ < 20 px theo R-08 | vật gánh không thuộc người |
| img_004 | 2 tuk-tuk có tài xế | R-03, R-13 | 2 `three_wheeler` + 2 `person`; cọc tiêu không gán | xe hở |
| img_005 | Đám đông đi xe máy cận cảnh + van phía sau | R-04, R-06 | mỗi người 1 `person`; xe máy chỉ thấy tay lái/gương → `motorcycle` khi nhận ra lớp, che ≥ 2; xe trắng → `van` | |
| img_009 | Minibus Coaster | R-02 | `bus` | thân dài, nhiều cửa sổ |
| img_011 | Tượng Predator + mô tô độ kim loại | R-10, R-15 | tượng không gán; mô tô kim loại có bánh, yên → `motorcycle`, tick `can_review` | |
| img_012 | Pickup chở hàng + SUV | R-02, R-11 | pickup `truck` (bao cả hàng trong thùng); Mazda SUV `car` | |
| img_014 | 2 người qua đường, xe máy nhòe | R-17 | 2 `person` rõ; người/xe nhòe nhận ra lớp → gán, nếu không → bỏ | |
| img_017 | Tượng người cưỡi ngựa | R-10 | không gán (ảnh trống) | tượng |
| img_018 | Billboard người + bãi ô tô sau rào | R-10, R-06 | không gán người in; ô tô sau rào → `car` có che theo % hàng rào | |
| img_019 | Xe diễu hành + linh vật + đám đông sau rào | R-15, R-10, R-09 | xe → `car`; tài xế → `person`; chuột không gán; khối đám đông → `ignore_region`, người hàng đầu tách được → `person` | |
| img_020 | Gương chiếu hậu có phản chiếu xe | R-10, R-14 | không gán (ảnh trống) | |
| img_022 | Mô tô sidecar, ảnh đen trắng | R-03 | 1 `motorcycle` bao cả thuyền + `person` | |
| img_023 | Xích lô | R-03, R-04 | `three_wheeler` + `person` người đạp (+ khách nếu thấy) | |
| img_024 | Bảo tàng xe, mô hình xe vàng trên nóc | R-15, R-10 | xe thật → `car`; xe vàng trên nóc → không gán | mô hình |
| img_026 | Đôi người đi xe máy, tranh tường | R-04, R-10 | 2 `person` + 1 `motorcycle`; tàu thuyền trong tranh không gán | |
| img_027 | Bia mộ hình pickup | R-10 | không gán (ảnh trống) | tượng đá |
| img_028 | Pickup cổ chở tượng ngựa | R-02, R-10 | pickup → `truck`, box **bao cả tượng ngựa** vì là hàng cố định trên thùng (R-11); tượng ngựa không có box riêng; SUV đỏ → `car` | ngựa là tượng, nằm trên xe |
| img_029 | Chở ống dài | R-12 | `motorcycle`, `bicycle`, 2 `person`; ống không thuộc box nào | |
| img_030 | Bãi xe máy dày đặc + poster | R-09, R-10 | xe hàng trước tách được → `motorcycle`; khối phía sau → `ignore_region`; người poster không gán; người áo xanh → `person` | |
| img_032 | Đám đông trạm buýt | R-09 | người tách được biên, cao ≥ 20 px → `person`; nhóm chồng nhau → `ignore_region` | |
| img_033 | Ma-nơ-canh | R-10 | không gán (ảnh trống) | |
| img_035 | Rickshaw chất hàng | R-11 | `three_wheeler` bao cả hàng | hàng cố định |
| img_037 | Pickup có nắp thùng + buýt | R-02 | `truck`, `bus`, người đi bộ `person` | |
| img_038 | Tủ kính đồ chơi | R-10 | không gán (ảnh trống) | đồ chơi |
| img_040 | Người đội mũ BH, taxi, tuk-tuk, buýt | R-02, R-03 | `person`, taxi `car`, `three_wheeler`, SUV `car`, `bus` | |

## 5. QC và phiên bản

- Ngưỡng (giữ nguyên `rules` trong `taxonomy.json`): box cao tối thiểu 20 px; IoU ≥ 0.85 (box cao ≥ 50 px) / ≥ 0.7 (nhỏ hơn); IAA lớp ≥ 95%; lỗi theo ảnh ≤ 2%; ghép box IoU ≥ 0.5.
- Ai chốt ca mơ hồ: 2 người cùng xem ảnh chồng nhãn, quyết định ghi vào `calibration_decisions.csv` với mã người chốt; người kiểm lại là người **không** sửa nhãn ca đó.
- Thay đổi chỉ sửa câu chữ → `editorial`; thay đổi cách chọn vật / lớp / box / thuộc tính → `semantic`, tăng phiên bản và kiểm lại cả lô.

| Phiên bản | Thay đổi | Lý do (ca nào) |
|---|---|---|
| v0 | Bản khởi đầu của giảng viên | — |
| v1.0 | Thêm lớp `bus`, `bicycle`, `three_wheeler`; R-01…R-17; ngưỡng % cho `occluded_level`; quy tắc tách box người/xe | img_004, 009, 023 không có lớp; img_017, 033, 038 vật giả; img_026 người đi xe máy |
