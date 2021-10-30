"""
Custom iterators for Project Euler.
"""

from itertools import chain, combinations

from lib.euler_lib import (
    cf_period,
    is_square,
    negative_pells_eqn_fundamental_soln,
    pells_eqn_fundamental_soln,
)


def pells_eqn_solns(D):
    """
    Iterates through all solutions (x, y) for the Diophontaine equation

        x^2 - Dy^2 = 1.
    """
    if is_square(D):
        return
    x0, y0 = pells_eqn_fundamental_soln(D)
    xk, yk = x0, y0
    while True:
        yield (xk, yk)
        xk, yk = x0 * xk + D * y0 * yk, x0 * yk + y0 * xk


def negative_pells_eqn_solns(D):
    """
    Iterates through all solutions (x, y) for the Diophontine equation

        x^2 - Dy^2 = -1.
    """
    if is_square(D):
        return
    if not cf_period(D) % 2:
        return
    x0, y0 = negative_pells_eqn_fundamental_soln(D)
    u, v = (x0 * x0 + D * y0 * y0), 2 * x0 * y0
    xk, yk = x0, y0
    while True:
        yield (xk, yk)
        xk, yk = xk * u + D * yk * v, xk * v + yk * u


def nonempty_subsets(itr):
    return chain.from_iterable(
        combinations(itr, r) for r in range(1, len(list(itr)) + 1)
    )


def set_partitions(iterable, k=None):
    """
    Modified from https://pypi.org/project/more-itertools/.
    """
    L = list(iterable)
    n = len(L)
    if k is not None:
        if k < 1:
            raise ValueError("Can't partition in a negative or zero number of groups")
        if k > n:
            return

    def set_partitions_helper(L, k):
        n = len(L)
        if k == 1:
            yield [tuple(L)]
        elif n == k:
            yield [tuple([s]) for s in L]
        else:
            e, *M = L
            for p in set_partitions_helper(M, k - 1):
                yield [tuple([e]), *p]
            for p in set_partitions_helper(M, k):
                for i in range(len(p)):
                    yield p[:i] + [tuple([e]) + p[i]] + p[i + 1 :]

    if k is None:
        for k in range(1, n + 1):
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)
