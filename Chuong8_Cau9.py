import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi():
    try:
        height = float(txt_height.get())
        weight = float(txt_weight.get())

        bmi = weight / (height * height)
        lbl_bmi_result.config(text=f"{bmi:.2f}")

        # Xác định tình trạng
        if bmi < 18.5:
            condition = "Gầy"
        elif bmi < 25:
            condition = "Bình thường"
        elif bmi < 30:
            condition = "Mập"
        else:
            condition = "Béo phì"

        lbl_status_result.config(text=condition)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Giao diện
root = tk.Tk()
root.title("Phần mềm tính BMI")
root.geometry("350x280")

tk.Label(root, text="CHIỀU CAO (m):", font=("Arial", 11)).pack(pady=5)
txt_height = tk.Entry(root, font=("Arial", 12))
txt_height.pack