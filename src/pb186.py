"""
Problem 186 of Project Euler.

https://projecteuler.net/problem=186

A direct application of the disjoint-sets data structure.
"""

from itertools import count


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
    k = 1
    size = 10 ** 6
    S = [0]
    for k in range(1, 56):
        S.append((100003 - 200003 * k + 300007 * k ** 3) % size)
        yield S[k]
    for k in count(56):
        S.append((S[-24] + S[-55]) % size)
        yield S[-1]


class DisjointSets:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]

    def get_representative(self, n):
        if self.parent[n] == n:
            return n

        parent = self.get_representative(self.parent[n])
        self.parent[n] = parent
        return parent

    def set_union(self, n, m):
        n = self.get_representative(n)
        m = self.get_representative(m)
        if n == m:
            return
        if self.size[n] < self.size[m]:
            n, m = m, n
        self.parent[m] = n
        self.size[n] += self.size[m]

    def set_size(self, n):
        rep = self.get_representative(n)
        return self.size[rep]
