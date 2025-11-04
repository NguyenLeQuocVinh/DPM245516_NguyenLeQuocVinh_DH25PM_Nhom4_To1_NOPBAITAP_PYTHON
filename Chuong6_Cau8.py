n = int(input("Nhập số lượng phần tử: "))

M = []

# Nhập dãy số thực
for i in range(n):
    x = float(input(f"Nhập phần tử M[{i}]: "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("Dãy số sau khi sắp xếp giảm dần:")
for x in M:
    print(x, end=" ")
