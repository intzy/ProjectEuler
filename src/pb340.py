"""
Problem 340 of Project Euler.

https://projecteuler.net/problem=340
"""

from lib.misc import sum_to_n


def problem340(a=21 ** 7, b=7 ** 21, c=12 ** 7, modulo=10 ** 9):
    y = b + 1 - c
    diff = 3 * (c - a)
    m = (b + 1) // a
    ans = a * m * y - a * diff * sum_to_n(m) + m * sum_to_n(a - 1)
    n = b + 1 - (m + 1) * a
    y = y - m * diff
    ans += (n + a) * (y - diff - n) + sum_to_n(n + a - 1)
    return ans % modulo
