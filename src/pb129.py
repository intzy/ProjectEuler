"""
Problem 129 of Project Euler.

https://projecteuler.net/problem=129
"""

from itertools import count
from math import gcd


def problem129(bound=1000000):
    return next(n for n in count(bound) if gcd(n, 10) == 1 and A(n) > bound)


def A(n):
    c = 1
    x = 1
    while x:
        x = (10 * x + 1) % n
        c += 1
    return c
