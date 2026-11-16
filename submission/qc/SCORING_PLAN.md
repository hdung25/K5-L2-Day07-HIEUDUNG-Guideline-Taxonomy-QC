# Mục tiêu chất lượng khoảng 92/100

92/100 là mục tiêu, không phải điểm đã được chấm. Không có điểm tự xác nhận. Người đánh giá dùng RUBRIC.md và rubric_scorecard.csv, ghi bằng chứng cho từng tiêu chí.

| Phần | Tối đa | Điều kiện cần hoàn tất để hướng tới điểm cao |
|---|---:|---|
| Guideline cá nhân | 15 | Định nghĩa lớp/thuộc tính rõ; ví dụ đúng ảnh; quyết định ban đầu có lý do |
| Guideline nhóm/taxonomy | 20 | Giải quyết khác biệt có căn cứ; khóa quy tắc nhất quán và taxonomy tương ứng |
| Phân công/gán độc lập | 15 | Đủ 80 lượt, COCO hợp lệ, nhãn đúng và có bằng chứng độc lập |
| IAA/calibration | 25 | Mẫu số đúng; giải thích lỗi chung; quyết định từng ca, sửa nhãn và kiểm lại theo v1.1 |
| QC/báo cáo | 15 | Duyệt đủ 40 ảnh nhãn cuối; ghi lỗi và mẫu số; kết luận theo bằng chứng |
| Tái lập/hợp tác | 10 | Mở lại được, checksum khớp, checklist sạch và hồ sơ cá nhân đầy đủ |

Hiện chưa đủ căn cứ dự đoán 92 điểm: calibration còn 996 ca chưa chốt, chưa có nhãn cuối/manifest/QC nghiệm thu, và hai bản nhãn cùng nguồn chưa chứng minh độc lập. Hồ sơ Hold giải thích được các giới hạn nhưng không tự thay thế bằng chứng của các mục trên.

Ưu tiên nâng điểm bằng công việc thật: khắc phục tính độc lập theo hướng coach chấp thuận; chốt từng ca; sửa theo guideline đã khóa; kiểm toàn lô; rồi chạy check_submission tới 0 lỗi. Không đổi ngưỡng hoặc tạo xác nhận chưa thực hiện để đạt điểm mục tiêu.
