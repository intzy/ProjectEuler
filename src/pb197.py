"""
Problem 197 of Project Euler.

https://projecteuler.net/problem=197

Approximently,

    f(x) = 1.42 * 2^(-x^2).

The function f(x) - x has one zero x0, but is is an unstable solution
since |f'(x0)| > 1.

On the otherhand, f(f(x)) - x has two additional different zeros x1 and x2,
and both of them are stable solutions.
In fact, u_n alternates between x1 and x2 as n becomes large.
Therefore, it suffices to figure when we are in this 2-cycle.
"""

from math import floor


def problem197(n=10 ** 12):
    u = [-1]
    u.append(f(u[0]))
    for _ in range(2, n + 2):
        u.append(f(u[-1]))
        if u[-1] == u[-3]:
            return round(u[-1] + u[-2], 9)
    return round(u[-1] + u[-2], 9)


def f(x):
    return floor(pow(2, 30.403243784 - x * x)) * pow(10, -9)
