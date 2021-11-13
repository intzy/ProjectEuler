"""
Problem 196 of Project Euler.

https://projecteuler.net/problem=196
"""

from lib.euler_lib import sum_to_n
from lib.primes import list_primes_in_range


def problem196():
    return solve(5678027) + solve(7208785)


def solve(n):
    primes = set(list_primes_in_range(sum_to_n(n - 3) + 1, sum_to_n(n + 2) + 1))

    A = [list(range(sum_to_n(m - 1) + 1, sum_to_n(m) + 1)) for m in range(n - 2, n + 3)]
    is_prime = [[False for _ in range(n + 3)] for _ in range(6)]
    is_prime_triplet = [[False for _ in row] for row in A]
    for i, row in enumerate(A):
        for j, a in enumerate(row):
            if a in primes:
                is_prime[i][j] = True

    for i, row in enumerate(is_prime):
        for j, b in enumerate(row):
            if not b:
                continue
            adj = [
                (i + u, j + v)
                for u in range(-1, 2)
                for v in range(-1, 2)
                if is_prime[i + u][j + v]
            ]
            if len(adj) >= 3:
                for u, v in adj:
                    is_prime_triplet[u][v] = True

    return sum(a for i, a in enumerate(A[2]) if is_prime_triplet[2][i])
