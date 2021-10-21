"""
Problem 114 of Project Euler.

https://projecteuler.net/problem=114

Satisfies the recurrence relation f[m] = 1 + f[m - 1] + f[0] + ... + f[m - 4].
"""


def problem114(n=50):
    f = [None] * (n + 1)
    f[0] = 1
    f[1] = 1
    f[2] = 1
    f[3] = 2
    for m in range(4, n + 1):
        f[m] = 1 + f[m - 1] + sum(f[0 : m - 4 + 1])
    return f[n]
