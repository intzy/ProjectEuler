"""
Number-theoretic algorithms.
"""

from functools import cache
from math import isqrt

from lib.euler_lib import list_totients, sum_to_n


class TotientSum:
    """
    A sub-linear algorithm to calculate Phi(n) = ∑ phi(n) from 1 to N,
    where phi is the euler-totient function.
    """

    def __init__(self, limit):
        self.sieve_limit = int(pow(limit, 2 / 3))
        self.totients = list_totients(self.sieve_limit)
        for i in range(2, len(self.totients)):
            self.totients[i] += self.totients[i - 1]

    @cache
    def Phi(self, n):
        if n < self.sieve_limit:
            return self.totients[n]
        Phi = self.Phi
        dmax = isqrt(n) if isqrt(n) == n // isqrt(n) else isqrt(n) + 1
        x = 0
        for d in range(2, isqrt(n) + 1):
            u = n // d
            x += Phi(u)
        for d in range(1, dmax):
            c = n // d - n // (d + 1)
            x += c * Phi(d)
        return sum_to_n(n) - x
