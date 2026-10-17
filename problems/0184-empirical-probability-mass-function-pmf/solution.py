from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    n = len(samples)
    cnt = Counter(samples)
    return [(el, cnt[el] / n) for el in cnt]