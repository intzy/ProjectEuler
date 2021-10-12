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

where n = (a-7)/5 and m = b (hence, we require a = 2 (mod 5)).

There are ways to solve this generalized Pell's equation.
However, by seeing the first 12 or so golden nuggets,
one can see that there are two equivalence classes of them,
starting with [2, 21] and [5, 42], and the ratios
a_n / a_{n - 1} converge to the same value (approx 6.8...) for each of these sequences,
with the ratios decreasing monotonically.
Therefore, we can just estimate the next term in the sequence,
and search for the next golden nugget looking downwards.

Thus, the above code solves the problem, though it is not rigorous.
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
                n.append(m)
                break
    return sum(n)
