from collections import Counter

def confusion_matrix(data):
    cnt = Counter([tuple(el) for el in data])
    return [[cnt[(1, 1)], cnt[(1, 0)]], [cnt[(0, 1)], cnt[(0, 0)]]]