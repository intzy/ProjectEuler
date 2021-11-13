"""
Problem 146 of Project Euler.

https://projecteuler.net/problem=146
"""

from lib.primes import is_prime


def problem146(limit=150000000):
    """
    Modular arithmetic reduces to searching for n that are multiples of 10,
    that are not multiples of 3, and are congruent to 3 or 4 mod 7.
    Furthermore, along with test primality of each n * n + a for relevent a,
    we only need to test that n * n + 21 is not primes.
    """
    summation = 0
    gens = (range(start, limit, 210) for start in [10, 80, 130, 200])
    for gen in gens:
        for n in gen:
            nn = n * n
            if not fermets_test(nn):
                continue
            if not is_prime(nn + 21) and all(
                is_prime(nn + a) for a in [1, 3, 7, 9, 13, 27]
            ):
                summation += n
    return summation


def fermets_test(nn):
    return all(pow(2, nn + a - 1, nn + a) == 1 for a in [1, 3, 7, 9, 13, 27])
