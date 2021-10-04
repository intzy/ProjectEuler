"""
Problem 719 of Project Euler.

https://projecteuler.net/problem=719
"""

from itertools import chain
from math import isqrt


def problem719(limit=pow(10, 12)):
    """
    Recall that a number is divisible by 9 if and only if the sum of its
    digits is divisible by 9.

    In particualar, taking the digit sum of n preserves the value of n mod 9.
    Therefore, all S-number satisfay n = sqrt(n) (mod 9).
    And so, n (and hence sqrt(n)) must be congruent to 0 or 1 mod 9.
    """
    return sum(
        n * n
        for n in chain(range(9, isqrt(limit) + 1, 9), range(10, isqrt(limit) + 1, 9))
        if split_x_to_make_y(n * n, n)
    )


def split_x_to_make_y(n1, n2):
    """
    Returns True if and only if n1 can be split so that the sum of the parts equals n2.
    """
    if n1 <= n2:
        return n1 == n2
    d = 10
    while n2 - n1 % d > 0:
        if split_x_to_make_y(n1 // d, n2 - (n1 % d)):
            return True
        d *= 10
    return False
