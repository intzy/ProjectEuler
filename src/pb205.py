"""
Problem 205 of Project Euler

https://projecteuler.net/problem=205

By the total law of probability,

    P(pyramidal > cubic)
        = ∑ P(pyramidal > cubic | pyramidal = i) * P(pyramidal = i).
"""

from itertools import product


def problem205():
    cubic = [0] * 37
    for cmb in product(range(1, 7), repeat=6):
        cubic[sum(cmb)] += 1

    pyramidal = [0] * 37
    for cmb in product(range(1, 5), repeat=9):
        pyramidal[sum(cmb)] += 1

    prob = 0
    for i in range(1, 37):
        prob += (sum(cubic[:i]) / sum(cubic)) * (pyramidal[i] / sum(pyramidal))
    return round(prob, 7)
