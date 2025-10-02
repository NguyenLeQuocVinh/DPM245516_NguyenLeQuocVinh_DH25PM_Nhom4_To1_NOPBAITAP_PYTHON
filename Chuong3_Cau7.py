def is_leap_year(year):
    """Kiểm tra năm nhuận"""
    # Năm nhuận nếu chia hết 400 hoặc chia hết 4 nhưng không chia hết 100
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month, year):
    """Trả về số ngày trong tháng của năm đó"""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0  # tháng không hợp lệ

def next_day(day, month, year):
    """Tính ngày kế tiếp, trả về tuple (ngày, tháng, năm)"""
    # dùng số ngày tối đa của tháng hiện tại
    dim = days_in_month(month, year)
    if dim == 0:
        raise ValueError("Tháng không hợp lệ")
    
    # nếu ngày hiện tại < số ngày của tháng thì chỉ tăng ngày
    if day < dim:
        return (day + 1, month, year)
    else:
        # nếu ngày hiện tại = ngày cuối tháng → sang tháng mới
        next_day = 1
        next_month = month + 1
        next_year = year
        if next_month > 12:
            next_month = 1
            next_year += 1
        return (next_day, next_month, next_year)

def main():
    # nhập từ người dùng
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
    
    # kiểm tra hợp lệ sơ bộ
    if m < 1 or m > 12:
        print("Tháng không hợp lệ")
        return
    maxd = days_in_month(m, y)
    if d < 1 or d > maxd:
        print("Ngày không hợp lệ cho tháng và năm đã cho")
        return
    
    nd, nm, ny = next_day(d, m, y)
    print(f"Ngày kế tiếp là: {nd}/{nm}/{ny}")

if __name__ == "__main__":
    main()