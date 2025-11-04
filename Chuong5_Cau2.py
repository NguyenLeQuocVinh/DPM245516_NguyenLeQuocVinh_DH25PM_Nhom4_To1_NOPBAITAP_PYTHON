while True:
    s = input("Nhập chuỗi cần tối ưu: ")

    # Tối ưu chuỗi
    s_toithieu = " ".join(s.split())

    print("Chuỗi sau khi tối ưu:", s_toithieu)

    # Hỏi tiếp tục
    tieptuc = input("Bạn có muốn tiếp tục không? (y/n): ").lower()
    if tieptuc != 'y':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
