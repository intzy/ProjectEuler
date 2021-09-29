"""
Problem 048 of Project Euler.

https://projecteuler.net/problem=048
"""


def problem048(limit=1000, modulo=10 ** 10):
    return sum(pow(n, n, modulo) for n in range(1, limit + 1)) % modulo
