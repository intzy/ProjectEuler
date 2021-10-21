"""
Problem 106 of Project Euler.

https://projecteuler.net/problem=106

Hint: we only need to consider checks for equal-sized disjoint subset pairs,
eg) For n=6, the only disjoint subset pairs (A, B) we have to consider
are when |A|=|B|=1, |A|=|B|= 2, and |A|=|B|=3.
We can eliminate the case |A|=|B|=1 by the other assumption.
"""

from math import comb


def problem106(n=12):
    return sum(comb(n, m) * comb(m - 1, (m - 4) // 2) for m in range(4, n + 1, 2))
