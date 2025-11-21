import tkinter as tk
from tkinter import ttk

def change_style(event=None):
    selected = combo_style.get()
    btn_target.configure(style=selected)

root = tk.Tk()
root.title("Cấu hình Style cho Button")
root.geometry("500x450")

style = ttk.Style()
style.theme_use("default")

# Tạo vài style mẫu
style.configure("Red.TButton", foreground="white", background="red")
style.map("Red.TButton",
          background=[("active", "#cc0000")])

style.configure("Green.TButton", foreground="white", background="green")
style.map("Green.TButton",
          background=[("active", "#006600")])

style.configure("Blue.TButton", foreground="white", background="blue")
style.map("Blue.TButton",
          background=[("active", "#000099")])

style.configure("Outline.TButton", 
                foreground="black",
                borderwidth=2,
                relief="solid")

style.configure("Big.TButton",
                font=("Arial", 14, "bold"),
                padding=10)

# Danh sách style
style_list = ["Red.TButton", "Green.TButton", "Blue.TButton", "Outline.TButton", "Big.TButton"]

# Combobox chọn style
ttk.Label(root, text="Chọn Style:").pack(pady=5)
combo_style = ttk.Combobox(root, values=style_list, state="readonly")
combo_style.current(0)
combo_style.pack(pady=5)
combo_style.bind("<<ComboboxSelected>>", change_style)

# Button để test style
btn_target = ttk.Button(root, text="Button Demo", style=style_list[0])
btn_target.pack(pady=20)

# Khung hiển thị toàn bộ button theo từng style
frame_preview = tk.Frame(root)
frame_preview.pack(pady=20)

tk.Label(frame_preview, text="Danh sách Button theo Style:", font=("Arial", 10, "bold")).pack()

for s in style_list:
    ttk.Button(frame_preview, text=s.replace(".TButton", ""), style=s).pack(pady=4)

root.mainloop()
