"""
Problem 101 of Project Euler.

https://projecteuler.net/problem=101

Lagrange interpolation.
"""

from math import prod


def problem101():
    first_incorrect_terms = []
    for degree in range(11):
        for n in range(1, 12):
            if u(n) != optimum_polynomial(degree, n):
                first_incorrect_terms.append(optimum_polynomial(degree, n))
                break
    return sum(first_incorrect_terms)


def u(n):
    return sum((-1 * n) ** k for k in range(11))


def optimum_polynomial(degree, n):
    def p(index, n):
        numerator = prod(n - k for k in range(1, degree + 2) if k != index)
        denominator = prod(index - k for k in range(1, degree + 2) if k != index)
        return numerator // denominator

    return sum(u(i) * p(i, n) for i in range(1, degree + 2))
