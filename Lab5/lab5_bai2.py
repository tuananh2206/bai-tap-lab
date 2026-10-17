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

    return entropy


def compute_information_gain(parent_labels, subsets_labels):
    if not parent_labels:
        return 0.0

    h_parent = compute_entropy(parent_labels)
    total_len = len(parent_labels)

    h_children = 0.0
    for subset in subsets_labels:
        if subset:
            weight = len(subset) / total_len
            h_children += weight * compute_entropy(subset)

    return round(h_parent - h_children, 4)


if __name__ == "__main__":
    parent = ["Yes", "Yes", "No", "No"]
    sub1 = ["Yes", "Yes"]
    sub2 = ["No", "No"]

    ig = compute_information_gain(parent, [sub1, sub2])
    print(f"Information Gain thu được: {ig} bits")
