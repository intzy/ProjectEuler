"""
Problem 026 of Project Euler.

https://projecteuler.net/problem=026
"""

from itertools import count


def problem026(limit=1_000):
    """
    The maximum length of the repeating decimal 1/n is n - 1.
    So it is natural to search downwards.
    Furthermore, factors of 2 or 5 in n don't increase the length of the
    repeating decimal.
    Actually calculating the length of the repeating decimal is simple long division.
    """
    max_cycle = 0
    m = None
    for n in reversed(range(limit)):
        if n <= max_cycle:
            return m
        if n % 2 == 0 or n % 5 == 0:
            continue
        length = cycle_length(n)
        if length > max_cycle:
            max_cycle = length
            m = n
    return None


def cycle_length(n):
    remainders = {}
    r = 1
    for i in count():
        r %= n
        if r in remainders:
            return i - remainders[r]
        remainders[r] = i
        r *= 10
    return None
