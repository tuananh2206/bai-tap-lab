import math


def compute_entropy(labels):
    if not labels:
        return 0.0

    total_samples = len(labels)
    label_counts = {}

    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    entropy = 0.0
    for count in label_counts.values():
        p = count / total_samples
        if p > 0:
            entropy -= p * math.log2(p)

    return round(entropy, 4)


if __name__ == "__main__":
    labels_mixed = ["Yes", "Yes", "No", "Yes", "No"]
    labels_pure = ["Yes", "Yes", "Yes"]

    print(f"Entropy tập hỗn loạn (3 Yes, 2 No): {compute_entropy(labels_mixed)} bits")
    print(f"Entropy tập tinh khiết (100% Yes): {compute_entropy(labels_pure)} bits")
