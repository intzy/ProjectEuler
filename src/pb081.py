"""
Problem 081 of Project Euler.

https://projecteuler.net/problem=081

Dynamic Programming.
"""

from lib.misc import file_to_matrix


def problem081(filename="txt/pb081.txt"):
    M = file_to_matrix(filename, ",")
    l = len(M)
    for k in range(1, l):
        M[k][0] += M[k - 1][0]
        for i in range(1, k):
            M[k - i][i] += min(M[k - i - 1][i], M[k - i][i - 1])
        M[0][k] += M[0][k - 1]
    for k in range(1, l):
        for i in range(k, l):
            M[l + k - i - 1][i] += min(M[l + k - i - 2][i], M[l + k - i - 1][i - 1])
    return M[-1][-1]
