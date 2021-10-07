"""
Problem 098 of Project Euler.

https://projecteuler.net/problem=098
"""

from itertools import combinations
from math import isqrt


def problem098(filename="txt/pb098.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.readlines()[0].replace('"', "").split(",")
        words = [
            [word for word in words if len(word) == i]
            for i in reversed(range(1, len(max(words, key=len))))
        ]

    for row in words:
        squares = None
        square_anagrams = [
            largest_square_anagram(w1, w2, squares)
            for w1, w2 in combinations(row, 2)
            if largest_square_anagram(w1, w2, squares) is not None
        ]
        if len(square_anagrams) > 0:
            return max(square_anagrams)
    return None


def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)


def largest_square_anagram(w1, w2, squares):
    if not is_anagram(w1, w2):
        return None
    if squares is None:
        squares = {
            n * n
            for n in range(isqrt(10 ** (len(w1) - 1) - 1) + 1, isqrt(10 ** len(w1)))
        }

    for sq1 in squares:
        x = str(sq1)
        for d, l in zip(str(sq1), w1):
            x = x.replace(d, l)
        if x != w1:
            continue
        sq2 = w2
        for d, l in zip(str(sq1), w1):
            sq2 = sq2.replace(l, d)
        sq2 = int(sq2)
        if sq2 in squares:
            return max(sq1, sq2)
    return None
