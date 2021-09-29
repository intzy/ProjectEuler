"""
Problem 033 of Project Euler.

https://projecteuler.net/problem=033
"""

from itertools import combinations
from math import gcd


def problem033():
    """
    After some analysis, it suffices to find fractions such that xy/yz = x/z,
    where x, y, z are digits.
    """
    numerator, denominator = 1, 1
    for x, y, z in combinations(range(1, 10), 3):
        if 9 * x * (y - z) == z * (x - y):
            numerator *= x
            denominator *= y
    return denominator // gcd(denominator, numerator)
