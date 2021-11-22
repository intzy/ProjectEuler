"""
Problem 387 of Project Euler.

https://projecteuler.net/problem=387
"""

from lib.primes import is_prime

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def problem387(num_digits=14):
    right_truncatable_harshads = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    strong_rt_harshads = []
    for i in range(1, num_digits - 1):
        new_harshads = []
        for n in right_truncatable_harshads[i - 1]:
            for d in DIGITS:
                x = 10 * n + d
                if is_harshad(x):
                    new_harshads.append(x)
                    if is_strong_harshad(x):
                        strong_rt_harshads.append(x)
        right_truncatable_harshads.append(new_harshads)

    harshad_primes = []
    for n in strong_rt_harshads:
        for d in DIGITS:
            p = 10 * n + d
            if is_prime(p):
                harshad_primes.append(p)

    return sum(harshad_primes)


def is_harshad(n):
    return n % digit_sum(n) == 0


def is_strong_harshad(n):
    ds = digit_sum(n)
    if n % ds:
        return False
    return is_prime(n // ds)


def digit_sum(n):
    ds = 0
    while n != 0:
        n, s = divmod(n, 10)
        ds += s
    return ds
