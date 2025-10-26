import math
#Viết chương trình tính căn bậc 2 lồng nhau
n=int(input("Nhap n:"))
S = math.sqrt(2)
for i in range(1,n):
    S = math.sqrt(2+S)
print(f"S({n})= {S:.6f}")