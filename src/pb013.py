"""
Problem 013 of Project Euler.

https://projecteuler.net/problem=013
"""


def problem013(num_digits=10, filename="txt/pb013.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()

    return int(str(sum(int(string) for string in strings))[:num_digits])
