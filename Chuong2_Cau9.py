#Giải thích kết quả tính toán của các biểu thức
"""
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:
(a) i1 + (i2 * i3)= -13 cách thực hiện: tính trong hoặc trước i3 * i2 sau đó cộng với i1 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(b) i1 * (i2 + i3)= 4 cách thực hiện: tính trong hoặc trước i3 * i2 sau đó nhân với i1 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(c) i1 / (i2 + i3)=1.0 cách thực hiện: tính trong hoặc trước i3 * i2 sau đó chia lấy hết với i1 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(d) i1 // (i2 + i3)=1 cách thực hiện: tính trong hoặc trước i3 * i2 sau đó chia (làm tròn) với i1 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(e) i1 / i2 + i3 =-2.6 cách thực hiện: tính phép chia i1 / i2 sau đó cộng với i3 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(f) i1 // i2 + i3=-3 cách thực hiện: tính phép chia i1 // i2 (làm tròn) sau đó cộng với i3 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(g) 3 + 4 + 5 / 3= 8.666666666666666 cách thực hiên 5 chia với 3 lấy hết sau đó cộng từ trái sang phải:theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(h) 3 + 4 + 5 // 3 = 8 cách thực hiên 5 chia với 3 (làm tròn) sau đó cộng từ trái sang phải:theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(i) (3 + 4 + 5) / 3 = 4.0 cách thực hiện tính phếp tính trong ngoặc trước rồi sau đó chia với 3 lấy hết:theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(j) (3 + 4 + 5) // 3 = 4 cách thực hiện tính phếp tính trong ngoặc trước rồi sau đó chia với 3 (làm tròn):theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(k) d1 + (d2 * d3)=- 0.5 cách thực hiện: tính trong hoặc trước d3 * d2 sau đó cộng với d1 theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(l) d1 + d2 * d3 = -0.5 cách thực hiện nhân chia trước cộng trừ sau:theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(m) d1 / d2 - d3 = 0.9 cách thực hiện d1 chia với d2 trước rồi sau đó trừ với d3 :theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(n) d1 / (d2 - d3)= 0.36363636363636365 cách thực hiên tính trong ngoặc trước sau đó chia với d1 lấy hết :theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(o) d1 + d2 + d3 / 3 =  6.833333333333333 cách thực hiện phép chia trước sau thực hiện phép cộng ::theo nguyên tắc nhân , chia : trước -- cộng ,trừ : sau và ưu tiên trong ngoặc
(p) (d1 + d2 + d3) / 3 = 2.1666666666666665 cách thực hiện tính trong ngoặc trước sau đó thực hiện phép chia 
(q) d1 + d2 + (d3 / 3)= 6.833333333333333 thực hiện phép tính trong ngoặc trước sau đó thực hiện phép cộng
(r) 3 * (d1 + d2) * (d1 - d3) = 52.5 thực hiện 2 phép toán trong ngoặc trước sau đó thực hiện phép nhân 
"""

