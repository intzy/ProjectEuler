"""
Problem 080 of Project Euler.

https://projecteuler.net/problem=080
"""

from math import isqrt

from lib.misc import is_square


def problem080(num_digits=100, limit=100):
    return sum(
        square_root_digit_sum(n, num_digits)
        for n in range(1, limit + 1)
        if not is_square(n)
    )


def square_root_digit_sum(n, num_digits):
    n *= 10 ** (2 * num_digits)
    return sum(int(d) for d in str(isqrt(n))[:num_digits])
