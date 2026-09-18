
def orthogonal_projection(v, L):
    dot_product = sum(v[i] * L[i] for i in range(len(v)))
    l_squared = sum(x ** 2 for x in L)
    projection = [(dot_product / l_squared) * x for x in L]
    return [round(x, 3) for x in projection]