"""
Problem 345 of Project Euler.

https://projecteuler.net/problem=345
"""

from itertools import combinations

from lib.misc import file_to_matrix


def problem345(filename="txt/pb345.txt"):
    M = file_to_matrix(filename, " ")
    return matrix_sum(M)


def matrix_sum(M):
    cache = {tuple([n]): m for n, m in enumerate(M[0])}
    for r in range(2, len(M) + 1):
        for c in combinations(range(len(M)), r):
            cache[c] = max(
                M[r - 1][n] + cache[c[:i] + c[i + 1 :]] for i, n in enumerate(c)
            )
    return cache[tuple(range(len(M)))]
