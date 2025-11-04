def NegativeNumberInStrings(s):
    i = 0
    result = []
    while i < len(s):
        if s[i] == '-' and i+1 < len(s) and s[i+1].isdigit():
            num = "-"
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            result.append(int(num))
        else:
            i += 1

    # Xuất kết quả
    for x in result:
        print(x)



