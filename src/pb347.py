"""
Problem 347 of Project Euler.

https://projecteuler.net/problem=347
"""

from lib.primes import list_primes


def problem347(limit=10000000):
    primes = list_primes(limit // 2)
    solns = set()
    for i, p in enumerate(primes):
        if p * p > limit:
            break
        for q in primes[i + 1 :]:
            if p * q > limit:
                break
            M = []
            pp = p
            while pp * q < limit:
                qq = q
                while pp * qq * q < limit:
                    qq *= q
                M.append(pp * qq)
                pp *= p
            solns.add(max(M))
    return sum(solns)
