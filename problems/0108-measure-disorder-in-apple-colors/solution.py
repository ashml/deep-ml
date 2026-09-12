from collections import Counter
from math import log2

def disorder(apples: list) -> float:
    n = len(apples)
    cnt = Counter(apples)

    return -1 * sum((count / n) * log2(count / n) for count in cnt.values())