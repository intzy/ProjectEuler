"""
Problem 143 of Project Euler.

https://projecteuler.net/problem=143
"""

from math import gcd, isqrt

import networkx as nx
from networkx.algorithms.clique import find_cliques


def problem143(limit=120000):
    triangles = []
    for u in range(2, isqrt(1 + limit)):
        for v in range(1, min(u, (limit - u * u) // (2 * u))):
            if gcd(u, v) - 1 or (u - v) % 3 == 0:
                continue
            a = u * u - v * v
            b = 2 * u * v + v * v
            for k in range(1, limit // (a + b) + 1):
                triangles.append((k * a, k * b))

    G = nx.Graph(triangles)
    return sum(
        set(
            sum(clique)
            for clique in find_cliques(G)
            if len(clique) == 3 and sum(clique) <= limit
        )
    )
