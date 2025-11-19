import csv
import random

# ==============================================
# 1. GHI FILE CSV (10 dòng, mỗi dòng 10 số ngẫu nhiên cách nhau bằng ;)
# ==============================================
def write_random_csv(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            row = [random.randint(1, 100) for _ in range(10)]  # 10 số/ngẫu nhiên
            writer.writerow(row)
    print(f"Đã ghi file CSV: {filename}")


# ==============================================
# 2. ĐỌC FILE CSV & TÍNH TỔNG MỖI DÒNG
# ==============================================
def read_and_sum_csv(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=';')
        print("Tổng từng dòng trong file:")
        for i, row in enumerate(reader, start=1):
            numbers = list(map(int, row))
            print(f"Dòng {i}: {numbers}  --> Tổng = {sum(numbers)}")


# ==============================================
# CHẠY THỬ
# ==============================================
filename = "random_numbers.csv"

write_random_csv(filename)
read_and_sum_csv(filename)
