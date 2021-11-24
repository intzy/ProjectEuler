"""
Problem 072 of Project Euler.

https://projecteuler.net/problem=072

A fraction m/n is in the Faray series of
order d if and only if 2 <= n <= d, m < n, and gcd(m, n) = 1.
In otherwords, the fraction m/n is in the Faray series
if and only if m < n <= d and m is relatively prime to n.
Thus the number of fractions with denonminator
n is phi(n), where phi is Euler's totient function.
Summing up all phis from 2 to d gives the desired result.
"""

from lib.number_theory import list_totients


def problem072(d=1000000):
    return sum(list_totients(d + 1)[2:])
