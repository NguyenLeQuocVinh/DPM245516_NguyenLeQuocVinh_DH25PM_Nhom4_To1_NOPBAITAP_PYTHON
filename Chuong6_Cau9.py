# Hàm kiểm tra số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập danh sách số tự nhiên
M = list(map(int, input("Nhập các số tự nhiên cách nhau bởi khoảng trắng: ").split()))

# Tách các loại số
odd = []
even = []
prime = []
not_prime = []

for x in M:
    if x % 2 == 1:
        odd.append(x)
    else:
        even.append(x)

    if isPrime(x):
        prime.append(x)
    else:
        not_prime.append(x)
print("Các số lẻ:", odd, "=> Tổng:", len(odd))
print("Các số chẵn:", even, "=> Tổng:", len(even))
print("Các số nguyên tố:", prime)
print("Không phải số nguyên tố:", not_prime)
