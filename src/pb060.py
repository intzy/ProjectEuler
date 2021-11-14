"""
Problem 060 of Project Euler.

https://projecteuler.net/problem=060
"""

from itertools import combinations
from math import inf

import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques

from lib.primes import is_prime, list_primes


def problem060(n=5):
    """
    We find the prime pair sets by finding the corresponding clique in a graph,
    where the primes are the vertices and pq is an edge if
    p concatenated with q and q concatenated with p are both primes.

    Our fast non-deterministic prime test uses Fermet's Theorem for base 2.
    We prove a potential prime set is infact a prime set
    by using a deterministic test.
    """
    prime_index = 0
    min_sum = inf
    G = nx.Graph()
    length_p = 10

    while True:
        primes = [3] + list_primes(length_p)[3:]
        for i, p in list(enumerate(primes))[prime_index:]:
            G.add_edges_from(get_prime_pairs(p, length_p, i, primes, min_sum))

        cliques = [clique for clique in enumerate_all_cliques(G) if len(clique) >= n]
        cliques.sort(key=sum)
        min_sum = next((sum(c) for c in cliques if is_prime_pair_set(c)), inf)
        prime_index = len(primes)
        length_p *= 10
        if min_sum < inf:
            break

    primes = [3] + list_primes(length_p)[3:]
    for i, p in list(enumerate(primes))[prime_index:]:
        if length_p < p:
            length_p *= 10
        G.add_edges_from(get_prime_pairs(p, length_p, i, primes, min_sum))
    cliques = [clique for clique in enumerate_all_cliques(G) if len(clique) >= n]
    cliques.sort(key=sum)
    return next(sum(clique) for clique in cliques if is_prime_pair_set(clique))


def is_probably_prime_pair(p, q, length_p, length_q):
    """
    Fermet's test for primes.
    Returns true if and only if p~q and q~p are pseudoprimes in base 2.
    """
    n1 = p * length_q + q
    n2 = q * length_p + p
    return not (pow(2, n1 - 1, n1) - 1 or pow(2, n2 - 1, n2) - 1)


def get_prime_pairs(p, length_p, i, primes, min_sum):
    prime_pairs = []
    length_q = 10
    for q in primes[:i]:
        if q > min_sum - p:
            break
        if length_q < q:
            length_q *= 10
        if is_probably_prime_pair(p, q, length_p, length_q):
            prime_pairs.append((p, q))
    return prime_pairs


def is_prime_pair_set(clique):
    return all(
        is_prime(int(str(p) + str(q))) and is_prime(int(str(q) + str(p)))
        for p, q in combinations(clique, 2)
    )
