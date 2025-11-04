# Hàm nhập ma trận
def nhap_matrix(m, n, name):
    print(f"Nhập ma trận {name}:")
    matrix = []
    for i in range(m):
        row = list(map(float, input(f"Nhập dòng {i+1} (cách nhau khoảng trắng): ").split()))
        while len(row) != n:
            print("Sai số phần tử! Mời nhập lại.")
            row = list(map(float, input(f"Nhập dòng {i+1} (cách nhau khoảng trắng): ").split()))
        matrix.append(row)
    return matrix

# Hàm cộng ma trận
def cong_matrix(A, B):
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        dong = []
        for j in range(n):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C

# Hàm hoán vị (transpose)
def transpose(M):
    m, n = len(M), len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

# --- Chương trình chính ---
m = int(input("Nhập số dòng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

A = nhap_matrix(m, n, "A")
B = nhap_matrix(m, n, "B")

# Cộng ma trận
C = cong_matrix(A, B)

# Hoán vị
AT = transpose(A)
BT = transpose(B)

# Xuất kết quả
print("\nMa trận A:")
print(A)
print("Ma trận B:")
print(B)

print("\nA + B =")
print(C)

print("\nMa trận hoán vị Aᵀ:")
print(AT)

print("\nMa trận hoán vị Bᵀ:")
print(BT)
