"""
Problem 188 of Project Euler.

https://projecteuler.net/problem=188
"""

from math import gcd


def problem188(a=1777, b=1888, digits=8):
    if gcd(a, 10) > 1:
        raise ValueError("b and 10 are not coprime")

    carmichaels = [10 ** digits]
    for _ in range(b - 1):
        carmichaels.append(carmichael(carmichaels[-1]))
        if carmichaels[-1] == 1:
            break

    ans = a
    for c in reversed(carmichaels):
        ans = pow(a, ans, c)

    return ans


def carmichael(n):
    """
    Assumes the only prime factors of n are 2 and 5.
    """
    i, j = 0, 0
    while not n % 2:
        i += 1
        n //= 2
    phi2 = pow(2, i - 2) if i > 1 else (2 if i == 1 else 0)
    while not n % 5:
        j += 1
        n //= 5
    phi5 = 4 * pow(5, j - 1) if j > 0 else 1
    return phi2 * phi5
