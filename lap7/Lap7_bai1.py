def simulate_markov_chain(P, pi_0, num_steps=1000):
    # Bước 1: Khởi tạo vector phân phối hiện tại
    pi = list(pi_0)
    n = len(pi)

    # Bước 2: Vòng lặp chạy num_steps lần
    for step in range(num_steps):
        # Bước 3: Tính pi_next = pi * P
        pi_next = [0.0] * n
        for j in range(n):
            pi_next[j] = sum(pi[i] * P[i][j] for i in range(n))

        # Bước 5 (Kiểm tra hội tụ sớm): hiệu số abs(pi_next[j] - pi[j]) < 1e-6
        if all(abs(pi_next[j] - pi[j]) < 1e-6 for j in range(n)):
            pi = pi_next
            break

        # Bước 4: Cập nhật pi = pi_next
        pi = pi_next

    # Làm tròn 4 chữ số thập phân trước khi trả về
    pi_star = [round(val, 4) for val in pi]
    return pi_star


# Dữ liệu đầu vào mẫu
P = [
    [0.8, 0.2],  # Nắng
    [0.4, 0.6],  # Mưa
]
pi_0 = [1.0, 0.0]  # Ngày đầu chắc chắn Nắng

# Chạy mô phỏng
pi_star = simulate_markov_chain(P, pi_0, num_steps=100)

print(f"Trạng thái ban đầu: {pi_0}")
print(f"Trạng thái dừng (pi*): {pi_star}")