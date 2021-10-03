"""
Problem 061 of Project Euler.

https://projecteuler.net/problem=061
"""

from itertools import count


def problem061():
    """
    Uniqueness not proven.
    """
    triangulars = generate_sequence(lambda n: n * (n + 1) // 2)
    squares = generate_sequence(lambda n: n * n)
    pentagonals = generate_sequence(lambda n: n * (3 * n - 1) // 2)
    hexagonals = generate_sequence(lambda n: n * (2 * n - 1))
    heptagonals = generate_sequence(lambda n: n * (5 * n - 3) // 2)
    octogaonals = generate_sequence(lambda n: n * (3 * n - 2))

    figurate_nums = [squares, pentagonals, hexagonals, heptagonals, octogaonals]
    for p in triangulars:
        result = find_cycle([p], figurate_nums)
        if result is not None:
            return result
    return None


def find_cycle(cycle, figurate_nums):
    if len(cycle) == 6 and str(cycle[5])[2:4] == str(cycle[0])[0:2]:
        return sum(cycle)

    n = cycle[-1]
    for i, gonal_nums in enumerate(figurate_nums):
        for p in [x for x in gonal_nums if str(n)[2:4] == str(x)[0:2]]:
            result = find_cycle(cycle + [p], figurate_nums[:i] + figurate_nums[i + 1 :])
            if result:
                return result
    return None


def generate_sequence(f):
    a = []
    for n in count():
        x = f(n)
        if x < 1000:
            continue
        if x >= 10000:
            return a
        a.append(x)
    return None
