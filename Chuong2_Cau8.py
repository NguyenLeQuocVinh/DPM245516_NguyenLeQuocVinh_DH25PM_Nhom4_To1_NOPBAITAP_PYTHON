#Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
"""
 các lỗi thường gặp:
 lỗi cú pháp
 lỗi thực thi
 lỗi logic
"""
"""
Khi chương trình dừng, hãy đọc kỹ thông báo lỗi (traceback) để xác định loại lỗi, dòng mã gây ra lỗi, và nguyên nhân. 
Dấu mũi tên trong thông báo lỗi chỉ ra chính xác điểm phát sinh vấn đề. 
Xử lý ngoại lệ với try-except:
Sử dụng khối try-except để bắt và xử lý các lỗi thực thi một cách có kiểm soát. 
Đặt đoạn mã có khả năng gây lỗi vào khối try.
Đặt mã xử lý lỗi (ví dụ: in thông báo lỗi) vào khối except. 
Kiểm tra cú pháp và thụt lề:
Đối với SyntaxError, kiểm tra các dấu câu, từ khóa, và đặc biệt là thụt lề vì Python rất nhạy cảm với thụt lề. 
Sử dụng IDE và công cụ hỗ trợ:
Các IDE như PyCharm cung cấp tính năng gỡ lỗi (debug mode), gợi ý mã, và kiểm tra cú pháp, giúp phát hiện lỗi nhanh chóng. 
Gỡ lỗi (Debugging):
Sử dụng print() để kiểm tra giá trị của các biến tại từng bước thực thi. 
Dùng các điểm dừng (breakpoint) trong IDE để tạm dừng chương trình và kiểm tra trạng thái các biến khi lỗi xảy ra. 
"""