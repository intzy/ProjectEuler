"""
Problem 076 of Project Euler.

https://projecteuler.net/problem=076
"""

from functools import cache


def problem076(n=100):
    """
    Let f(n, m) be the number of ways you can add positive integers <= m to make n.
    Then f(n, m) = f(n - m, m) + f(n, m - 1).
    """

    @cache
    def f(n, m):
        if m == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 0
        return f(n - m, m) + f(n, m - 1)

    return f(n, n - 1)
