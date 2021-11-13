"""
Problem 187 of Project Euler.

https://projecteuler.net/problem=187

The number of composite numbers x < n of the form x = pq
is the number of combinations of primes {p, q} such that pq < n.
"""

from bisect import bisect_left

from lib.primes import list_primes


def problem187(n=10 ** 8):
    primes = list_primes(n // 2)

    count = 0
    j = len(primes)
    for i, prime in enumerate(primes):
        if i > j:
            break
        j = bisect_left(primes, n / prime, lo=i, hi=j)
        count += max(j - i, 0)

    return count
