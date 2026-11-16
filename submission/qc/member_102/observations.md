# Quan sát sơ bộ 40 ảnh

Đây là triage  trên overlay, không phải phiếu nghiệm thu nhãn cuối. Không dùng số dòng ở đây tính tỉ lệ lỗi. Các vùng khó cần xem ảnh gốc ở độ phân giải đầy đủ và chỉnh trong CVAT.

| Ảnh | Quan sát / việc cần kiểm |
|---|---|
| 001 | Người ngồi quán che nhau; kiểm người phía sau người đứng và mức che, không mặc định 0. |
| 002 | Kiểm từng ô tô trên giá; box #13/#14 có giao nhau, xác định số xe thật; truck gồm khung chở. |
| 003 | Cụm xe xa và nhiều người che nhau; kiểm box riêng/vùng ignore và vật gánh không nằm trong person. |
| 004 | Hai tuk-tuk, người trong xe hở; không ép box người dài tới sàn khi chân không thấy. |
| 005 | Người, xe che khuất nặng; van phía sau bị che, kiểm xe máy chỉ thấy tay lái/gương. |
| 006 | Nhiều xe/người sát nhau; đã bỏ #84 trùng #79 và #90 trùng #95, cần kiểm ranh giới và bicycle/motorcycle. |
| 007 | Ảnh gốc có hai truck; bỏ #98 là box con trùng #100, giữ box xe gồm thùng cao. |
| 008 | Đêm, nhiều xe máy; kiểm box trùng giữa các xe đỗ, người xa và xe tải nhỏ ở giữa. |
| 009 | Bus trung tâm; không gán người qua kính xe kín; kiểm người/xe nhỏ ở rìa. |
| 010 | Bỏ #143 nằm trong box xe #142; kiểm giỏ hàng và bicycle bị che. |
| 011 | Loại tượng Predator; xe mô tô trang trí chưa rõ là xe vận hành hay điêu khắc; cần chốt bằng chứng, giữ review. |
| 012 | Pickup gồm hàng cố định; xe tải phía trước bị pickup che; kiểm box và mức che. |
| 013 | Ảnh tối, người/xe xa; kiểm chiều cao và khả năng nhận lớp. |
| 014 | Ảnh gốc có người/xe nhòe bên trái, giữa và phải; hiện chỉ ba person, cần xem có bỏ sót theo R-17, không đánh dấu sạch. |
| 015 | Xe bị cắt mép trái/phải và xe nhòe phía sau; kiểm modal bbox và truncated. |
| 016 | Nhiều xe ba bánh che nhau; truck/three_wheeler rìa trái có thể cần chốt lại cấu trúc, không suy chỉ từ box. |
| 017 | Tượng người/ngựa; COCO giữ ảnh, không box đối tượng. |
| 018 | Loại người in trên billboard; xe sau hàng rào bị che, cần chỉnh occlusion và kiểm số xe. |
| 019 | Ignore lớn đang phủ cả hàng người có thể tách; rà person hàng trước và thu vùng ignore để tránh che bỏ sót. |
| 020 | Gương phản chiếu và xe chủ; COCO giữ ảnh trống. |
| 021 | Dòng xe/người dày; ignore nền xa và nhiều box giao nhau, cần kiểm đếm và box trùng. |
| 022 | Đã xem ảnh gốc: mô tô gắn thuyền, không có người; chỉnh box #251 bao đỉnh gương/ghi đông. Ví dụ person trong guideline nhóm cần sửa sau chốt. |
| 023 | Xích lô và người đạp riêng; kiểm box xe nhỏ nền và person bên trái. |
| 024 | Xe vàng trên nóc chưa thể khẳng định là mô hình chỉ từ overlay; cần xác nhận trước khi loại. |
| 025 | Người và xe ở xa; kiểm ngưỡng 20 px, đừng đo trên ảnh thumbnail. |
| 026 | Hai person và một motorcycle; người trước bị người sau che, không bao tranh tường thành vật thật. |
| 027 | Tượng/bia xe pickup; giữ ảnh trống. |
| 028 | Truck gồm tượng ngựa là hàng cố định theo v1.0; xe đỏ phía sau bị che nặng. |
| 029 | Hai người/xe ở trước và nhiều người nền; không bao ống dài trong box person hoặc xe. |
| 030 | Bãi xe dày; bỏ person #314 trùng bên trong #309. Box xe và vùng ignore còn cần sửa từng biên. |
| 031 | Đêm và mặt đường ướt; bỏ phản xạ trên đường, kiểm xe/person xa. |
| 032 | Người xếp hàng nhiều người vẫn tách được; kiểm bỏ sót phía trái, box trùng và xe bị người che. |
| 033 | Ma-nơ-canh, hình in; giữ ảnh trống. |
| 034 | Người qua đường và xe bị che; người/xe mép phải bị cắt, cần truncated. |
| 035 | Hai three_wheeler gồm hàng cố định trên xe trái; person bị xe che phải ước mức che. |
| 036 | Truck chính, xe máy hai bên; kiểm box trùng xe máy trái và phản chiếu trên kính. |
| 037 | Đã xem ảnh gốc; #423 là bus xanh phía sau pickup, đổi từ truck. Pickup nắp thùng vẫn truck. |
| 038 | Đồ chơi trong tủ kính; giữ ảnh trống. |
| 039 | Đã bỏ #447 trùng #445 ở mép phải; người/xe nền xa cần đối chiếu ảnh gốc. |
| 040 | Taxi bị người và tuk-tuk che; bus và xe xa cần kiểm lớp/mức che, không gán người qua kính taxi. |

Các đề xuất thay đổi quy tắc phải được nhóm chốt; nếu semantic thì rà cả 40 ảnh, không chỉ ảnh bị IAA gắn cờ.
