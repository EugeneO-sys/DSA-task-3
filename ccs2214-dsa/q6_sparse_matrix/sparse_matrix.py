"""
Question 6 - Sparse matrix represented with arrays (triplet / 3-column form).

Only non-zero elements are stored as rows of  [row, column, value].
The first row is a header holding [total_rows, total_cols, non_zero_count].
"""


def to_sparse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    triplets = [[rows, cols, 0]]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                triplets.append([i, j, matrix[i][j]])
    triplets[0][2] = len(triplets) - 1
    return triplets


def to_dense(sparse):
    rows, cols, _ = sparse[0]
    m = [[0] * cols for _ in range(rows)]
    for r, c, v in sparse[1:]:
        m[r][c] = v
    return m


def transpose(sparse):
    rows, cols, n = sparse[0]
    t = [[cols, rows, n]] + [[c, r, v] for r, c, v in sparse[1:]]
    return [t[0]] + sorted(t[1:], key=lambda x: (x[0], x[1]))


def memory_cells(dense, sparse):
    return len(dense) * len(dense[0]), len(sparse) * 3


def show(title, m):
    print(title)
    for row in m:
        print("  ", row)


if __name__ == "__main__":
    dense = [
        [0, 0, 0, 0, 0, 9],
        [0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
    ]
    show("Dense 6x6 matrix:", dense)
    sp = to_sparse(dense)
    print("\nSparse (triplet) form  [row, col, value]:")
    print("   [rows, cols, nonzero] =", sp[0])
    for t in sp[1:]:
        print("                         ", t)
    assert to_dense(sp) == dense
    show("\nTranspose (sparse):", transpose(sp))
    d, s = memory_cells(dense, sp)
    print(f"\nStorage: dense = {d} cells, sparse = {s} cells")
