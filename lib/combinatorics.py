"""
Combinatoric functions for my solutions to Project Euler.
"""

from itertools import chain, combinations


def nonempty_subsets(itr):
    """
    An iterator that yields all nonempty subsets of "itr".
    """
    return chain.from_iterable(
        combinations(itr, r) for r in range(1, len(list(itr)) + 1)
    )


def set_partitions(iterable, k=None):
    """
    An iterator which yields all partitions of "iterable".

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
        for k in range(1, n + 1):  # pylint: disable=R1704
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)
