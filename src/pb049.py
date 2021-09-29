"""
Problem 049 of Project Euler.

https://projecteuler.net/problem=049
"""


from itertools import combinations

from lib.euler_lib import concat_ints, is_digit_permutation, list_primes


def problem049():
    primes = list(filter(lambda x: x > 999, list_primes(10_000)))
    primes.remove(1487)
    for p, q in combinations(primes, 2):
        if is_digit_permutation(p, q):
            r = q + (q - p)
            if r in primes and is_digit_permutation(p, r):
                return concat_ints(p, q, r)
    return None
