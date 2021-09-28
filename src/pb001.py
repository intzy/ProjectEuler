"""
Problem 001 of Project Euler.

https://projecteuler.net/problem=001
"""

from math import lcm

from lib.euler_lib import sum_to_n


def problem001(m1=3, m2=5, limit=1000):
    """
    Recall that 1 + 2 + 3 +...+ n = n(n + 1)/2.
    """
    m3 = lcm(m1, m2)
    return (
        m1 * sum_to_n((limit - 1) // m1)
        + m2 * sum_to_n((limit - 1) // m2)
        - m3 * sum_to_n((limit - 1) // m3)
    )
