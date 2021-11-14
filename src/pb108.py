"""
Problem 108 of Project Euler.

https://projecteuler.net/problem=108

We are trying to find positive integer solutions to

    1/x + 1/y = 1/n.

Clearly x, y > n, so there are a, b such that x = a + n, y = b + n.
Subsitution these into the above equation and simplfying yields

    ab = n^2.

Therefore, it suffices to find the number of distinct factorizations a * b of n^2.

If n = p_1^(alpha_1) * p_2^(alpha_2) * ... * p_k^(alpha_k),
then the number of distinct factorizations of n is

    (alpha_1 + 1) * (alpha_2 + 1) * ... * (alpha_k + 1).

Therefore, since n^2 = p_1^(2 * alpha_1) * p_2^(2 * alpha_2) * ... * p_k^(2 * alpha_k),
the number of distinct factorizations of n^2 is

    (2 * alpha_1 + 1) * (2 * alpha_2 + 1) * ... * (2 * alpha_k + 1).

Finally, since n^2 is square, the number of distinct factorizations a * b of n^2
is (num_divisors(n^2) + 1) // 2.

Instead of finding the minimum n such that

    (num_divisors(n^2) + 1) // 2 >= 2 * 1000,

we can find n directly by looking at the alphas.
"""

from math import ceil, log, prod

from lib.primes import list_n_primes


def problem108(solns=1000):
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
