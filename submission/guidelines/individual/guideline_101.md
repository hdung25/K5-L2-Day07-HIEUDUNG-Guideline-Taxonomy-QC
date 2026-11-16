# Guideline gán nhãn — bản cá nhân (Pha 1) — 101

- Phiên bản: draft-101 (viết từ v0, trước khi họp nhóm)
- Ngày: 2026-11-16
- Người phụ trách: Dũng (101) · Người duyệt: chưa xác nhận

> Bản này ghi **quyết định ban đầu** của 101 sau khi xem cả 40 ảnh. Không sửa lại sau khi họp;
> quyết định cuối nằm ở `submission/guidelines/guideline_v1.0_agreed.md`.

## 1. Mục tiêu

Nhãn dùng để huấn luyện mô hình **phát hiện người và phương tiện thật đang/có thể tham gia giao thông**
trên ảnh 2D (camera giao thông, hỗ trợ lái). Hai loại sai nguy hiểm nhất:

- **Bỏ sót người / xe máy thật** (mô hình không thấy người đi đường → nguy cơ va chạm).
- **Gán vật giả là vật thật** (tượng, ma-nơ-canh, poster, phản chiếu) → mô hình báo động giả, phanh gấp.

## 2. Lớp và thuộc tính

### Chỗ v0 làm hai người hiểu khác nhau (lý do phải viết lại)

| Câu trong v0 | Cách hiểu A | Cách hiểu B |
|---|---|---|
| "Gán box cho mọi người và phương tiện" | gán cả tượng, ma-nơ-canh, xe đồ chơi (img_017, 033, 038) | chỉ gán vật thật |
| `car` "Ô tô con" / `truck` "Xe tải" | pickup là `car` (img_012) | pickup là `truck` |
| `van` "Xe thùng kín cỡ nhỏ" | Hiace chở khách là `van` (img_005) | xe 16 chỗ cũng là `van` (img_009) |
| `motorcycle` | tuk-tuk là `motorcycle` (img_004) | tuk-tuk là `car` — không có lớp đúng |
| `person` | người đi xe máy: 1 box chung người + xe | 2 box riêng |
| không nói xe đạp, xe buýt | bỏ qua | ép vào lớp gần nhất |
| `occluded_level` 1/2 "ít / nhiều" | không có ngưỡng % | mỗi người tự đoán |

### Lớp đề xuất

| Lớp | Định nghĩa | Ví dụ | Dễ nhầm với |
|---|---|---|---|
| `car` | Ô tô chở người ≤ 9 chỗ: sedan, hatchback, SUV, taxi, coupe. | img_015, img_023, img_031 | `van` (thân một khối), `truck` (pickup) |
| `van` | Xe một khối thân hộp cao, ≤ 16 chỗ, cửa trượt hông (Hiace, minivan chở hàng). | img_005, img_016 | `bus` nhỏ (img_009) |
| `truck` | Xe có **khoang hàng tách khỏi cabin**: pickup, xe tải nhỏ/lớn, xe chở ô tô. | img_001, img_002, img_007, img_012, img_036, img_037 | `car` (SUV) |
| `bus` | Xe chở khách > 16 chỗ, nhiều hàng cửa sổ, kể cả minibus Coaster. | img_009, img_031, img_037, img_040 | `van` |
| `motorcycle` | Xe 2 bánh có động cơ (xe máy, tay ga, mô tô), kể cả mô tô có thuyền (sidecar). | img_006, img_021, img_022 | `bicycle` |
| `bicycle` | Xe đạp 2 bánh không động cơ. | img_003, img_006, img_029 | `motorcycle` |
| `three_wheeler` | Xe 3 bánh chở người/hàng: tuk-tuk, auto-rickshaw, xích lô. | img_004, img_016, img_023, img_035 | `motorcycle` |
| `person` | Người thật (đi bộ, đứng, ngồi trên xe hở). | img_014, img_034 | tượng, ma-nơ-canh, người trên poster |
| `ignore_region` | Vùng có vật thật nhưng không gán được từng vật (quá nhỏ, quá dày). | đám đông img_019 | — |

**Vật không thuộc lớp nào** (xe đẩy, xe hàng rong, ngựa, cọc tiêu): không gán. **Vật giả** (tượng, ma-nơ-canh,
in hình, đồ chơi, phản chiếu): không gán, không đặt ignore — để làm mẫu âm cho mô hình.

### Thuộc tính

| Thuộc tính | Mức | Ngưỡng |
|---|---|---|
| `occluded_level` | `0` | che < 10% diện tích ước lượng của vật |
| | `1` | che 10% – < 40% |
| | `2` | che 40% – < 80% |
| | `3` | che ≥ 80% nhưng vẫn nhận ra lớp |
| `truncated` | `yes` | vật bị mép ảnh cắt mất phần (box chạm mép và vật còn tiếp ra ngoài) |
| | `no` | còn lại |
| `can_review` | tick | không chắc lớp / phạm vi box → để reviewer xem |

## 3. Quy tắc vẽ box (ý định ban đầu)

1. Box ôm sát **phần nhìn thấy** (không đoán phần bị che), lệch ≤ 2 px.
2. Người đi xe máy / xe đạp: **2 box riêng** — `person` (từ mũ bảo hiểm tới chân) và xe (bánh, thân, tay lái, gương). Chân người đè lên xe là bình thường.
   - Thử trên img_026: 2 `person` + 1 `motorcycle`. Thử trên img_005: mỗi người 1 box, xe máy chỉ thấy tay lái/gương → `motorcycle` occluded 3 hoặc bỏ nếu không nhận ra.
3. Box cao < 20 px: không vẽ; nếu là cụm nhiều vật nhỏ → 1 `ignore_region`.
4. Đám đông chồng nhau không tách được → `ignore_region` bao cả cụm.
5. Xe chủ (gương, cửa xe người chụp — img_020): không gán.
6. Hàng chất cố định trên xe nằm trong box xe; vật người cầm/vác tay không nằm trong box nào.

## 4. Ca khó

| Ảnh | Tình huống | Quyết định ban đầu (101) | Lý do | Loại |
|---|---|---|---|---|
| img_002 | Xe tải chở 8–9 ô tô | 1 `truck` (đầu kéo + khung) + mỗi ô tô thấy rõ 1 `car` | ô tô được chở vẫn là ô tô thật | **hỏi reviewer** — có gán xe đang được chở không? |
| img_017 | Tượng người cưỡi ngựa đội nón giao thông | không gán | không phải người thật | theo quy tắc |
| img_018 | Billboard có ảnh người + bãi xe phía sau | không gán người trên billboard; gán `car` đỗ sau hàng rào | in hình không phải người | theo quy tắc |
| img_019 | Xe diễu hành hình siêu xe + linh vật chuột | xe → `car`, tài xế → `person`, linh vật không gán, đám đông sau rào → `ignore_region` | xe chạy được trên đường | **hỏi reviewer** (lớp của xe giả tưởng) |
| img_020 | Gương chiếu hậu phản chiếu xe | không gán gì | phản chiếu + xe chủ | theo quy tắc |
| img_022 | Mô tô có thuyền, ảnh đen trắng | 1 `motorcycle` bao cả thuyền + `person` | thuyền gắn cố định | hỏi reviewer |
| img_024 | Bảo tàng ô tô, mô hình xe vàng trên nóc | xe thật → `car`; xe vàng trên nóc nhỏ hơn thật → không gán | mô hình | **hỏi reviewer** |
| img_027 | Bia mộ hình xe bán tải bằng đá | không gán | tượng | theo quy tắc |
| img_028 | Pickup cổ chở tượng ngựa | `truck`; ngựa không gán; xe đỏ phía sau `car` | ngựa là tượng, không thuộc lớp | theo quy tắc |
| img_029 | 2 người chở ống dài bằng xe máy + xe đạp | `motorcycle`, `bicycle`, 2 `person`, ống không thuộc box nào | vật cầm tay | theo quy tắc |
| img_030 | Bãi xe máy dày đặc | xe phía trước gán riêng; khối xe phía sau → `ignore_region` | không tách được | hỏi reviewer (ranh giới cụm) |
| img_033 | Ma-nơ-canh trong tủ kính | không gán | không phải người | theo quy tắc |
| img_035 | Auto-rickshaw chất hàng cao | `three_wheeler` bao cả hàng | hàng chằng cố định | theo quy tắc |
| img_038 | Tủ kính xe đồ chơi | không gán | đồ chơi | theo quy tắc |
| img_011 | Tượng Predator + mô tô điêu khắc kim loại | tượng không gán; mô tô kim loại **chưa chắc** | không rõ có chạy được | **hỏi reviewer** |

## 5. QC và phiên bản

- Dùng ngưỡng trong `taxonomy.json` (không đổi): IoU ≥ 0.85 (box cao ≥ 50 px) / 0.7, đồng thuận lớp ≥ 95%, lỗi theo ảnh ≤ 2%.
- Ca mơ hồ: tick `can_review`; nhóm chốt ở Pha 5, người chốt ghi mã.

| Phiên bản | Thay đổi | Lý do |
|---|---|---|
| draft-101 | Thêm `bus`, `bicycle`, `three_wheeler`; tách box người/xe; ngưỡng che % | v0 không xử lý được img_004, 009, 023, 026 |

## Phụ lục rà soát sau bản ban đầu

Giữ phần quyết định ban đầu ở trên để đối chiếu. Quan sát ảnh gốc sau đó xác định img_022 không có người; không tạo person dù ví dụ ban đầu ghi như vậy. Xe vàng img_024 chưa đủ bằng chứng để khẳng định là mô hình chỉ từ vị trí đặt trên nóc. Hai đề xuất này được ghi trong GUIDELINE_DISCUSSION.md và bản đề xuất v1.1; chưa có xác nhận calibration. Nhãn 101 hiện là bản làm việc cùng nguồn prelabel với 102, không khai báo là bằng chứng gán độc lập.
