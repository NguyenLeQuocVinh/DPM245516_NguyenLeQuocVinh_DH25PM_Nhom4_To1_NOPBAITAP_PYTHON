n = int(input("Nhập chiều cao n: "))

# 1. Hình chữ nhật rỗng (n x n)
print("\nHình chữ nhật rỗng:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 2. Tam giác vuông trái
print("\nTam giác vuông trái:")
for i in range(1, n+1):
    print("* " * i)

# 3. Tam giác vuông phải
print("\nTam giác vuông phải:")
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)

# 4. Hình chữ thập (dấu +)
print("\nHình chữ thập:")
for i in range(n):
    for j in range(n):
        if i == n//2 or j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()