"""
Problem 034 of Project Euler.

https://projecteuler.net/problem=034
"""

FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def problem034():
    # A natural upper bound is 7 * 9!.
    return sum(n for n in range(3, 7 * FACTORIALS[9]) if n == digit_factorial(n))


def digit_factorial(n):
    x = 0
    while n > 0:
        d, n = n % 10, n // 10
        x += FACTORIALS[d]
    return x
