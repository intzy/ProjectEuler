"""
Problem 064 of Project Euler.

https://projecteuler.net/problem=064
"""


from math import isqrt

from lib.misc import is_square


def problem064(N=10_000):
    """
    We simply check the cycle length of the continued fraction of sqrt(n)
    each non-square positive integer n <= N.
    """
    return sum(1 for n in range(2, N + 1) if not is_square(n) and cf_period(n) % 2 == 1)


def cf_period(n):
    """
    y / (sqrt(n) - x) = y (sqrt(n) + x) / (n - x^2)
                      = (sqrt(n) + x) / ynew
                      = a + (sqrt(n) - xnew) / ynew
    It we encounter the same (x, y) as before, then we hit a new cycle.
    """
    remainders = []
    x = isqrt(n)
    y = 1
    while (x, y) not in remainders:
        remainders.append((x, y))
        y = (n - pow(x, 2)) // y
        a = (isqrt(n) + x) // y
        x = y * a - x
    return len(remainders) - remainders.index((x, y))
