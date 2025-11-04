def lay_file_va_duoi(path):
    # Lấy phần sau dấu "\" cuối cùng
    return path.split("\\")[-1]


def lay_ten_file(path):
    filename = lay_file_va_duoi(path)
    # Tách theo dấu "." và lấy phần trước
    return filename.split(".")[0]


duongdan = input("Nhập đường dẫn file: ")

print("Tên file + đuôi:", lay_file_va_duoi(duongdan))
print("Tên file (không đuôi):", lay_ten_file(duongdan))
