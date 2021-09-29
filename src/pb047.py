"""
Problem 047 of Project Euler.

https://projecteuler.net/problem=047
"""


from itertools import count

from lib.euler_lib import list_primes


def problem047(consecutive=4):
    prime_limit = 256
    prime_divisors = [{}, {}, {2}, {3}, {2}, {5}, {2, 3}, {7}]
    primes = list_primes(prime_limit)
    consec_count = 0
    prime_index = 4

    for n in count(8):

        # resize our list of primes if necessary
        if prime_index == len(primes):
            prime_limit *= 2
            primes = list_primes(prime_limit)

        # if n is prime, mark it as prime
        if n == primes[prime_index]:
            prime_index += 1
            prime_divisors.append({n})
            consec_count = 0
            continue

        # find all prime divisors of n using dp
        for p in primes:
            if n % p == 0:
                prime_divisors.append({p}.union(prime_divisors[n // p]))
                break

        # If has "consecutive" distinct prime divisors,
        # increment count and return function if the count == consecutive
        if len(prime_divisors[-1]) == consecutive:
            consec_count += 1
            if consec_count == consecutive:
                return n - consecutive + 1

        # Else reset the count
        else:
            consec_count = 0
