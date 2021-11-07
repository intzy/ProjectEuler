"""
Problem 196 of Project Euler.

https://projecteuler.net/problem=196
"""

from itertools import product
from math import isqrt

from lib.euler_lib import list_primes, sum_to_n


def problem196():
    return solve(5678027) + solve(7208785)


def solve(n):
    small_primes = list_primes(isqrt(sum_to_n(n + 2)))
    large_primes = set(range(sum_to_n(n - 3) + 1, sum_to_n(n + 2) + 1))
    for p in small_primes:
        for m in range(sum_to_n(n - 3) // p, (sum_to_n(n + 2) + 1) // p + 1):
            if m * p in large_primes:
                large_primes.remove(m * p)

    A = [list(range(sum_to_n(m - 1) + 1, sum_to_n(m) + 1)) for m in range(n - 2, n + 3)]
    B = [[a in large_primes for a in row] for row in A]
    C = [[False for _ in row] for row in A]

    B[0] = B[0] + [False, False, False, False, False]
    B[1] = B[1] + [False, False, False, False]
    B[2] = B[2] + [False, False, False]
    B[3] = B[3] + [False, False]
    B[4] = B[4] + [False]
    length = len(B[4]) + 1
    B = B + [[False for _ in range(length)]] + [[False for _ in range(length)]]

    for i, row in enumerate(B):
        for j, b in enumerate(row):
            if not b:
                continue
            adj_primes = [
                (n, m)
                for n, m in product([i - 1, i, i + 1], [j - 1, j, j + 1])
                if B[n][m]
            ]
            if len(adj_primes) >= 3:
                for u, v in adj_primes:
                    C[u][v] = True

    return sum(a for i, a in enumerate(A[2]) if C[2][i])
