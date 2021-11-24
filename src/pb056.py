"""
Problem 056 of Project Euler.

https://projecteuler.net/problem=056
"""

from lib.misc import digit_sum


def problem056(limit=100):
    return max(digit_sum(a ** b) for a in range(limit) for b in range(limit))
