"""
Problem 093 of Project Euler.

https://projecteuler.net/problem=093
"""

from itertools import combinations, count, permutations, product
from math import inf

from lib.misc import concat_ints


def problem093():
    """
    Simply test each combination of 4 digits from 1 to 9,
    and with each combination, test with all possible operations.

    To get around non-communitivity of subtraction and division,
    I create two additional operations, revsub and revdiv.
    """
    x = max(
        ((a, b, c, d) for a, b, c, d in combinations(range(1, 10), r=4)),
        key=lambda x: get_sequence(*x),
    )
    return concat_ints(*x)


def get_sequence(a, b, c, d):
    answers = set()
    for x1, x2, x3, x4 in permutations([a, b, c, d]):
        for op1, op2, op3 in product([add, sub, revsub, mult, div, revdiv], repeat=3):
            ans = op1(x1, op2(x2, op3(x3, x4)))
            if float(ans).is_integer() and int(ans) > 0:
                answers.add(int(ans))
    for n in count(1):
        if n not in answers:
            return n - 1


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def revsub(x, y):
    return y - x


def mult(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return inf
    return x / y


def revdiv(x, y):
    if x == 0:
        return inf
    return y / x
