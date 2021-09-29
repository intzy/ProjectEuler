"""
Problem 005 of Project Euler.

https://projecteuler.net/problem=005
"""

from functools import reduce
from math import lcm


def problem005(n=20):
    return reduce(lcm, range(2, n + 1))
