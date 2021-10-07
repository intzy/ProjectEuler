"""
Problem 092 of Project Euler.

https://projecteuler.net/problem=092
"""

from itertools import combinations_with_replacement
from math import factorial, prod


def problem092(power=7):
    """
    Instead of checking each number, check the permuations of digit combinations.
    """
    sequences = [None] * (81 * power + 1)
    sequences[1] = False
    sequences[89] = True

    for n in range(1, 81 * power + 1):
        seq = []
        while sequences[n] is None:
            seq.append(n)
            n = next_square_digit_chain(n)
        for k in seq:
            sequences[k] = sequences[n]

    return sum(
        permutations(digits)
        for digits in combinations_with_replacement(range(10), power)
        if sequences[sum(d * d for d in digits)]
    )


def next_square_digit_chain(n):
    m = 0
    while n > 0:
        d = n % 10
        m += d * d
        n //= 10
    return m


def permutations(digits):
    count = [0] * 10
    for d in digits:
        count[d] += 1
    return factorial(len(digits)) // prod(factorial(d) for d in count)
