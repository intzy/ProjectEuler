"""
Problem 073 of Project Euler.

https://projecteuler.net/problem=073
"""

from lib.euler_lib import bezouts


def problem073(p1=1, q1=3, p2=1, q2=2, N=12000):
    count = 0
    (c, d) = bezouts(q1, p1, 1)
    d *= -1
    r = (N - d) // q1
    a = p1
    b = q1
    c += r * p1
    d += r * q1

    while (c, d) != (p2, q2):
        count += 1
        k = (N + b) // d
        e = k * c - a
        f = k * d - b
        a = c
        b = d
        c = e
        d = f
    return count
