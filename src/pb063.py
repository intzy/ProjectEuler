"""
Problem 063 of Project Euler.

https://projecteuler.net/problem=063
"""

from math import log10


def problem063():
    """
    Since 10^{n - 1} <= d^n < 10^n,
    you only need to check that d^n has length n for digits d.
    The right inequality is given automatically by our restriction of d,
    and solving for n for the left inequality gives that n <= 1 / (1 - log10(d)).
    """
    return sum(int(1 / (1 - log10(d))) for d in range(1, 10))
