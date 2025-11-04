while True:
    s = input("Nhập vào một chuỗi: ")
    if s == s[::-1]:
        print("=> Chuỗi đối xứng!")
    else:
        print("=> Chuỗi không đối xứng!")
    tieptuc = input("Bạn có muốn tiếp tục không? (y/n): ").lower()
    if tieptuc != "y":
        print("Cảm ơn bạn đã sử dụng chương trình! Tạm biệt!")
        break
