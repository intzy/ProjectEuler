"""
Problem 066 of Project Euler.

https://projecteuler.net/problem=066
"""

from math import isqrt

from lib.euler_lib import is_square


def problem066(limit=1000):
    return max((D for D in range(2, limit + 1)), key=get_minimal_x)


def get_minimal_x(D):
    if is_square(D):
        return 0
    return solve_pells_equation(D)[0]


def solve_pells_equation(D):
    """
    Find fundamental solution (x, y) to x^2 - Dy^2 = 1.
    """
    s = isqrt(D)
    t = 1
    p = [1, s]
    q = [0, 1]
    x = s
    y = 1
    while x * x - D * y * y != 1:
        t = (D - s * s) // t
        a = (isqrt(D) + s) // t
        s = t * a - s
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
        x = p[-1]
        y = q[-1]
    return (x, y)
