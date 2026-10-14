from collections import Counter

def balance_undersample(data):
    if not data:
        return []

    counts = Counter(label for sample, label in data)
    min_count = min(counts.values())

    kept = Counter()
    result = []

    for sample, label in data:
        if kept[label] < min_count:
            result.append((sample, label))
            kept[label] += 1

    return result
