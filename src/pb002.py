"""
Problem 002 of Project Euler.

https://projecteuler.net/problem=002
"""


def problem002(limit=4_000_000):
    """
    One can prove the recurrence relation for even fibonacci numbers is
    f_n = 4 * f_{n - 1} + f_{n - 2}, with a_1 = 2, a_2 = 8.
    """
    f = [2, 8]
    while f[-1] < limit:
        f.append(4 * f[-1] + f[-2])
    return sum(f[:-1])
