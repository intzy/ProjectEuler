"""
Problem 173 of Project Euler.

https://projecteuler.net/problem=173
"""

from math import isqrt

from lib.euler_lib import sum_to_n


def problem173(limit=1000000):
    c = int(0.5 * (1 + isqrt(1 + limit)))
    ans = sum_to_n(c - 1)

    limit //= 4
    y = c + 1
    for n in range(limit // y, 0, -1):
        ynext = limit // n + 1
        ans += (ynext - y) * n
        y = ynext
    return ans
