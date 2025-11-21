import tkinter as tk
from tkinter import ttk, messagebox

def convert_F_to_C():
    try:
        f = float(txt_f.get())
        c = (f - 32) * 5 / 9
        result.set(f"{c:.2f} °C")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Giao diện chính
root = tk.Tk()
root.title("Chuyển đổi độ F → độ C")
root.geometry("350x200")

# Nhãn
tk.Label(root, text="Nhập độ F:", font=("Arial", 12)).pack(pady=10)

# Ô nhập
txt_f = tk.Entry(root, font=("Arial", 12))
txt_f.pack()

# Nút chuyển đổi
ttk.Button(root, text="Chuyển đổi", command=convert_F_to_C).pack(pady=10)

# Kết quả
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), fg="blue").pack(pady=10)


