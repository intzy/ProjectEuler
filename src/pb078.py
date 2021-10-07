"""
Problem 078 of Project Euler.

https://projecteuler.net/problem=078
"""

from itertools import count


def problem078(divisible=1000000):
    k = 1
    pentagonals = [1, 2]
    p = [1]
    for n in count(1):
        if pentagonals[-1] <= n:
            k += 1
            pentagonals.append(k * (3 * k - 1) // 2)
            pentagonals.append(-k * (3 * -k - 1) // 2)

        u = 0
        t = 0
        while pentagonals[t] <= n:
            u += p[-pentagonals[t]] if t % 4 in {0, 1} else -p[-pentagonals[t]]
            t += 1
        p.append(u % divisible)
        if not p[n]:
            return n
