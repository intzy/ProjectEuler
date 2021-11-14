"""
Problem 139 of Project Euler.

https://projecteuler.net/problem=139
"""

from math import gcd, isqrt


def problem139(limit=100000000):
    count = 0
    for u in range(2, int(-1 / 2 + 1 / 2 * isqrt(1 + 2 * limit))):
        for v in range(1 + (u % 2), min(u, (limit - 2 * u * u) // (2 * u) + 1), 2):
            if gcd(u, v) - 1:
                continue
            a = u * u - v * v
            b = 2 * u * v
            c = u * u + v * v
            if c % abs(a - b):
                continue
            count += limit // (a + b + c)
    return count
