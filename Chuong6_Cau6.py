import random

# Nhập số phần tử cần tạo
N = int(input("Nhập số lượng phần tử N: "))

# Tạo danh sách gồm N số ngẫu nhiên không trùng nhau từ 0-100
lst = random.sample(range(0, 101), N)

print("List gồm", N, "số ngẫu nhiên không trùng nhau:")
print(lst)
