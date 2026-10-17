import math


def binary_cross_entropy(y_true, y_pred, eps=1e-15):
    if y_true not in (0, 1):
        raise ValueError("y_true phải là 0 hoặc 1.")
    if not 0 < eps < 0.5:
        raise ValueError("eps phải nằm trong khoảng (0, 0.5).")

    y_pred = max(eps, min(1 - eps, float(y_pred)))
    loss = -(y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred))
    return loss


def laplace_smoothing(count_word, count_class, vocab_size, alpha=1.0):
    if count_word < 0 or count_class < 0:
        raise ValueError("Các số đếm không được âm.")
    if vocab_size <= 0:
        raise ValueError("vocab_size phải lớn hơn 0.")
    if alpha <= 0:
        raise ValueError("alpha phải lớn hơn 0.")

    return (count_word + alpha) / (count_class + alpha * vocab_size)


if __name__ == "__main__":
    print(f"Loss khi dự đoán chuẩn (y=1, p=0.9): {binary_cross_entropy(1, 0.9):.4f}")
    print(f"Loss khi dự đoán sai (y=1, p=0.1): {binary_cross_entropy(1, 0.1):.4f}")

    p_smoothed = laplace_smoothing(count_word=0, count_class=100, vocab_size=500)
    print(f"Xác suất sau làm mượt: {p_smoothed:.4f}")
