s = input("Nhập chuỗi họ tên: ")

# Xóa khoảng trắng đầu/cuối và tách các từ
words = s.strip().split()

# Viết hoa ký tự đầu mỗi từ
result = " ".join(word.capitalize() for word in words)

print("Chuỗi tối ưu:", result)
