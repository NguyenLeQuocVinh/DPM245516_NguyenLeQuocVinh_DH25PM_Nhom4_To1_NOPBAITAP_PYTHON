import tkinter as tk
from tkinter import ttk, messagebox

# Danh sách Can - Chi
CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp",
       "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]

CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu",
       "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def convert_year():
    try:
        year = int(txt_year.get())
        can = CAN[(year + 6) % 10]
        chi = CHI[(year + 8) % 12]
        result.set(f"{can} {chi}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm hợp lệ!")

# Giao diện
root = tk.Tk()
root.title("Chuyển Năm Dương Lịch → Âm Lịch")
root.geometry("350x200")

tk.Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack(pady=10)

txt_year = tk.Entry(root, font=("Arial", 12))
txt_year.pack()

ttk.Button(root, text="Chuyển đổi", command=convert_year).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), fg="blue").pack(pady=1
)