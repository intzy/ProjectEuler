"""
Problem 174 of Project Euler.

https://projecteuler.net/problem=174
"""

from math import isqrt


def problem174(limit=10 ** 6):
    num_solns = [0 for _ in range(limit + 1)]
    for x in range(1, isqrt(limit // 4) + 1):
        for c in range(1, limit // (4 * x) - x + 1):
            num_solns[4 * (x * x + c * x)] += 1
    return sum(1 for n in num_solns if 1 <= n <= 10)
