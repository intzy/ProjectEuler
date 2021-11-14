"""
Problem 157 of Project Euler.

https://projecteuler.net/problem=157
"""

from itertools import product
from math import gcd

from sympy import divisor_count


def problem157(limit=9):
    return sum(solve(n) for n in range(1, limit + 1))


def solve(n):
    g = pow(10, n)
    count = 0
    for e1, e2 in product(range(2 * n + 1), repeat=2):
        x = 2 ** e1 * 5 ** e2
        y = g * g // x
        if x > y:
            continue
        d = gcd(x + g, y + g)
        count += divisor_count(d)
    return count
