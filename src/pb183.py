"""
Problem 183 of Project Euler.

https://projecteuler.net/problem=183

The function max_k (x/k)^k is strictly increasing in x.
Take the log of both sides and find the max k by continually incrementing k.

A simplified fraction p / q has a terminating decimal expansion
if and only if the only prime factors of q are 2 and 5.
"""

from math import gcd, log


def problem183(L=10000):
    D = [0] * (L + 1)
    kmax = 1
    for N in range(5, L + 1):
        while kmax * log(N / kmax) < (kmax + 1) * log(N / (kmax + 1)):
            kmax += 1
        D[N] = -N if is_terminating((N, kmax)) else N
    return sum(D)


def is_terminating(frac):
    p, q = frac
    g = gcd(p, q)
    q //= g

    while q % 2 == 0:
        q //= 2
    while q % 5 == 0:
        q //= 5
    return q == 1
