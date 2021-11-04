"""
Problem 110 of Project Euler.

https://projecteuler.net/problem=110

See problem 108
"""

from math import ceil, log, prod

from lib.euler_lib import list_n_primes


def problem110(solns=4000000):
    primes = list_n_primes(ceil(log(solns) / log(3)))
    prime_factorizations = get_prime_factorizations(primes[-1] + 1, primes)
    alphas = [1 for _ in primes]

    flag = True
    while flag:
        flag = False
        for i, p, a in reversed(list(zip(range(len(primes)), primes, alphas))):
            if not a:
                continue
            for p_fact in prime_factorizations[2:p]:
                betas = [x + y for x, y in zip(alphas, p_fact)]
                betas[i] -= 1
                if any(x < y for x, y in zip(betas[:-1], betas[1:])):
                    continue
                if prod(2 * b + 1 for b in betas) < 2 * solns:
                    continue
                alphas = betas
                flag = True
                break

    return prod(p ** a for p, a in zip(primes, alphas))


def get_prime_factorizations(limit, primes):
    prime_factorizations = [[], [0 for _ in primes]]
    for n in range(2, limit):
        for i, p in enumerate(primes):
            if n % p:
                continue
            betas = prime_factorizations[n // p].copy()
            betas[i] += 1
            prime_factorizations.append(betas)
            break
    return prime_factorizations
