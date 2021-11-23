"""
Problem 214 of Project Euler.

https://projecteuler.net/problem=214
"""

from lib.euler_lib import list_totients
from lib.primes import list_primes


def problem214(limit=40000000):
    totients = list_totients(limit)
    primes = list_primes(limit)

    cycle_length = [None for _ in range(limit)]
    cycle_length[1] = 1
    for n in range(2, len(cycle_length)):
        cycle_length[n] = 1 + cycle_length[totients[n]]

    return sum(p for p in primes if cycle_length[p] == 25)
