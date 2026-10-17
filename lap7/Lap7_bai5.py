import numpy as np
from collections import deque

# =====================================================================
# PHẦN 1: MÔ PHỎNG GOOGLE PAGERANK
# =====================================================================
def compute_pagerank(P_web, damping_factor=0.85, max_iter=100, tol=1e-6):
    """
    Tính điểm số uy tín PageRank cho các server.
    - P_web: Ma trận xác suất chuyển trạng thái (kích thước N x N),
             với P_web[i][j] là xác suất nhảy từ i -> j.
    - damping_factor (d): Xác suất người dùng tiếp tục đi theo liên kết.
    - (1 - d) / N: Xác suất người dùng nhảy ngẫu nhiên đến một server bất kỳ (Teleporting).
    """
    P = np.array(P_web, dtype=float)
    N = P.shape[0]
    
    # Khởi tạo vector điểm PageRank ban đầu r_0 = [1/N, 1/N, ..., 1/N]
    r = np.ones(N) / N
    
    # Ma trận chuyển tiếp có Teleportation (Google Matrix):
    # Nếu server i có hàng toàn số 0 (dangling node), ta phân phối đều xác suất 1/N
    for i in range(N):
        if np.sum(P[i]) == 0:
            P[i] = np.ones(N) / N
            
    # Công thức lặp Power Iteration theo dạng vector hàng:
    # r_{k+1} = d * (r_k * P) + (1 - d) / N
    teleport = np.ones(N) * ((1.0 - damping_factor) / N)
    
    for iteration in range(max_iter):
        r_next = damping_factor * np.dot(r, P) + teleport
        
        # Chuẩn hóa để tổng luôn bằng 1
        r_next = r_next / np.sum(r_next)
        
        # Kiểm tra điều kiện hội tụ
        if np.linalg.norm(r_next - r, 1) < tol:
            r = r_next
            break
        r = r_next

    return r


# =====================================================================
# PHẦN 2: XÁC ĐỊNH ĐIỂM NGHẼN MẠNG (MIN-CUT QUA MAX-FLOW)
# =====================================================================
def bfs_find_path(capacity, flow, source, sink, parent):
    """Tìm đường tăng luồng từ source đến sink bằng BFS."""
    visited = set([source])
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        if u == sink:
            return True
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
    return False

def find_min_cut(capacity_matrix, source, sink):
    """
    Sử dụng định lý Max-Flow Min-Cut:
    1. Chạy thuật toán Ford-Fulkerson (Edmonds-Karp) để tìm luồng cực đại.
    2. Tập S là các đỉnh đến được từ source trong đồ thị thặng dư (Residual Graph).
    3. Tập T = V \ S.
    4. Cạnh thuộc lát cắt hẹp nhất (Min-Cut) là các cạnh u -> v với u thuộc S, v thuộc T và capacity > 0.
    """
    n = len(capacity_matrix)
    capacity = np.array(capacity_matrix, dtype=float)
    flow = np.zeros((n, n), dtype=float)
    parent = {}

    # Bước 1: Tìm Max-Flow
    max_flow = 0
    while bfs_find_path(capacity, flow, source, sink, parent):
        path_flow = float('inf')
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, capacity[prev][curr] - flow[prev][curr])
            curr = prev

        curr = sink
        while curr != source:
            prev = parent[curr]
            flow[prev][curr] += path_flow
            flow[curr][prev] -= path_flow
            curr = prev

        max_flow += path_flow
        parent = {}

    # Bước 2: Tìm tập S từ source trên đồ thị thặng dư
    visited = set([source])
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(n):
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                visited.add(v)
                queue.append(v)

    S = visited
    T = set(range(n)) - S

    # Bước 3: Tìm các cạnh bị nghẽn (u in S, v in T, capacity[u][v] > 0)
    min_cut_edges = []
    min_cut_capacity = 0
    for u in S:
        for v in T:
            if capacity[u][v] > 0:
                min_cut_edges.append((u, v, capacity[u][v]))
                min_cut_capacity += capacity[u][v]

    return max_flow, S, T, min_cut_edges, min_cut_capacity


# =====================================================================
# THỰC THI & KIỂM THỬ
# =====================================================================
if __name__ == "__main__":
    servers = ['A', 'B', 'C', 'D']
    
    # 1. PageRank
    P_web = [
        [0.0, 0.5, 0.5, 0.0],  # A -> B, C
        [0.0, 0.0, 1.0, 0.0],  # B -> C
        [1.0, 0.0, 0.0, 0.0],  # C -> A
        [0.0, 0.5, 0.5, 0.0]   # D -> B, C
    ]
    
    ranks = compute_pagerank(P_web, damping_factor=0.85, max_iter=100)
    print("=== KẾT QUẢ GOOGLE PAGERANK ===")
    for server, score in zip(servers, ranks):
        print(f"Server {server}: {score:.5f}")

    # 2. Min-Cut / Max-Flow
    # Giả sử ma trận dung lượng mạng (băng thông Gbps) giữa các máy chủ:
    # 0: A, 1: B, 2: C, 3: D
    # Xét nguồn phát Server A (0) truyền dữ liệu đến Server D (3)
    bandwidth_matrix = [
        [0, 10, 15,  0],  # Từ A nối B (10), C (15)
        [0,  0,  5,  8],  # Từ B nối C (5), D (8)
        [0,  0,  0, 12],  # Từ C nối D (12)
        [0,  0,  0,  0]   # D
    ]
    
    src, snk = 0, 3  # Từ Server A sang Server D
    max_flow, S, T, cut_edges, cut_val = find_min_cut(bandwidth_matrix, src, snk)
    
    print("\n=== KẾT QUẢ ĐIỂM NGHẼN MẠNG (MIN-CUT) ===")
    print(f"Luồng cực đại (Max Flow) từ {servers[src]} đến {servers[snk]}: {max_flow} Gbps")
    print(f"Tập lát cắt S: {[servers[i] for i in S]}")
    print(f"Tập lát cắt T: {[servers[i] for i in T]}")
    print("Các đường cáp mạng chịu tải trọng yếu nhất (Điểm nghẽn Min-Cut):")
    for u, v, cap in cut_edges:
        print(f" - Đường {servers[u]} -> {servers[v]} (Dung lượng giới hạn: {cap} Gbps)")