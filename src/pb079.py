"""
Problem 079 of Project Euler.

https://projecteuler.net/problem=079

Topological sorting.
"""


def problem079(filename="txt/pb079.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        strings = [string.replace("\n", "") for string in f.readlines()]

    before = {str(x): set() for x in range(10)}
    for x in strings:
        before[x[1]].add(x[0])
        before[x[2]].add(x[1])

    for d in range(10):
        if not before[str(d)] and all(str(d) not in before[x] for x in before):
            before.pop(str(d))

    ans = ""
    for _ in range(len(before)):
        d = sorted(before.keys(), key=lambda d: len(before[d]))[0]
        for x in before:
            before[x].discard(d)
        before.pop(d)
        ans += d
    return ans
