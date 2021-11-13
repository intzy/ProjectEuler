"""
Problem 200 of Project Euler.

https://projecteuler.net/problem=200
"""

from math import isqrt

from lib.primes import is_prime, list_primes


def problem200():
    limit = 1000000
    while True:
        squbes = get_squbes(limit)
        squbes_200 = [n for n in squbes if "200" in str(n)]
        if len(squbes_200) >= 200:
            prime_proof_200_squbes = [n for n in squbes_200 if is_prime_proof(n)]
            if len(prime_proof_200_squbes) >= 200:
                return prime_proof_200_squbes[199]
        limit *= 10


def get_squbes(limit):
    primes = list_primes(isqrt(limit) // 8)

    squbes = []
    for i, p in enumerate(primes):
        ppp = p * p * p
        if ppp * p * p > limit:
            break
        for q in primes[i + 1 :]:
            n = ppp * q * q
            if n > limit:
                break
            squbes.append(n)
    for i, p in enumerate(primes):
        pp = p * p
        if pp * p * p * p > limit:
            break
        for q in primes[i + 1 :]:
            n = pp * q * q * q
            if n > limit:
                break
            squbes.append(n)

    squbes.sort()
    return squbes


def is_prime_proof(n):
    n = str(n)
    for i in range(0, len(n)):
        for d in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            m = n[:i] + d + n[i + 1 :]
            if is_prime(int(m)):
                return False
    return True
