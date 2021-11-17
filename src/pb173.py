"""
Problem 173 of Project Euler.

https://projecteuler.net/problem=173
"""


def problem173(limit=1000000):
    count = 0

    evens = list(range(8, limit + 1, 8))
    for i, x in enumerate(evens):
        num_tiles = x
        count += 1
        for y in evens[i + 1 :]:
            num_tiles += y
            if num_tiles > limit:
                break
            count += 1

    odds = list(range(12, limit + 1, 8))
    for i, x in enumerate(odds):
        num_tiles = x
        count += 1
        for y in odds[i + 1 :]:
            num_tiles += y
            if num_tiles > limit:
                break
            count += 1

    return count
