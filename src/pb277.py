"""
Problem 277 of Project Euler.

https://projecteuler.net/problem=277

Let a = a_1.  We can represent each a_n as

    a_n = (qa + r) / m,

where m = 3^{m - 1}, and q and r are determined by the sequence "UDDDUd....".
Therefore,

    qa + r == 0 mod m,

or

    a == -rq^{-1} mod m,

where q^{-1} is the multiplicative inverse of q in the group Z*_m.
Note that q is in Z^*_m since q is a power of 2, m is a power of 3,
hence q and m are relatively prime.
It then suffices to find the least a > 10^15 with residue -rq^{-1} mod m.
"""

from math import ceil

from lib.euler_lib import bezouts


def problem277(lower_bound=10 ** 15, seq="UDDDUdddDDUDDddDdDddDDUDDdUUDd"):
    q = 1
    r = 0
    m = 1
    for c in seq:
        if c == "U":
            q *= 4
            r = 4 * r + 2 * m
        if c == "d":
            q *= 2
            r = 2 * r - m
        m *= 3

    _, qinv = bezouts(m, q, 1)
    residue = (-r * qinv) % m
    k = ceil((lower_bound - residue + 1) / m)
    return residue + k * m
