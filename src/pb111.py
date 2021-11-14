"""
Problem 111 of Project Euler.

https://projecteuler.net/problem=111
"""

from itertools import combinations_with_replacement, permutations

from lib.primes import is_prime

DIGITS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


def problem111(n=10):
    return sum(S(n, d) for d in DIGITS)


def S(n, d):
    cache = set()
    x = str(d) * n
    for M in range(n, -1, -1):
        for digits in combinations_with_replacement(DIGITS - {d}, n - M):
            for pos in permutations(range(n), n - M):
                y = x
                for m, i in zip(digits, pos):
                    y = y[:i] + str(m) + y[i + 1 :]
                if y[0] == "0":
                    continue
                y = int(y)
                if is_prime(y) and y not in cache:
                    cache.add(y)
        if cache:
            return sum(cache)
