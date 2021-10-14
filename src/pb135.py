"""
Problem 135 of Project Euler.

https://projecteuler.net/problem=135

Since x, y, z is an arthmetic progression of positive integers, we have

    x^2 - (x - k)^2 - (x - 2k)^2 = (5k - x)(x - k) = n.

Therefore, we are looking for uv = n so that

    x = (5u + v)/4,     k = (u + v)/4,    3u > v,

the inequaliy needed since (x - 2k) > 0.
"""


def problem135(limit=1000000, num_solns=10):
    solns = [0] * limit
    for u in range(1, limit):
        for v in range(4 - (u % 4), min(3 * u, (limit - 1) // u + 1), 4):
            solns[u * v] += 1
    return solns.count(num_solns)
