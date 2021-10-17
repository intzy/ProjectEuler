"""
Problem 071 of Project Euler.

https://projecteuler.net/problem=071
"""

from lib.euler_lib import bezouts


def problem071(h=3, k=7, n=1000000):
    (x, y) = bezouts(k, h, -1)
    r = (n + y) // k
    return x + r * h
