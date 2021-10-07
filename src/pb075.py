"""
Problem 075 of Project Euler.

https://projecteuler.net/problem=075
"""

from math import gcd, isqrt


def problem075(L=1_500_000):
    perimeters = [0] * (L + 1)
    for m in range(2, isqrt(L) + 1):
        for n in range(m - 1, 0, -2):
            if gcd(m, n) != 1:
                continue
            a = pow(m, 2) - pow(n, 2)
            b = 2 * m * n
            c = pow(m, 2) + pow(n, 2)
            for k in range(1, L // (a + b + c) + 1):
                perimeters[k * (a + b + c)] += 1
    return perimeters.count(1)
