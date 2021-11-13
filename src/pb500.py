"""
Problem 500 of Project Euler.

https://projecteuler.net/problem=500
"""

import heapq
from functools import reduce

from lib.primes import list_n_primes


def problem500(exponent=500500, mod=500500507):
    """
    The smallest number that has 2^n divisors
    is the procuct of the n least numbers of the form p^k,
    where p is prime and k is a power of 2
    """
    primes = list_n_primes(exponent)
    heap = []

    # Since this heap package only supports min-heaps,
    # all numbers are multiplied by -1 when put into and taken out of the heap
    for p in primes:
        heapq.heappush(heap, -p)

    for p in primes:
        k = 2
        x = p ** k
        if x >= -heap[0]:
            break
        while x < -heap[0]:
            heapq.heappushpop(heap, -x)
            k *= 2
            x = p ** k

    return reduce(lambda a, b: a * b % mod, heap)
