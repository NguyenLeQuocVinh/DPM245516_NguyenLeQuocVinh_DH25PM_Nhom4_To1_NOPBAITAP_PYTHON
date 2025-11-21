import tkinter as tk

def btn_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def calculate():
    try:
        result = eval(display.get())   # thực hiện phép tính
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear_display():
    display.delete(0, tk.END)

# Tạo cửa sổ
root = tk.Tk()
root.title("Calculator")

# Ô hiển thị
display = tk.Entry(root, width=25, font=("Arial", 20), borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Danh sách nút
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Tạo nút
for (text, row, col) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear_display
    else:
        cmd = lambda x=text: btn_click(x)

    tk.Button(root, text=text, width=7, height=2,
              font=("Arial", 18), command=cmd).grid(row=row, column=col)

# Chạy chương trình
root.mainloop()
