"""
Problem 024 of Project Euler.

https://projecteuler.net/problem=024
"""

from math import factorial


def problem024(n=1_000_000):
    """
    You can quickly find the n'th lexographic permutation by using the fact that
    for i distinct characters, there are i! permutations...
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutation = 0
    count = 0
    for i in reversed(range(len(digits))):
        j = (n - count - 1) // factorial(i)
        permutation = 10 * permutation + digits[j]
        digits.remove(digits[j])
        count += j * factorial(i)
    return permutation
