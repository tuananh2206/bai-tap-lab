from collections import deque
from copy import deepcopy


def flood_fill_bfs(image, start_row, start_col, new_color):
    if not image or not image[0]:
        return image

    rows = len(image)
    cols = len(image[0])

    if any(len(row) != cols for row in image):
        raise ValueError("Ma tran anh khong hop le.")

    if not (0 <= start_row < rows and
            0 <= start_col < cols):
        raise IndexError("Toa do pixel nam ngoai ma tran.")

    original_color = image[start_row][start_col]

    if original_color == new_color:
        return image

    queue = deque([(start_row, start_col)])
    image[start_row][start_col] = new_color

    directions = [
        (-1, 0),  # Tren
        (1, 0),   # Duoi
        (0, -1),  # Trai
        (0, 1)    # Phai
    ]

    # Do phuc tap thoi gian: O(M * N) trong truong hop xau nhat.
    # Do phuc tap bo nho: O(M * N) trong truong hop xau nhat.
    # Moi pixel la mot dinh cua do thi luoi 2D,
    # co toi da 4 dinh ke: tren, duoi, trai va phai.

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if image[nr][nc] == original_color:
                    image[nr][nc] = new_color
                    queue.append((nr, nc))

    return image


if __name__ == "__main__":
    image = [
        [1, 1, 1, 0, 0],
        [1, 1, 0, 0, 2],
        [1, 0, 0, 2, 2],
        [0, 0, 2, 2, 2]
    ]

    result = flood_fill_bfs(
        deepcopy(image),
        0,
        0,
        3
    )

    print("Anh ban dau:")
    for row in image:
        print(row)

    print("\nAnh sau Flood Fill:")
    for row in result:
        print(row)