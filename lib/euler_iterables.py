"""
Custom iterators for Project Euler.
"""

from itertools import chain, combinations, count


def nonempty_subsets(itr):
    return chain.from_iterable(
        combinations(itr, r) for r in range(1, len(list(itr)) + 1)
    )


def positive_integers():
    return count(1)


def nonnegative_integers():
    return count()


def positive_even_integers():
    return count(2, 2)
