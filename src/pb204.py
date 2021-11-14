"""
Problem 204 of Project Euler.

https://projecteuler.net/problem=204
"""

from lib.primes import list_primes


def problem204(t=100, limit=10 ** 9):
    primes = list_primes(t + 1)

    def find_hamming_numbers(n, i):
        count = 0
        for j, p in enumerate(primes[i:]):
            if n * p > limit:
                break
            count += 1
            count += find_hamming_numbers(n * p, i + j)
        return count

    return 1 + find_hamming_numbers(1, 0)
