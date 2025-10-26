import math
#Viết chương trình tính loga
a=float(input("Nhap a:"))
x=float(input("Nhap x:"))
if a<= 0 or a ==1 or x <=0:
        print("Gia tri khong hop le : La a>0, a !=1, x>0.")
else:
    loga_x = math.log(x) / math.log(a)
print(f"log_{a:.2f}({x:.2f} = {loga_x:.4f})")         