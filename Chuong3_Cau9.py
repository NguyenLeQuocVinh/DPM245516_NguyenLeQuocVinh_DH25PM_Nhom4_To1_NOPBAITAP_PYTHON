def get_quarter(month):
    """Trả về quý (1, 2, 3, 4) tương ứng nếu tháng hợp lệ, ngược lại trả None."""
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    else:
        return None

def main():
    m = int(input("Nhập tháng (1–12): "))
    q = get_quarter(m)
    if q is None:
        print("Tháng không hợp lệ!")
    else:
        print(f"Tháng {m} thuộc quý {q} trong năm.")

if __name__ == "__main__":
    main()