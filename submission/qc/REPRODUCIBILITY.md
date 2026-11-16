# Kiểm tra tái lập và thay đổi công cụ

## Chuẩn hóa đường dẫn checksum

Trong scripts/common.py, hàm rel trước đây dùng str(Path), sinh dấu gạch chéo ngược trên Windows nhưng gạch chéo xuôi trên Linux. Do khóa của inputs_sha256 phụ thuộc đường dẫn, hồ sơ tạo trên Windows có thể không khớp khi mở trên Linux dù nội dung không đổi.

Đã đổi hàm rel sang Path.as_posix() cho đường dẫn tương đối và đường dẫn ngoài repo. Không thay thuật toán ghép box, công thức đo, kiểm cấu trúc hay bất kỳ ngưỡng rules nào. Các artifact so sánh được sinh lại bằng script chuẩn sau thay đổi, không sửa tay checksum.

Kiểm thử bổ sung: test_comparison_records_portable_relative_paths xác nhận khóa submission/labels/101.json và không có dấu gạch chéo ngược.

## Kiểm thử symlink trên Windows

Tách kiểm tra mã thành viên không an toàn và kiểm tra đích symlink thành hai test. Trường hợp Windows báo WinError 1314 do tài khoản không được tạo symlink thì riêng test symlink được skip với lý do rõ; kiểm tra mã thành viên vẫn chạy. Trên Linux CI, test symlink tiếp tục chạy đầy đủ. Không bỏ kiểm tra an toàn trong script phân công.

Kết quả kiểm thử thực tế ở test_results.txt: 22 test, 21 đạt và 1 skip vì quyền tạo symlink trên Windows. Checklist bài nộp và kết quả script kiểm nội dung nằm ở evidence_status.json và check_submission_latest.txt; kiểm thử công cụ đạt không đồng nghĩa nhãn đã nghiệm thu.

## Giữ nguyên byte artifact khi đưa lên Git

`.gitattributes` đặt `-text` cho submission và data/ATTRIBUTION.csv để Git không tự đổi CRLF/LF ở các file được khóa checksum. Đây không phải tắt kiểm tra hash; các byte tải từ repo phải khớp byte đã đo. Nhờ vậy có thể kiểm cùng hồ sơ trên Windows/Linux mà không thay nội dung nhãn hoặc sửa tay manifest.
