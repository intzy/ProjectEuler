"""
Problem 086 of Project Euler.

https://projecteuler.net/problem=086
"""

from heapq import heappop, heappush
from itertools import count
from math import gcd


def problem086(integer_cuboids=1000000):
    heap = []
    cuboid_count = [0, 0, 0]
    for M in count(2):
        cuboid_count += [0, 0]
        cuboid_count[M] += cuboid_count[M - 1]

        x = M
        for y in range(1 + (x % 2), x, 2):
            if gcd(x, y) - 1:
                continue
            a, b = tuple(sorted([x * x - y * y, 2 * x * y]))
            heappush(heap, PythagoreanTriple(a, b))

        while heap[0].M == M:
            pt = heappop(heap)
            c = pt.num_cuboids()
            cuboid_count[M] += c[0]
            cuboid_count[pt.b] += c[1]
            pt.next_k()
            heappush(heap, pt)
        if cuboid_count[x] > integer_cuboids:
            return x


class PythagoreanTriple:
    def __init__(self, a, b):
        self.init_a = a
        self.init_b = b
        self.a = a
        self.b = b
        self.M = max(a, (b + 1) // 2)
        self.k = 1

    def __lt__(self, other):
        return self.M < other.M

    def next_k(self):
        self.k += 1
        self.a = self.k * self.init_a
        self.b = self.k * self.init_b
        self.M = max(self.a, (self.b + 1) // 2)

    def num_cuboids(self):
        return (max(0, self.b // 2 - self.b + self.a + 1), self.a // 2)
