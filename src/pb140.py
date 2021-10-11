"""
Problem 140 of Project Euler.

https://projecteuler.net/problem=140

By using the recurrence G_k = G_{k - 1} + G_{k - 2} inside the summations,
one can prove that

    ∑ G_n x^n = (x + 3x^2)/(1 - x - x^2),

and we want this to be an integer n.
Solving for x via the quadratic formula, we have discriminant

    (n+1)^2 + 4(3+n)n = 5n^2 + 14n + 1 = 5(n + 7/5)^2 - 44/5,

and we need this to be a perfect square m^2.
Therefore, we need to solve the generalized Pell's equation

    (5n + 7)^2 - 5m^2 = 44 = a^2 - 5b^2,

where n = (a-7)/5 and m = b.
"""

from itertools import count

from lib.euler_lib import is_square


def problem140():
    n = [2, 21]
    for _ in range(2, 15):
        n0 = int(n[-1] * (n[-1] / n[-2]))
        for d in count():
            m = n0 - d
            x = 5 * m * m + 14 * m + 1
            if is_square(x):
                print(d)
                n.append(m)
                break
    n.append(5)
    n.append(42)
    for _ in range(2, 15):
        n0 = int(n[-1] * (n[-1] / n[-2]))
        for d in count():
            m = n0 - d
            x = 5 * m * m + 14 * m + 1
            if is_square(x):
                print(d)
                n.append(m)
                break
    return sum(n)
