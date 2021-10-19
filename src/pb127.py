"""
Problem 127 of Project Euler.

https://projecteuler.net/problem=127

A few things to note.

Since gcd(a, b) = gcd(b, c) = gcd(a, c),
we have rad(abc) = rad(a) * rad(b) * rad(c)
Therefore, we can precompute rad with a sieve.

Next, since a + b = c, gcd(a, b) = 1 implies gcd(a, c) = gcd(b, c) = 1.

Finally, we significantly improve the running time if for each c,
we iterate though the a's, sorted by rad(a), and continue to next c when
2 * rad(a) * rad(c) >= c.
"""

from math import gcd

from lib.euler_lib import list_primes


def problem127(limit=120000):
    abc_hits = []

    primes = list_primes(limit)
    rad = [1] * (limit + 1)
    for p in primes:
        for n in range(p, limit + 1, p):
            rad[n] *= p
    E = sorted(list(range(1, limit)), key=lambda n: rad[n])

    for c in range(3, limit):
        for a in E:
            if 2 * rad[a] * rad[c] >= c:
                break
            b = c - a
            if gcd(a, b) == 1 and a < b and rad[a] * rad[b] * rad[c] < c:
                abc_hits.append((a, b, c))
    return sum(abc[2] for abc in abc_hits)
