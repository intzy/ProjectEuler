"""
Problem 012 of Project Euler.

https://projecteuler.net/problem=012
"""

from itertools import count


def problem012(divisor_count=500):
    """
    Let d(x) be the number of divisors that x has.
    Recall that if m and n are coprime, then d(nm) = d(m)d(n).
    Furthermore, n and (n + 1) / 2; and n / 2 and (n + 1) are coprime.
    """
    divisor_limit = 2 ** 4
    d = list_divisor_count(divisor_limit)

    for n in count(2, 2):
        # Resize d if necessary.
        if n + 2 == divisor_limit:
            divisor_limit *= 4
            d = list_divisor_count(divisor_limit)

        if divisor_count < d[n // 2] * d[n + 1]:
            return n * (n + 1) // 2
        n += 1
        if divisor_count < d[n] * d[(n + 1) // 2]:
            return n * (n + 1) // 2


def list_divisor_count(limit):
    d = [1] * limit
    for n in range(2, limit):
        for m in range(n, limit, n):
            d[m] += 1
    return d
