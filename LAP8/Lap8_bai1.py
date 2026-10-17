def solve_lp_geometric(vertices, c1, c2):
    """
    Giải bài toán Quy hoạch Tuyến tính 2D bằng phương pháp duyệt đỉnh hình học.
    
    Tham số:
    - vertices: Danh sách các tọa độ đỉnh dạng [(x1, x2), ...]
    - c1, c2: Hệ số của hàm mục tiêu f(x1, x2) = c1*x1 + c2*x2
    
    Trả về:
    - (best_vertex, best_val): Nghiệm tối ưu x* và giá trị cực đại f*
    """
    # Bước 1: Khởi tạo best_val = -float('inf') và best_vertex = None
    best_val = -float('inf')
    best_vertex = None

    # Bước 2: Duyệt qua từng đỉnh p = (x1, x2) trong danh sách vertices bằng vòng lặp
    for p in vertices:
        x1, x2 = p
        
        # Bước 3: Tính giá trị hàm mục tiêu tại đỉnh hiện tại: current_val = c1 * x1 + c2 * x2
        current_val = c1 * x1 + c2 * x2
        print(f"Xét đỉnh {p}: f({x1}, {x2}) = {c1}*{x1} + {c2}*{x2} = {current_val}")
        
        # Bước 4: Nếu current_val > best_val: Cập nhật best_val = current_val và best_vertex = p
        if current_val > best_val:
            best_val = current_val
            best_vertex = p

    # Bước 5: Trả về cặp kết quả (best_vertex, best_val)
    return best_vertex, best_val


# --- Khởi tạo dữ liệu theo đề bài ---
# Các đỉnh giao điểm của miền đa diện lồi: A(0, 0), B(0, 80), C(20, 60), D(50, 0)
vertices = [(0, 0), (0, 80), (20, 60), (50, 0)]

# Hàm mục tiêu: max f(x1, x2) = 40*x1 + 30*x2
c1 = 40
c2 = 30

# Chạy thuật toán và in kết quả ra màn hình
best_vertex, best_val = solve_lp_geometric(vertices, c1, c2)

print("\n--- KẾT QUẢ TỐI ƯU ---")
print(f"Nghiệm tối ưu x* = {best_vertex}")
print(f"Giá trị lợi nhuận cực đại f* = {best_val} USD")