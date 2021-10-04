"""
Project Euler Library

A collection of functions that are used in multiple project euler problems.
"""

from math import isqrt, log, log10


def digit_sum(n):
    """
    Returns the sum of the digits of the integer n.
    """
    summation = 0
    while n != 0:
        summation += n % 10
        n //= 10
    return summation


def int_len(n):
    """
    Returns the number of digits the positive integer n has.
    """
    if n > 999999999999997:
        return len(str(n))
    return int(log10(n)) + 1


def is_square(n):
    """
    Return True if and only if n is a perfect square.
    """
    return isqrt(n) ** 2 == n


def is_pentagonal(n):
    """
    Return True if and only if n is a pentagonal number,
    i.e., n = m(3m - 1)/2 for some integer m
    """
    m = 1 + 24 * n
    return is_square(m) and isqrt(m) % 6 == 5


def is_digit_permutation(n, m):
    """
    Return True if and only if n and m are, in base 10, permutations of the same digits.
    Does not consider leading zeros
    """
    return sorted(str(n)) == sorted(str(m))


def sum_to_n(n):
    """
    Takes an integer, outputs 1 + 2 + ... + (n-1) + n
    """
    return n * (n + 1) // 2


def is_palindrome(number):
    """
    Takes an integer, outputs True if and only if the integer is a palindrome number
    """
    return int(str(number)[::-1]) == number


def concat_ints(*args):
    """
    Takes one or more digits, concatenates their digits,
    and returns the resulting integer
    """
    n = ""
    for arg in args:
        n = f"{n}{arg}"
    return int(n)


def digit_factorial(number):
    digit_fact = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
    answer = 0
    while number > 0:
        digit, number = number % 10, number // 10
        answer += digit_fact[digit]
    return answer


def list_totients(limit):
    """
    Returns a list of phi(n), the Euler totient function, for 0 <= n < limit
    """
    totient = list(range(limit))
    for p in range(2, limit):
        if totient[p] == p:
            for n in range(p, limit, p):
                totient[n] -= totient[n] // p
    return totient


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


def is_prime(n):
    """
    Returns True if and only if n is a prime integer
    A deterministic version of the Miller-Rabin primality test.
    Assumes n < 2^64.
    """
    if not n % 2:
        return n == 2
    if n < 2047:
        witness = [2]
    elif n < 9080191:
        witness = [31, 73]
    elif n < 4759123141:
        witness = [2, 7, 61]
    elif n < 21652684502221:
        witness = [2, 1215, 34862, 574237825]
    elif n < 3825123056546413051:
        witness = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    else:  # assume n < 2^64
        witness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

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


def file_to_matrix(filename, separator):
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()
    array = []
    for string in strings:
        array.append(list(map(int, string.split(separator))))
    return array
