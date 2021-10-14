"""
Problem 136 of Project Euler.

https://projecteuler.net/problem=135

Exactly the same as 135.
Though further analysis can be done to significanlty reduce running time.
"""


def problem136(limit=50000000, num_solns=1):
    solns = [0] * limit
    for u in range(1, limit):
        for v in range(4 - (u % 4), min(3 * u, (limit - 1) // u + 1), 4):
            solns[u * v] += 1
    return solns.count(num_solns)
