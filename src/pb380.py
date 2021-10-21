"""
Problem 380 of Project Euler.

https://projecteuler.net/problem=380

Kirchoff's Theorem is revelent.
Recall log(det(A)) = trace(log(A)).
If M = LU, since det(L) = 1, we see trace(log(L)) = 0.
Since det(U) = prod(D), where D is the diagonal entries of D,
we see log(det(U)) = sum(log(D)), where the log is taken component-wise.
"""

import numpy as np
from numpy import log
from scipy.sparse import diags
from scipy.sparse.linalg import splu


def problem380(m=100, n=500):
    A = grid_adjacency_matrix(m, n)
    D = grid_degree_matrix(m, n)
    M = D - A
    M.resize(m * n - 1, m * n - 1)

    log10det = log(splu(M).U.diagonal()).sum() / log(10)
    exponent = int(log10det)
    mantissa = round(10 ** (log10det % 1), 4)
    return str(mantissa) + "e" + str(exponent)


def grid_adjacency_matrix(m, n):
    right_adjacency = [0 if i % n == n - 1 else 1 for i in range(n * m - 1)]
    left_adjacency = [right_adjacency][-1] + right_adjacency[:-1]
    vertical_adjaceny = [1 for _ in range(m * n - 1)]
    diagonals = [right_adjacency, left_adjacency, vertical_adjaceny, vertical_adjaceny]
    offsets = [1, -1, n, -n]
    return diags(diagonals, offsets, dtype=np.longlong).tocsc()


def grid_degree_matrix(m, n):
    degrees = [3 if i % n in {0, n - 1} else 4 for i in range(m * n)]
    for i in range(n):
        degrees[i] -= 1
        degrees[(m - 1) * n + i] -= 1
    return diags(degrees, 0, dtype=np.longlong).tocsc()
