"""
Problem 186 of Project Euler.

https://projecteuler.net/problem=186

A direct application of the disjoint-sets data structure.
"""

from itertools import count
from lib.datastructs import DisjointSets


def problem186(prime_minister=524287, ratio=0.99):
    size = 10 ** 6
    limit = ratio * size
    ds = DisjointSets(size)
    person = lagged_fib()
    calls = 0
    while ds.set_size(prime_minister) < limit:
        caller = next(person)
        callee = next(person)
        if caller != callee:
            ds.set_union(caller, callee)
            calls += 1
    return calls


def lagged_fib():
    size = 10 ** 6
    S = [0]
    for k in range(1, 56):
        S.append((100003 - 200003 * k + 300007 * k ** 3) % size)
        yield S[k]
    for _ in count(56):
        S.append((S[-24] + S[-55]) % size)
        yield S[-1]



