# Đối chiếu hướng dẫn trực tuyến

Đã đọc [hướng dẫn trợ giảng Day 07](https://site-ivory-mu-57.vercel.app/) ngày 2026-11-16 và đối chiếu với GUIDE.md, RUBRIC.md, SUBMISSION.md cùng các script hiện có.

Áp dụng các điểm trọng tâm: mỗi ca calibration có quyết định và dấu vết sửa; thay đổi quy tắc phải vào v1.1; ghi mẫu số IAA và hai cách đếm lỗi QC; kiểm bằng mắt không thay bằng validate; giữ nguyên rules; xem lại nhãn sau sửa; giữ lịch sử vòng kiểm; không báo Release khi số liệu không đạt.

Một số chi tiết của trang khác phiên bản repo hiện tại:

| Nội dung trên trang | Cách dùng phù hợp script hiện tại |
|---|---|
| Mã học viên/họ tên trong tên file | Giữ mã ba chữ số 101/102 để khớp assignment và validator; không tự đổi tên làm hỏng kiểm bài |
| Bảng calibration 6 cột | Dùng đủ 9 cột, thêm dấu vết sửa, kiểm lại và phạm vi |
| labels_calibrated_flagged.json | Dùng tên COCO có hash do prepare_calibration.py in ra |
| QC mẫu 20 ảnh | Duyệt đủ 40/40; vòng chỉ lấy mẫu không được Release theo script hiện tại |
| Ghi đè bằng force | Giữ round-01, mở round-02 để truy được bản trước và sau sửa |

Trang không cung cấp nhãn chuẩn từng box, không xác nhận độc lập của hai bộ nhãn và không phải căn cứ tự gán điểm 92/100. Bản ghi giới hạn IAA vẫn đi kèm hồ sơ.
