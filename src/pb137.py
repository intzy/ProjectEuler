"""
Problem 137 of Project Euler.

https://projecteuler.net/problem=137

Expading F_n as F_{n-1} + F_{n-2} in the summations,
we see that

    ∑F_n x^n = x / (1-x-x^2),

which must be an integer n.
Solving for x via the quadratic formula, we get discriminant

    (1 + n)^2 + (2n)^2,

which must be a perfect square k^2,
i.e., (1 + n, 2n, k^2) is a pythagorean triple,
and it must be primitive since 1 + n and 2n are relatively prime.

By Euclid's formula for pythagorean triples,
either

    1 + n = x^2 - y^2, n = xy,
or
    1 + n = 2xy, 2n = x^2 - y^2.

Iterating over integers y and solving for x and n
is fast enough for the 15'th golden nugget, but it won't scale well.
Further analysis can be used 
"""

from itertools import count
from math import isqrt

from lib.misc import is_square


def problem137(m=15):
    tally = 0
    for y in count(1):
        k = 5 * y * y + 4
        if is_square(k) and not (y + isqrt(k)) % 2:
            x = (y + isqrt(k)) // 2
            n = x * y
            tally += 1
            if tally == m:
                return n
        k = 5 * y * y - 2
        if is_square(k) and not (4 * y + isqrt(k)) % 2:
            x = (4 * y + isqrt(k)) % 2
            n = 2 * x * y - 1
            tally += 1
            if tally == m:
                return n
