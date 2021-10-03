"""
Problem 052 of Project Euler.

https://projecteuler.net/problem=052
"""

from itertools import count

from lib.euler_lib import is_digit_permutation


def problem052(multiples=6):
    return next(
        n
        for i in count()
        for n in range(10 ** i, int(10 / multiples * 10 ** i) + 1)
        if all(is_digit_permutation(n, c * n) for c in range(2, multiples))
    )
