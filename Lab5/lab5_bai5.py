import math
from collections import Counter


def extract_vocabulary(emails):
    vocabulary = set()
    for words, _ in emails:
        vocabulary.update(words)
    return vocabulary


def train_naive_bayes(train_emails, alpha=1.0):
    if not train_emails:
        raise ValueError("Dữ liệu huấn luyện không được rỗng.")
    if alpha <= 0:
        raise ValueError("alpha phải lớn hơn 0.")

    vocabulary = extract_vocabulary(train_emails)
    if not vocabulary:
        raise ValueError("Từ điển rỗng.")

    class_docs = Counter()
    word_counts = {0: Counter(), 1: Counter()}
    total_words = {0: 0, 1: 0}

    for words, label in train_emails:
        if label not in (0, 1):
            raise ValueError("Nhãn email phải là 0 (Ham) hoặc 1 (Spam).")

        class_docs[label] += 1
        word_counts[label].update(words)
        total_words[label] += len(words)

    total_docs = len(train_emails)
    priors = {
        cls: class_docs[cls] / total_docs
        for cls in (0, 1)
    }

    likelihoods = {0: {}, 1: {}}
    vocab_size = len(vocabulary)

    for cls in (0, 1):
        denominator = total_words[cls] + alpha * vocab_size
        for word in vocabulary:
            likelihoods[cls][word] = (
                word_counts[cls][word] + alpha
            ) / denominator

    return {
        "vocabulary": vocabulary,
        "priors": priors,
        "likelihoods": likelihoods,
        "alpha": alpha,
    }


def predict_email(email_words, model):
    # Dùng log-likelihood để tránh underflow khi nhân nhiều xác suất nhỏ.
    vocabulary = model["vocabulary"]
    priors = model["priors"]
    likelihoods = model["likelihoods"]

    scores = {}
    for cls in (0, 1):
        if priors[cls] == 0:
            scores[cls] = float("-inf")
            continue

        score = math.log(priors[cls])
        for word in email_words:
            # Từ ngoài từ điển được bỏ qua vì mô hình không có xác suất đã học cho từ đó.
            if word in vocabulary:
                score += math.log(likelihoods[cls][word])
        scores[cls] = score

    return max(scores, key=scores.get)


if __name__ == "__main__":
    train_emails = [
        (["free", "money", "offer"], 1),
        (["free", "ticket", "win"], 1),
        (["money", "bonus", "free"], 1),
        (["meeting", "project", "deadline"], 0),
        (["project", "report", "review"], 0),
        (["schedule", "meeting", "room"], 0),
    ]

    vocabulary = extract_vocabulary(train_emails)
    print("Vocabulary:", sorted(vocabulary))

    model = train_naive_bayes(train_emails)
    print("P(Spam):", model["priors"][1])
    print("P(Ham):", model["priors"][0])

    test_email = ["free", "project", "bonus"]
    prediction = predict_email(test_email, model)
    print(f"Email {test_email} được phân loại: {prediction} ({'Spam' if prediction == 1 else 'Ham'})")

    # Ma trận nhầm lẫn trên chính tập huấn luyện: hàng là nhãn thực tế,
    # cột là nhãn dự đoán. Thứ tự lớp: 0 (Ham), 1 (Spam).
    confusion_matrix = [[0, 0], [0, 0]]
    for words, actual_label in train_emails:
        predicted_label = predict_email(words, model)
        confusion_matrix[actual_label][predicted_label] += 1

    print("Confusion Matrix (actual rows, predicted columns; labels [0, 1]):")
    for row in confusion_matrix:
        print(row)
