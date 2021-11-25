"""
Problem 764 of Project Euler.

https://projecteuler.net/problem=764

By recognizing that (4x, y^2, z) form a pythagorean triple,
one can generate solutions to the diophontaine equation
based on consider cases

    4x = 4(m^2 - n^2),  y^2 = 8mn,  z = m^2 + n^2,

    4x = 2mn,   y^2 = m^2 - n^2,    z = m^2 + n^2,

where m > n are coprime and both not odd.
"""

from math import gcd, isqrt, sqrt


def problem764(limit=10 ** 16, modulo=10 ** 9):
    ans = 0

    for a in range(1, isqrt(isqrt(limit)) // 2 + 1):
        aaaa = pow(a, 4)
        for b in range(
            1, min(int(sqrt(2) * a), isqrt(isqrt((limit - 16 * aaaa) // 4))) + 1, 2
        ):
            if gcd(a, b) != 1:
                continue
            bbbb = pow(b, 4)
            ans += 20 * aaaa + 3 * bbbb + 4 * a * b

    for a in range(1, isqrt(isqrt(limit // 4)) + 1, 2):
        aaaa = pow(a, 4)
        for b in range(
            1, min(int(a / sqrt(2)), isqrt(isqrt((limit - 4 * aaaa))) // 2) + 1
        ):
            if gcd(a, b) != 1:
                continue
            bbbb = pow(b, 4)
            ans += 5 * aaaa + 12 * bbbb + 4 * a * b

    for u in range(2, isqrt(isqrt(limit)) + 1):
        uu = u * u
        uuuu = uu * uu
        for v in range(
            1 + (u % 2), min(u, isqrt(isqrt(8 * uuuu + limit) - 3 * u * u) + 1), 2
        ):
            if gcd(u, v) != 1:
                continue
            vv = v * v
            vvvv = vv * vv
            ans += uuuu + vvvv + 6 * uu * vv + uu - vv + uu * u * v + u * v * vv

    return ans % modulo
