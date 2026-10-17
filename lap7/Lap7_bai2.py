from collections import deque


def is_bipartite_bfs(adj_list, num_nodes):
    # Bước 1: Khởi tạo từ điển màu color = {}
    color = {}

    # Duyệt qua các đỉnh từ 0 đến num_nodes - 1 (xử lý đồ thị có nhiều thành phần rời rạc)
    for start in range(num_nodes):
        # Bước 2: Nếu đỉnh start chưa được tô màu, gán color[start] = 0 và đưa vào Queue
        if start not in color:
            color[start] = 0
            queue = deque([start])

            # Bước 3: Vòng lặp while queue
            while queue:
                u = queue.popleft()

                # Duyệt qua các đỉnh kề v của u
                for v in adj_list.get(u, []):
                    # Bước 4: Nếu v chưa có màu, gán màu đối lập (1 - color[u]) và đưa vào Queue
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    # Bước 5: Nếu v đã có màu và cùng màu với u -> Xung đột màu
                    elif color[v] == color[u]:
                        return False

    # Bước 6: Nếu duyệt hết toàn bộ đồ thị mà không có xung đột màu
    return True


# ================= Ví dụ kiểm thử =================

# Test case 1: Đồ thị hai phía (chu trình chẵn: 0 - 1 - 2 - 3 - 0)
adj_list_1 = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
print(
    "Đồ thị 1 có phải đồ thị hai phía?", is_bipartite_bfs(adj_list_1, 4)
)  # Kết quả: True

# Test case 2: Không phải đồ thị hai phía (chu trình lẻ - tam giác: 0 - 1 - 2 - 0)
adj_list_2 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
print(
    "Đồ thị 2 có phải đồ thị hai phía?", is_bipartite_bfs(adj_list_2, 3)
)  # Kết quả: False