"""
Problem 053 of Project Euler.

https://projecteuler.net/problem=053
"""

from math import comb


def problem053(bound=1_000_000, limit=100):
    return sum(
        1 for n in range(1, limit + 1) for r in range(2, n - 1) if comb(n, r) > bound
    )
