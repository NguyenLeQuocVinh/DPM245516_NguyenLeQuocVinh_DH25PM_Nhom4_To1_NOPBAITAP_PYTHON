def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None  # hoặc có thể báo lỗi
        else:
            return a / b
    else:
        return None  # phép toán không hợp lệ

def main():
    # nhập
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    op = input("Nhập phép toán (+, -, *, /): ")
    
    result = calculate(a, b, op)
    if result is None:
        if op == "/" and b == 0:
            print("Lỗi: không thể chia cho 0")
        else:
            print("Phép toán không hợp lệ")
    else:
        # nếu muốn in kết quả là số nguyên khi đúng là số nguyên:
        if result.is_integer():  
            # chuyển sang int để in gọn nếu không có phần thập phân
            print("Kết quả:", int(result))
        else:
            print("Kết quả:", result)

if __name__ == "__main__":
    main()