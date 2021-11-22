"""
Primality and prime_counting functions.
"""

from bisect import bisect
from functools import cache
from math import isqrt, log

from sympy import integer_nthroot


def is_prime(n):
    """
    Returns True if and only if n is a prime integer
    A deterministic version of the Miller-Rabin primality test.
    Assumes n < 2^64.
    """

    def get_witness():
        if n < 2047:
            return [2]
        if n < 9080191:
            return [31, 73]
        if n < 4759123141:
            return [2, 7, 61]
        if n < 21652684502221:
            return [2, 1215, 34862, 574237825]
        if n < 3825123056546413051:
            return [2, 3, 5, 7, 11, 13, 17, 19, 23]
        # assume n < 2^64
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    if n <= 3:
        return n in [2, 3]
    if not n % 2:
        return n == 2

    witness = get_witness()
    t = 0
    u = n - 1
    while u % 2 == 0:
        t += 1
        u //= 2

    for a in witness:
        x = [pow(a, u, n)]
        for _ in range(1, t + 1):
            x.append(pow(x[-1], 2, n))
            if x[-1] == 1 and x[-2] != 1 and x[-2] != n - 1:
                return False
        if x[-1] != 1:
            return False
    return True


def list_n_primes(n):
    """
    Takes an integer n, returns a list of the first n primes numbers
    """
    if n < 6:
        primes = {
            1: [2],
            2: [2, 3],
            3: [2, 3, 5],
            4: [2, 3, 5, 7],
            5: [2, 3, 5, 7, 11],
        }
        return primes[n]

    # An upper bound for the nth prime number is n * (log(n) + log(log(n))))
    limit = int(n * (log(n) + log(log(n)))) + 1
    return list_primes(limit)[:n]


def list_primes(limit):
    """
    Takes a number limit, returns a sorted list of all primes less than limit
    """
    if limit < 2:
        return []
    primes = [2]

    # sieve indices i correspond to the number (i * 2) + 1
    sieve = [True] * int(limit // 2)
    sieve[0] = False

    for i in range(isqrt(limit) // 2 + 1):
        if sieve[i]:
            primes.append((i * 2) + 1)
            for j in range((i * 3) + 1, len(sieve), (i * 2) + 1):
                sieve[j] = False

    for i in range(isqrt(limit) // 2 + 1, len(sieve)):
        if sieve[i]:
            primes.append((i * 2) + 1)

    return primes


def list_primes_in_range(lower, upper):
    """
    Returns a list of all primes between lower and upper.
    """
    small_primes = list_primes(isqrt(upper))

    # sieve indices i correspond to the number lower + i
    sieve = [True] * (upper - lower)
    for p in small_primes:
        for i in range(p * ((lower - 1) // p + 1) - lower, upper - lower, p):
            sieve[i] = False

    primes = []
    for i, x in enumerate(sieve):
        if x:
            primes.append(i + lower)
    return primes


class Pi:
    def __init__(self, limit):
        self.primes = list_primes(isqrt(limit) + 10)
        self.pi_cache = {}
        self.phi_cache = {}

    def pi(self, n):
        if n in self.pi_cache:
            return self.pi_cache[n]
        primes = self.primes
        if n < len(primes):
            ans = bisect(primes, n)
            self.pi_cache[n] = ans
            return ans

        pi = self.pi
        phi = self.phi
        a = pi(isqrt(isqrt(n)))
        b = pi(isqrt(n))
        c = pi(integer_nthroot(n, 3)[0])

        ans = phi(n, a) + (b + a - 2) * (b - a + 1) // 2
        for i in range(a + 1, b + 1):
            w = n // primes[i - 1]
            b_i = pi(isqrt(w))
            ans -= pi(w)
            if i <= c:
                for j in range(i, b_i + 1):
                    ans += j - 1 - pi(w // primes[j - 1])
        self.pi_cache[n] = ans
        return ans

    @cache
    def phi(self, n, a):
        if a == 1:
            return (n + 1) // 2
        phi = self.phi
        primes = self.primes
        return phi(n, a - 1) - phi(n // primes[a - 1], a - 1)
