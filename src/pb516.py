"""
Problem 516 of Project Euler.

https://projecteuler.net/problem=516
"""

from lib.euler_lib import is_prime


def problem516(limit=10 ** 12, modulo=2 ** 32):
    hamming_numbers = get_hamming_numbers(limit)
    hamming_primes = list(sorted([n + 1 for n in hamming_numbers if is_prime(n + 1)]))
    hamming_primes = hamming_primes[3:]

    def get_hamming_totients(n, i):
        hamming_totients = [n]
        for j in range(i, len(hamming_primes)):
            x = n * hamming_primes[j]
            if x > limit:
                break
            hamming_totients += get_hamming_totients(x, j + 1)
        return hamming_totients

    hamming_totients = []
    for n in hamming_numbers:
        hamming_totients += get_hamming_totients(n, 0)
    return sum(hamming_totients) % modulo


def get_hamming_numbers(limit):
    hamming_numbers = []
    p2 = 1
    while p2 <= limit:
        p3 = 1
        while p3 * p2 <= limit:
            x = p2 * p3
            while x <= limit:
                hamming_numbers.append(x)
                x *= 5
            p3 *= 3
        p2 *= 2
    return hamming_numbers
