"""
Problem 115 of Project Euler.

https://projecteuler.net/problem=115
"""

from itertools import count


def problem115(m=50, limit=1_000_000):
    return next(n for n in count(m) if F(m, n) > limit)


def F(m, n):
    f = [None] * (n + 1)
    for i in range(m):
        f[i] = 1
    f[m] = 2
    for i in range(m + 1, n + 1):
        f[i] = 1 + f[i - 1] + sum(f[0 : i - m])
    return f[n]
