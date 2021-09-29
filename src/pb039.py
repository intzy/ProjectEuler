"""
Problem 039 of Project Euler.

https://projecteuler.net/problem=039
"""

from math import gcd, isqrt


def problem039(max_perimeter=1000):
    perimeters = [0] * (max_perimeter + 1)
    for m in range(2, isqrt(max_perimeter)):
        for n in range(m - 1, 0, -2):
            if gcd(m, n) != 1:
                continue
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            for k in range(1, max_perimeter // (a + b + c) + 1):
                perimeters[k * (a + b + c)] += 1
    return max(range(max_perimeter + 1), key=lambda i: perimeters[i])
