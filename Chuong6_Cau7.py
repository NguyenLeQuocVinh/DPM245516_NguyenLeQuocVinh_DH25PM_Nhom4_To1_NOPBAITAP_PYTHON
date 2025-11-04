n = int(input("Nhập số lượng phần tử: "))
lst = []

print("Nhập dãy số tăng dần:")

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    
    # Nếu không phải phần tử đầu tiên thì kiểm tra tăng dần
    while i > 0 and x <= lst[-1]:
        print("Sai quy tắc! Số phải lớn hơn", lst[-1])
        x = int(input(f"Nhập lại phần tử thứ {i+1}: "))
    
    lst.append(x)

print("Dãy số tăng dần là:", lst)
