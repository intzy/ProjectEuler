"""
Problem 157 of Project Euler.

https://projecteuler.net/problem=157
"""

from math import gcd, isqrt


def problem157():
    return solve(7)


def solve(n):
    g = pow(10, n)
    solns = set()
    for x in (
        [1] + list(range(2, isqrt(g * g) + 1, 2)) + list(range(5, isqrt(g * g) + 1, 10))
    ):
        if g * g % x:
            continue
        y = g * g // x
        d = gcd(x + g, y + g)
        for p in range(1, d + 1):
            if d % p == 0:
                a = (x + g) // p
                b = (y + g) // p
                solns.add((a, b, p))
    return len(solns)
