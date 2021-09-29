"""
Problem 021 of Project Euler.

https://projecteuler.net/problem=021
"""

from lib.euler_lib import list_sum_proper_divisors


def problem021(limit=10_000):
    """
    Let d[n] be the sum of the proper divisors of n.
    """
    d = list_sum_proper_divisors(limit)
    return sum(n for n in range(limit) if d[n] < limit and d[n] != n and d[d[n]] == n)
