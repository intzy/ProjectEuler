"""
Problem 077 of Project Euler.

https://projecteuler.net/problem=077
"""

from functools import cache
from itertools import count

from lib.euler_lib import list_primes


def problem077(threshold=5000):
    """
    Let f(n, i) be the number of ways you can add the first i prime numbers to make n.
    Then f(n, i) = f(n - p_i, i) + f(n, i - 1), where p_i is the i'th prime.
    """

    prime_limit = 10
    primes = list_primes(prime_limit)

    @cache
    def f(n, i):
        if i == -1:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 0
        p = primes[i]
        return f(n - p, i) + f(n, i - 1)

    i = 0
    for n in count(2):
        if n == primes[i]:
            i += 1
        if i == len(primes):
            prime_limit *= 10
            primes = list_primes(prime_limit)
        res = f(n, i - 1)
        if res > threshold:
            return n
    return None
