"""
Problem 118 of Project Euler.

https://projecteuler.net/problem=118
"""

from math import prod

from lib.euler_iterables import set_partitions
from lib.euler_lib import list_primes


def problem118():
    """
    Partition primes into equivalence classes based on the digits they contain,
    and store how many primes have those digits.
    Then go though each partition of the digits 1-9 to get the number of prime sets.
    Note that a 1-9 pandigital number is not prime.
    """
    pandigital_primes = get_pandigital_primes(100000000)
    return sum(
        prod(pandigital_primes[p] for p in partition)
        for k in range(2, 7)
        for partition in set_partitions([1, 2, 3, 4, 5, 6, 7, 8, 9], k)
        if all(p in pandigital_primes for p in partition)
    )


def get_pandigital_primes(limit):
    primes = list_primes(limit)
    pandigital_primes = {}
    for p in primes:
        pstr = str(p)
        pid = tuple(sorted(set(int(d) for d in pstr)))
        if len(pstr) == len(pid) and pid[0] != 0:
            if pid in pandigital_primes:
                pandigital_primes[pid] += 1
            else:
                pandigital_primes[pid] = 1
    return pandigital_primes
