"""
Number-theoretic algorithms.
"""

from functools import cache
from math import isqrt

from lib.misc import sum_to_n


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


def list_totients(limit):
    """
    Returns a list of phi(n), the Euler totient function, for 0 <= n < limit.
    """
    phi = [0 for _ in range(limit)]
    phi[1] = 1
    for n in range(2, limit):
        if phi[n] != 0:
            continue
        phi[n] = n - 1
        for k in range(2, (limit - 1) // n + 1):
            if phi[k] == 0:
                continue
            q = k
            f = n - 1
            while not q % n:
                f *= n
                q //= n
            # phi(k * n) = n^r * (n - 1) * phi(k // n^r),
            # where r is the exponent of n in the prime factorization of k.
            phi[k * n] = f * phi[q]
    return phi


def list_sum_proper_divisors(limit):
    """
    Returns a list d,
    where d[n] is the sum of the proper divisors of d.
    """
    d = [1] * limit
    for i in range(2, limit // 2):
        for n in range(2 * i, limit, i):
            d[n] += i
    return d