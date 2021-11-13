"""
Primality and prime_counting functions.
"""

from math import isqrt, log


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
