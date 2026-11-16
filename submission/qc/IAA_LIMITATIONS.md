# Giới hạn phép so sánh 101–102

Trạng thái: **Hold**. Các file iaa_summary.json/.md là kết quả gốc của qc_compare.py và được giữ nguyên; phần giải thích này phải đi kèm khi đọc hoặc chấm điểm.

Hai bản nhãn 101/102 phát triển từ cùng prelabel. Không đủ bằng chứng cho giả định gán độc lập; không dùng `overall.pass=true` để tuyên bố hai thành viên đã đạt IAA độc lập. Đây là phép so sánh hai phiên bản nhãn làm việc.

| Số liệu máy tính | Giá trị | Cách hiểu |
|---|---:|---|
| Độ phủ cấu trúc | 80/80 lượt | Có đủ ảnh trong hai COCO; không chứng minh 80 lượt đã nghiệm thu |
| Cặp box ghép | 446 | Ghép 1–1, IoU ≥0.5, không phân biệt lớp |
| IoU trung bình | 0.998757 | Cao phần lớn do cùng nguồn box |
| Cùng lớp | 446/446 = 100% | Không phát hiện lỗi cùng phân loại sai/bỏ sót |
| Cùng mức che | 351/446 ≈78.70% | Còn 95 cặp khác mức che |
| Chưa ghép 101 / 102 | 4 / 0 | Bốn box bổ sung ở img_014, chưa kết luận bên nào đúng chỉ từ phép ghép |
| Bỏ qua do ignore | 0 | Đây là số box chưa ghép bị bỏ qua; không phải kiểm chứng ranh giới ignore đúng |
| Cờ review | 896 dòng | 450 đối tượng bản 101 + 446 đối tượng bản 102 |
| Tổng ca / ảnh bị cờ | 996 / 35 | 896 cờ +95 thuộc tính +4 chưa ghép +1 IoU thấp; một vật/ảnh có thể đóng góp nhiều ca |

Không có mẫu số lỗi QC cuối vì chưa có nhãn sau calibration và vòng nghiệm thu. Đừng dùng 996/902 hoặc 35/40 làm tỉ lệ lỗi nghiệm thu.

Để có IAA độc lập hợp lệ cần tổ chức lại lượt gán theo quy trình coach chấp thuận, khóa nhãn trước khi xem bản còn lại, rồi chạy lại toàn bộ pipeline. Nếu không thực hiện được, nộp hồ sơ Hold và giới hạn trên; không dựng lịch sử độc lập.
