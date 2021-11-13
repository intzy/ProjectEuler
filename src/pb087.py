"""
Problem 087 of Project Euler.

https://projecteuler.net/problem=087
"""


from itertools import product
from math import isqrt

from lib.primes import list_primes


def problem087(limit=50_000_000):
    numbers = set()
    primes = list_primes(isqrt(limit))
    prime_squares = [pow(p, 2) for p in primes if pow(p, 2) < limit]
    prime_cubes = [pow(p, 3) for p in primes if pow(p, 3) < limit]
    prime_fourths = [pow(p, 4) for p in primes if pow(p, 4) < limit]
    for p, q, r in product(prime_squares, prime_cubes, prime_fourths):
        if p + q + r < limit:
            numbers.add(p + q + r)
    return len(numbers)
