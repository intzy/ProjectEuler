"""
Problem 004 of Project Euler.

https://projecteuler.net/problem=004
"""

from lib.euler_lib import is_palindrome


def problem004():
    """
    Brute force downward search on reduced search space.
    The palindrome ab, with a <= b, must be divisible by 11,
    hence one of the 3-digit numbers a or b must also be divisible by 11,
    since 11 is prime.
    """

    largest_palindrome = 0

    for a in range(990, 0, -1):
        if a * 999 <= largest_palindrome:
            return largest_palindrome

        skip, start = (-1, 999) if a % 11 == 0 else (-11, 990)
        for b in range(start, max(a - 1, largest_palindrome // a), skip):
            if is_palindrome(a * b):
                largest_palindrome = a * b
                break

    return None
