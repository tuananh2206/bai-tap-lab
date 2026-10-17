import numpy as np

def generate_dual_problem(c_primal, A_primal, b_primal):
    """
    Chuyển đổi bài toán gốc (Primal):
        max c^T * x thỏa mãn A * x <= b và x >= 0
    Sang bài toán đối ngẫu (Dual):
        min b^T * y thỏa mãn A^T * y >= c và y >= 0
    """
    # Vector hàm mục tiêu đối ngẫu: c_dual = b_primal
    c_dual = np.array(b_primal, dtype=float)[cite: 6]
    
    # Ma trận ràng buộc đối ngẫu: A_dual = A_primal^T (chuyển vị của A)
    A_dual = np.array(A_primal, dtype=float).T[cite: 6]
    
    # Vector vế phải đối ngẫu: b_dual = c_primal
    b_dual = np.array(c_primal, dtype=float)[cite: 6]
    
    return c_dual, A_dual, b_dual


# --- Dữ liệu bài toán gốc (Primal) từ các bài trước ---
c_primal = [40, 30]
A_primal = [
    [2, 1],
    [1, 1]
]
b_primal = [100, 80]

# Tạo bài toán đối ngẫu
c_dual, A_dual, b_dual = generate_dual_problem(c_primal, A_primal, b_primal)

print("=== THÔNG SỐ BÀI TOÁN ĐỐI NGẪU (DUAL) ===")
print("Vector hàm mục tiêu c_dual (min c_dual^T * y):", c_dual.tolist())
print("Ma trận ràng buộc A_dual (A^T):")
print(A_dual)
print("Vector vế phải b_dual (A^T * y >= b_dual):", b_dual.tolist())

# --- Kiểm chứng định lý Đối ngẫu mạnh (Strong Duality Theorem) ---
# Nghiệm tối ưu gốc x* = (20, 60)
x_star = np.array([20, 60])[cite: 6]

# Nghiệm tối ưu đối ngẫu y* = (10, 20)
y_star = np.array([10, 20])[cite: 6]

# Tính giá trị hàm mục tiêu bài toán gốc: f_primal = c^T * x*
f_primal = np.dot(c_primal, x_star)

# Tính giá trị hàm mục tiêu bài toán đối ngẫu: f_dual = b^T * y*
f_dual = np.dot(b_primal, y_star)

print("\n=== KIỂM CHỨNG ĐỊNH LÝ ĐỐI NGẪU MẠNH ===")
print(f"Giá trị mục tiêu gốc (c^T * x*): 40*(20) + 30*(60) = {f_primal}")
print(f"Giá trị mục tiêu đối ngẫu (b^T * y*): 100*(10) + 80*(20) = {f_dual}")

# Kiểm tra đẳng thức c^T * x* == b^T * y* == 2600
is_equal = (f_primal == f_dual == 2600)[cite: 6]
print(f"Kiểm chứng c^T * x* == b^T * y* == 2600: {is_equal}")[cite: 6]
