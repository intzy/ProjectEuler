"""
Problem 055 of Project Euler.

https://projecteuler.net/problem=055
"""

from lib.euler_lib import is_palindrome


def problem055(limit=10_000, iterations=50):
    return sum(1 for n in range(limit) if is_lychrel(n, iterations))


def is_lychrel(n, iterations):
    for _ in range(iterations):
        n += reverse(n)
        if is_palindrome(n):
            return False
    return True


def reverse(n):
    return int(str(n)[::-1])
