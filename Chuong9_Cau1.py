# linear_bmi_predictor.py
from __future__ import print_function
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Dữ liệu: chiều cao (cm) và cân nặng (kg)
X = np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T  # shape (13,1)
y = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])                    # shape (13,)

# Tạo và huấn luyện mô hình Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Hệ số (w1) và hệ số chệch (w0)
w1 = regr.coef_[0]
w0 = regr.intercept_

print("Kết quả huấn luyện bằng scikit-learn:")
print(f"  w_1 (slope) = {w1:.12f}")
print(f"  w_0 (intercept) = {w0:.12f}")
print()

# Hàm dự đoán thuận tiện
def predict_weight(height_cm):
    """Dự đoán cân nặng (kg) từ chiều cao (cm)."""
    return w1 * height_cm + w0

# Nhập chiều cao từ người dùng với kiểm tra lỗi
def input_and_predict():
    while True:
        try:
            s = input("Nhập chiều cao của bạn (cm), hoặc gõ 'exit' để thoát: ").strip()
            if s.lower() in ("exit", "quit", "q"):
                print("Thoát chương trình.")
                return
            h = float(s)
            if h <= 0:
                print("Vui lòng nhập chiều cao dương.")
                continue
            pred = predict_weight(h)
            print(f"Chiều cao: {h:.1f} cm  →  Dự đoán cân nặng: {pred:.2f} kg")
            print()
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập số (ví dụ: 170).")

# Tùy chọn: vẽ đồ thị dữ liệu gốc + đường hồi quy
def plot_data_and_line(show=True):
    xs = X.flatten()
    ys = y
    x_line = np.linspace(xs.min()-5, xs.max()+5, 100)
    y_line = w1 * x_line + w0

    plt.figure(figsize=(8,5))
    plt.scatter(xs, ys, label="Dữ liệu (height, weight)", zorder=3)
    plt.plot(x_line, y_line, label=f"Hồi quy tuyến tính: y={w1:.4f}x+{w0:.2f}")
    plt.xlabel("Chiều cao (cm)")
    plt.ylabel("Cân nặng (kg)")
    plt.title("Hồi quy tuyến tính: dự đoán cân nặng theo chiều cao")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    if show:
        plt.show()

if __name__ == "__main__":
    print("Mô hình đã được huấn luyện trên 13 mẫu dữ liệu.")
    print("Bạn có thể nhập nhiều lần để dự đoán hoặc gõ 'exit' để thoát.\n")
    # Hiển thị đồ thị (bạn có thể tắt nếu không muốn)
    try:
        plot_data_and_line(show=True)
    except Exception as e:
        # nếu môi trường không hỗ trợ đồ họa (ví dụ chạy terminal không có display)
        print("Không thể hiển thị đồ thị (matplotlib). Bỏ qua plot. Lỗi:", e)
    # Vòng lặp nhập & dự đoán
    input_and_predict()
