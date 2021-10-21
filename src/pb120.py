"""
Problem 120 of Project Euler.

https://projecteuler.net/problem=120
"""


def problem120(k=1000):
    return sum(
        max(2, max(2 * n * a % (a * a) for n in range(1, a))) for a in range(3, k + 1)
    )
