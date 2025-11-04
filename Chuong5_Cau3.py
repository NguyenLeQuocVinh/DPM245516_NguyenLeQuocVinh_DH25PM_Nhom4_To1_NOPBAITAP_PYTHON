# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi số, các số cách nhau bởi dấu ';': ")

# Tách chuỗi theo dấu ;
lst = s.split(";")

print("\nCác số trên từng dòng:")
count_even = 0

for x in lst:
    num = int(x)     # chuyển sang số nguyên
    print(num)

    # kiểm tra số chẵn
    if num % 2 == 0:
        count_even += 1

print("\nTổng số chẵn là:", count_even)
