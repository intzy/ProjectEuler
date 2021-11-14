"""
Problem 122 of Project Euler.

https://projecteuler.net/problem=122

These are known as addition chains.
"""

from itertools import combinations_with_replacement


def problem122(limit=200):
    m = {1: 0}
    encountered_previously = [set() for _ in range(limit + 1)]
    chains = [[(1,)]]
    num_mults = 0
    while len(m) < limit:
        num_mults += 1
        chains.append([])
        for chain in chains[num_mults - 1]:
            for c1, c2 in combinations_with_replacement(chain, 2):
                k = c1 + c2
                if (
                    k in chain
                    or k < chain[-1]
                    or k > limit
                    or all(d in encountered_previously[k] for d in chain)
                ):
                    continue
                chains[num_mults].append(chain + (k,))
                encountered_previously[k].update(chain)
                if k not in m:
                    m[k] = num_mults
    return sum(m.values())
