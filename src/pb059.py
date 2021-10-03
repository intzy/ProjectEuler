"""
Problem 059 of Project Euler.

https://projecteuler.net/problem=059
"""

from itertools import product

from lib.euler_lib import file_to_matrix


def problem059(filename="txt/pb059.txt"):
    file = file_to_matrix(filename, ",")[0]
    best_key = max(
        ((a, b, c) for a, b, c in product(range(ord("a"), ord("z") + 1), repeat=3)),
        key=lambda key: english_score(decrypt(file, key)),
    )
    return sum(ord(c) for c in decrypt(file, best_key))


def decrypt(file, key):
    return "".join(chr(c ^ key[i % 3]) for i, c in enumerate(file))


def english_score(text):
    score = 0
    for c in text:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            score += 2
        elif ord(c) == ord(" "):
            score += 5
        elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
            score += 1
    for word in MOST_COMMON_ENGLISH_WORDS:
        score += 20 * text.count(word)
    return score


MOST_COMMON_ENGLISH_WORDS = [
    "the",
    "and",
    "that",
    "have",
    "for",
    "not",
    "with",
    "you",
    "this",
    "but",
]
