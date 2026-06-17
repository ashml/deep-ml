def compressed_col_sparse_matrix(dense_matrix):
    vals, row_idx, col_ptr = [], [], [0]
    n, m = len(dense_matrix), len(dense_matrix[0])
    for j in range(m):
        for i in range(n):
            if dense_matrix[i][j] != 0:
                vals.append(dense_matrix[i][j])
                row_idx.append(i)
        col_ptr.append(len(vals))      
    return vals, row_idx, col_ptr