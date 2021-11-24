"""
Problem 036 of Project Euler.

https://projecteuler.net/problem=036
"""

from lib.misc import is_palindrome


def problem036(bound=1_000_000):
    return sum(
        n
        for n in range(1, bound)
        if is_palindrome(n) and is_palindrome(int(bin(n)[2:]))
    )
