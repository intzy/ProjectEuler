"""
Problem 035 of Project Euler.

https://projecteuler.net/problem=035
"""

from lib.euler_lib import concat_ints, list_primes


def problem035(limit=1_000_000):
    primes = set(list_primes(limit))
    circular_primes = set()
    for p in primes:
        p_rotate_primes = {p}
        for _ in range(len(str(p)) - 1):
            p = rotate(p)
            if p not in primes:
                break
            p_rotate_primes.add(p)
        else:
            circular_primes = circular_primes.union(p_rotate_primes)

    return len(circular_primes)


def rotate(n):
    return concat_ints(n % 10, n // 10)
