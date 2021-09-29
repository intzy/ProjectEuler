"""
Problem 006 of Project Euler.

https://projecteuler.net/problem=006
"""

from lib.euler_lib import sum_to_n


def problem006(n=100):
    """
    Recall that
        1 + 2 +...+ n = n(n + 1)/2
    and
        1^2 + 2^2 +...+ n^2 = n(n + 1)(2n + 1) / 6.
    """
    sqaure_of_sum = sum_to_n(n) ** 2
    sum_of_squares = (2 * n + 1) * (n + 1) * n // 6
    return sqaure_of_sum - sum_of_squares
