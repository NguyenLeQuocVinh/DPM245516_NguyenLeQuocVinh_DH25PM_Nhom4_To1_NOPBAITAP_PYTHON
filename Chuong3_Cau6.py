n = int(input("nhập 1 số có 2 chữ số:"))
if n > 10 or n < 99:
    xc = n // 10
    xd = n % 10
    X1 = ("")
    X2 = ("")
    if xc == 1:
        X1 = "mười"
    elif xc == 2:
        X1 = "hai"
    elif xc == 3:
        X1 = "ba"
    elif xc == 4:
        X1 = "bốn"
    elif xc == 5:
        X1 = "năm"
    elif xc == 6:
        X1 = "sáu"
    elif xc == 7:
        X1 = "bảy"
    elif xc == 8:
        X1 = "tám"
    elif xc == 9:
        X1 = "chín"
    if xd == 0:
        X2 = ""
    elif xd == 1:
        X2 = "mốt"
    elif xd == 2:
        X2 = "hai"
    elif xd == 3:
        X2 = "ba"
    elif xd == 4:
        X2 = "bốn"
    elif xd == 5:
        X2 = "lăm"
    elif xd == 6:
        X2 = "sáu"
    elif xd == 7:
        X2 = "bảy"
    elif xd == 8:
        X2 = "tám"
    elif xd == 9:
        X2 = "chín"
    print(X1, "mươi", X2)
else:
    print("bạn nhập sai, mời nhập lại")
    n = int(input("nhập 1 số có 2 chữ số:"))