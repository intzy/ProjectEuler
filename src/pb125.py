"""
Problem 125 of Project Euler.

https://projecteuler.net/problem=125
"""

from math import isqrt

from lib.misc import is_palindrome


def problem125(limit=pow(10, 8)):
    squares = [m ** 2 for m in range(1, isqrt(limit))]
    palindromes = set()
    for i, square_sum in enumerate(squares[:-1]):
        for square in squares[i + 1 :]:
            square_sum += square
            if square_sum > limit:
                break
            if is_palindrome(square_sum):
                palindromes.add(square_sum)
    return sum(palindromes)
