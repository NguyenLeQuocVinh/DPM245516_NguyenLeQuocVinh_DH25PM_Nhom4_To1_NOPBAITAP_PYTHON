import tkinter as tk
from tkinter import messagebox

def login():
    username = txtUser.get()
    password = txtPass.get()

    # Kiểm tra tài khoản mẫu
    if username == "admin" and password == "123":
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

def clear():
    txtUser.delete(0, tk.END)
    txtPass.delete(0, tk.END)

# Tạo cửa sổ
root = tk.Tk()
root.title("Login Screen")
root.geometry("350x200")

# Label và Textbox Username
tk.Label(root, text="Username:", font=("Arial", 12)).place(x=30, y=30)
txtUser = tk.Entry(root, width=25, font=("Arial", 12))
txtUser.place(x=120, y=30)

# Label và Textbox Password
tk.Label(root, text="Password:", font=("Arial", 12)).place(x=30, y=70)
txtPass = tk.Entry(root, width=25, font=("Arial", 12), show="*")
txtPass.place(x=120, y=70)

# Nút đăng nhập
btnLogin = tk.Button(root, text="Login", width=10, font=("Arial", 12), command=login)
btnLogin.place(x=70, y=120)

# Nút xóa
btnClear = tk.Button(root, text="Clear", width=10, font=("Arial", 12), command=clear)
btnClear.place(x=180, y=120)

root.mainloop()
