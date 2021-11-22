"""
Problem 173 of Project Euler.

https://projecteuler.net/problem=173
"""

from math import isqrt


def problem173(limit=10 ** 6):
    ans = 0
    for x in range(1, isqrt(limit // 4) + 1):
        ans += limit // (4 * x) - x
    return ans
