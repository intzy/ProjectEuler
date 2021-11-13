"""
Problem 123 of Project Euler.

https://projecteuler.net/problem=123

If n is even, then

    (p_n - 1)^n + (p_n + 1)^n = (-np_n + 1) + (np_n + 1) = 2 (mod (p_n)^2).

If n is odd, then

    (p_n - 1)^n + (p_n + 1)^n = (np_n - 1) + (np_n + 1) = 2np_n (mod (p_n)^2).

Clearly it suffices to check only odd p_n.
"""

from itertools import count

from lib.primes import list_n_primes


def problem123(limit=10 ** 10):
    prime_index_limit = 100
    primes = list_n_primes(prime_index_limit)
    for n in count(1, 2):
        if n > prime_index_limit:
            prime_index_limit *= 10
            primes = list_n_primes(prime_index_limit)
        pn = primes[n - 1]
        if (2 * n * pn) % (pn * pn) > limit:
            return n
