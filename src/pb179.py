"""
Problem 179 of Project Euler.

https://projecteuler.net/problem=179
"""


def problem179(limit=10 ** 7):
    divisors = [2] * (limit + 1)
    for n in range(2, limit // 2 + 1):
        for i in range(2 * n, limit, n):
            divisors[i] += 1

    return sum(1 for n in range(2, limit) if divisors[n] == divisors[n + 1])
