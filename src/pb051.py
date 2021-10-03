"""
Problem 051 of Project Euler.

https://projecteuler.net/problem=051
"""

from itertools import count

from lib.euler_iterables import nonempty_subsets
from lib.euler_lib import list_primes


def problem051(family_size=8):
    length = 0
    for d in count(1):
        primes = list_primes(10 ** d)
        d_decimal_primes = primes[length:]
        primes = set(d_decimal_primes)
        length = len(primes)
        for p in d_decimal_primes:
            if in_prime_family(p, primes, family_size):
                return p


def in_prime_family(p, primes, family_size):
    # For each digit d (in {0, 1} for family_size=8),
    # for each nonempty subset of the positions of d in p,
    # see if replacing those digits d with larger digits forms a family of primes.
    digit_distibution_of_p = digit_distribution(p)[: 10 - family_size]
    for d, d_pos in enumerate(digit_distibution_of_p):
        for pos in nonempty_subsets(d_pos):
            q = p
            prime_count = 1
            for j in range(d + 1, 10):
                if family_size > prime_count + 10 - j:
                    break
                for k in pos:
                    q += 10 ** k
                if q in primes:
                    prime_count += 1
            if prime_count == family_size:
                return True
    return False


def digit_distribution(n):
    histogram = [[] for _ in range(10)]
    for i in count():
        d, n = n % 10, n // 10
        histogram[d].append(i)
        if n == 0:
            break
    return histogram
