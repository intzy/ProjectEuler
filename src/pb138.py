"""
Problem 138 of Project Euler.

https://projecteuler.net/problem=138

Essentially, we are trying to find Pythagroean triples (b/2, h, L),
where h = b +- 1.
Since b, L, and h are integral, by the Pythagorean formula, b/2 must be an integer,
hence b must be even.  Therefore, h must be odd.
Therefore, by Euclud's formula,

    b = 4uv,    h = u^2 - v^2,      L = u^2 + v^2.

So,

    u^2 - v^2 = h = b +- 1 = 4uv +- 1,

i.e.,

    u^2 - 4uv - v^2 -+ 1 = 0.

Solving for u via the quadratic equation and noting that u > 0 gives

    u = 2v + sqrt(5v^2 +- 1).

Therefore, 5v^2 +- 1 is square, i.e.,

    k^2 - 5v^2 = +-1.

This is Pell's equation and negative Pell's equation, which we know how to solve for.
"""

from lib.euler_iterables import negative_pells_eqn_solns, pells_eqn_solns


def problem138(L=12):
    solns = []
    iter1 = pells_eqn_solns(5)
    iter2 = negative_pells_eqn_solns(5)
    for _ in range(L):
        k, v = next(iter1)
        u = 2 * v + k
        solns.append(u * u + v * v)
        k, v = next(iter2)
        u = 2 * v + k
        solns.append(u * u + v * v)
    return sum(sorted(solns)[:L])
