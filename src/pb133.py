"""
Problem 133 of Project Euler.

https://projecteuler.net/problem=133
"""

from lib.primes import list_primes


def problem133(limit=100000):
    primes = list_primes(limit)[3:]
    non_factors = [2, 3, 5]
    for p in primes:
        k = p - 1
        gcd = 1
        while not k % 2:
            k //= 2
            gcd *= 2
        while not k % 5:
            k //= 5
            gcd *= 5
        if pow(10, gcd, p) - 1:
            non_factors.append(p)
    return sum(non_factors)
