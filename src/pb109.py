"""
Problem 109 of Project Euler.

https://projecteuler.net/problem=109
"""

SINGLES = list(range(1, 21)) + [25]
DOUBLES = list(range(2, 41, 2)) + [50]
TRIPLES = list(range(3, 61, 3))
DART_REGIONS = SINGLES + DOUBLES + TRIPLES


def problem109(score=100):
    count = 0
    for n in DOUBLES:
        count += dart_combinations(score - n, 0, 2)
    return count


def dart_combinations(remaining_points, index, remaining_throws):
    if remaining_points <= 0:
        return 0
    if remaining_throws == 0:
        return 1
    return 1 + sum(
        dart_combinations(remaining_points - n, index + i, remaining_throws - 1)
        for i, n in enumerate(DART_REGIONS[index:])
    )
