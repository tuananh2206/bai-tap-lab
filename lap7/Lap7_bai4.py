from collections import deque, defaultdict

def bfs(capacity, flow, source, sink, parent):
    """Tìm đường tăng luồng từ source đến sink bằng BFS."""
    visited = set([source])
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        if u == sink:
            return True
        for v in capacity[u]:
            # Nếu còn dung lượng dư (residual capacity) và chưa thăm đỉnh v
            residual = capacity[u][v] - flow[u][v]
            if v not in visited and residual > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
    return False

def ford_fulkerson(capacity, source, sink):
    """Tính toán luồng cực đại bằng thuật toán Ford-Fulkerson / Edmonds-Karp."""
    flow = defaultdict(lambda: defaultdict(int))
    parent = {}
    max_flow = 0

    while bfs(capacity, flow, source, sink, parent):
        # Tìm dung lượng thắt nút (bottleneck) trên đường tăng luồng
        path_flow = float('inf')
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, capacity[prev][curr] - flow[prev][curr])
            curr = prev

        # Cập nhật luồng trên các cạnh xuôi và ngược
        curr = sink
        while curr != source:
            prev = parent[curr]
            flow[prev][curr] += path_flow
            flow[curr][prev] -= path_flow
            curr = prev

        max_flow += path_flow
        parent = {}

    return max_flow

def solve_bipartite_matching(L, R, candidate_edges):
    """
    Quy đổi bài toán Maximum Bipartite Matching sang Maximum Flow:
    - s = 4, t = 5
    - Nối s -> u (u thuộc L) với c = 1
    - Nối u -> v (u thuộc L, v thuộc R từ candidate_edges) với c = 1
    - Nối v -> t (v thuộc R) với c = 1
    """
    s = 4
    t = 5
    capacity = defaultdict(lambda: defaultdict(int))

    # 1. Nối đỉnh phát s -> u (u thuộc L) với dung lượng 1
    for u in L:
        capacity[s][u] = 1

    # 2. Nối u -> v theo candidate_edges với dung lượng 1
    for u, v in candidate_edges:
        capacity[u][v] = 1

    # 3. Nối v -> t (v thuộc R) với dung lượng 1
    for v in R:
        capacity[v][t] = 1

    # 4. Tìm luồng cực đại từ s đến t
    return ford_fulkerson(capacity, s, t)

# --- Chạy thử với test case mẫu ---
L = {0, 1}
R = {2, 3}
# Ứng viên 0 làm được [2, 3] -> cạnh (0, 2), (0, 3)
# Ứng viên 1 làm được [2]    -> cạnh (1, 2)
candidate_edges = [(0, 2), (0, 3), (1, 2)]

max_matching = solve_bipartite_matching(L, R, candidate_edges)
print("Số lượng cặp ghép tối đa:", max_matching)