from collections import deque


def bfs_find_path(residual, s, t, parent):
    """Tìm đường tăng luồng từ s đến t trên ma trận thặng dư bằng BFS."""
    visited = set([s])
    queue = deque([s])

    while queue:
        u = queue.popleft()

        # Duyệt qua các đỉnh kề có dung lượng thặng dư > 0
        for v in range(len(residual)):
            if v not in visited and residual[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == t:
                    return True
                queue.append(v)

    return False


def ford_fulkerson(C, s, t):
    # Khởi tạo ma trận thặng dư residual = [row[:] for row in C] và max_flow = 0
    residual = [row[:] for row in C]
    n = len(C)
    max_flow = 0

    parent = [-1] * n

    # Lặp lại việc tìm đường tăng luồng từ s đến t cho đến khi không còn đường đi
    while bfs_find_path(residual, s, t, parent):
        # Tìm dung lượng nghẽn (bottleneck) trên đường tăng luồng
        bottleneck = float("inf")
        curr = t
        while curr != s:
            prev = parent[curr]
            bottleneck = min(bottleneck, residual[prev][curr])
            curr = prev

        # Cập nhật mạng thặng dư:
        # Giảm dung lượng cạnh thuận và tăng dung lượng cạnh nghịch
        curr = t
        while curr != s:
            prev = parent[curr]
            residual[prev][curr] -= bottleneck  # Cạnh thuận
            residual[curr][prev] += bottleneck  # Cạnh nghịch
            curr = prev

        # Cộng dồn bottleneck vào max_flow
        max_flow += bottleneck

    return max_flow


# ================= Test case mẫu =================
# Ma trận dung lượng C (4 đỉnh: 0, 1, 2, 3)
C = [
    [0, 10, 10, 0],  # s (0)
    [0, 0, 2, 8],  # u (1)
    [0, 0, 0, 9],  # v (2)
    [0, 0, 0, 0],  # t (3)
]

s = 0
t = 3

result = ford_fulkerson(C, s, t)
print(f"Luồng cực đại Max Flow từ {s} đến {t} là: {result}")