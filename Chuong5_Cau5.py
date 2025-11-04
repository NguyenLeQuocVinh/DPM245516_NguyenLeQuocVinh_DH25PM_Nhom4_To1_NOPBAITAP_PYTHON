s = input("Nhập chuỗi: ")

hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0
vowels = "aeiouyAEIOUY"

for ch in s:
    if ch.isupper():
        hoa += 1
    if ch.islower():
        thuong += 1
    if ch.isdigit():
        so += 1
    if ch == " ":
        khoangtrang += 1
    if not ch.isalnum() and ch != " ":
        dacbiet += 1
    # Kiểm tra nguyên âm / phụ âm
    if ch.isalpha():
        if ch in vowels:
            nguyenam += 1
        else:
            phuam += 1

print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số chữ nguyên âm:", nguyenam)
print("Số chữ phụ âm:", phuam)
