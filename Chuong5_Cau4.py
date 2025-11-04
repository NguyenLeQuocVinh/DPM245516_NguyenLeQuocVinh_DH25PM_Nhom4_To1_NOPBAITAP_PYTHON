"""
1. Hàm kiểm tra thông tin chuỗi
| Hàm           | Ý nghĩa                    |
| ------------- | -------------------------- |
| `len(s)`      | Trả về độ dài chuỗi        |
| `s.isalpha()` | Chuỗi chỉ gồm ký tự chữ?   |
| `s.isdigit()` | Chuỗi chỉ gồm số?          |
| `s.isalnum()` | Chuỗi gồm chữ và số?       |
| `s.isspace()` | Chuỗi chỉ là khoảng trắng? |
| `s.isupper()` | Tất cả chữ viết hoa?       |
| `s.islower()` | Tất cả chữ viết thường?    |
2. Hàm chuyển đổi chữ hoa – thường
| Hàm              | Công dụng                       |
| ---------------- | ------------------------------- |
| `s.upper()`      | Chuyển toàn bộ thành chữ HOA    |
| `s.lower()`      | Chuyển toàn bộ thành chữ thường |
| `s.title()`      | Chữ cái đầu mỗi từ viết hoa     |
| `s.capitalize()` | Chỉ chữ đầu tiên viết hoa       |
| `s.swapcase()`   | Đảo hoa ⇄ thường                |
3. Hàm tìm kiếm  thay thế
| Hàm                   | Ý nghĩa                                       |
| --------------------- | --------------------------------------------- |
| `s.find(sub)`         | Vị trí đầu tiên của `sub` (1 nếu không thấy) |
| `s.rfind(sub)`        | Tìm từ phải sang trái                         |
| `s.index(sub)`        | Giống find nhưng báo lỗi nếu không có         |
| `s.replace(old, new)` | Thay chuỗi `old` bằng `new`                   |
4. Hàm tách & nối chuỗi
| Hàm              | Ý nghĩa                            |
| ---------------- | ---------------------------------- |
| `s.split(sep)`   | Tách chuỗi thành list              |
| `" ".join(list)` | Ghép list thành chuỗi với dấu cách |

"""