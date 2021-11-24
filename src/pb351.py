"""
Problem 351 of Project Euler.

https://projecteuler.net/problem=351

The solution is

    6 * ∑ (n - phi(n)) from 1 to N,

where phi is the euler-totient function.
"""

from lib.euler_lib import sum_to_n
from lib.number_theory import TotientSum


def problem351(N=10 ** 8):
    Phi = TotientSum(N).Phi
    return 6 * (sum_to_n(N) - Phi(N))
