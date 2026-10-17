def naive_bayes_predict(dataset, x_new, alpha=1.0):
    """
    Naive Bayes cho đặc trưng nhị phân.
    Laplace smoothing được dùng để tránh xác suất likelihood bằng 0.
    Trả về nhãn dự đoán 0 hoặc 1.
    """
    if not dataset:
        raise ValueError("Dataset không được rỗng.")

    if not x_new:
        raise ValueError("x_new không được rỗng.")

    classes = sorted({label for _, label in dataset})
    if any(len(features) != len(x_new) for features, _ in dataset):
        raise ValueError("Các mẫu trong dataset phải có cùng số đặc trưng với x_new.")

    total = len(dataset)
    scores = {}

    for cls in classes:
        class_rows = [features for features, label in dataset if label == cls]
        class_count = len(class_rows)
        prior = class_count / total
        score = prior

        for i, value in enumerate(x_new):
            # Mỗi đặc trưng nhị phân có hai giá trị có thể: 0 và 1.
            count_value = sum(1 for row in class_rows if row[i] == value)
            likelihood = (count_value + alpha) / (class_count + 2 * alpha)
            score *= likelihood

        scores[cls] = score

    return max(scores, key=scores.get)


if __name__ == "__main__":
    dataset = [
        ([1, 1], 1),
        ([1, 0], 1),
        ([1, 1], 1),
        ([0, 1], 0),
        ([0, 0], 0),
        ([0, 0], 0),
    ]

    x_new = [1, 0]
    print(f"Nhãn dự đoán cho {x_new}: {naive_bayes_predict(dataset, x_new)}")
