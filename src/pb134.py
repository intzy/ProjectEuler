"""
Problem 134 of Project Euler.

https://projecteuler.net/problem=134
"""

from itertools import count

from lib.misc import int_len
from lib.diophantine import bezouts
from lib.primes import is_prime, list_primes


def problem134(limit=1000000):
    primes = list_primes(limit)[2:]
    for n in count(limit + ((limit + 1) % 2), 2):
        if is_prime(n):
            primes.append(n)
            break

    S = []
    for p1, p2 in zip(primes[:-1], primes[1:]):
        n = 10 ** int_len(p1)
        a, _ = bezouts(n, p2, -p1)
        a += (p2 - a - 1) // p2 * p2
        S.append(a * n + p1)

    return sum(S)
