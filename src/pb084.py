"""
Problem 084 of Project Euler.

https://projecteuler.net/problem=084

I find the stationary distributioin of a Markov Chain
that is a good approximation of the Monopoly Board.

The two assumptions that I have to make that are not true are that
- the chance of getting triple doubles is equal on every square
  (which is not true since if you go to jail for rolling three doubles
  in a row, you won't go back to jail for rolling a fourth double), and
- the deck of cards is reshuffled after each a card is picked up.

I need to make these assumptions since Markov Chains are past-independent.

The first assumption can be removed by making a much bigger Markov chain,
where the states are the direct product of the board position and
how many doubles you have rolled.

The second assumptioin can't be removed, and there are too many deck orders
to feasibly test each possible deck.
However, I doubt that it would make much if any difference assuming that
the cards are resuffled vs. taking the average of all possible deck permutations.
"""

from itertools import product

import numpy as np

GO = 0
JAIL = 10
G2J = 30
COMMUNITY_CHEST = [2, 17, 33]
CHANCE = [7, 22, 36]
C1 = 11
E3 = 24
H2 = 35
R1 = 5
R2 = 15
R3 = 25
R4 = 35
U1 = 12
U2 = 28


def problem084():
    P = build_transition_martix()
    pi = get_stationary_distribution(P)
    return int("".join(str(x[1]) for x in sorted(zip(pi, range(40)), reverse=True)[:3]))


def build_transition_martix():
    dice_sum = [0] * 9
    for d1, d2 in product(range(1, 5), repeat=2):
        dice_sum[d1 + d2] += 1
    dice_sum = [d / sum(dice_sum) for d in dice_sum]
    triple_doubles = (dice_sum[2] + dice_sum[8]) / 16 + (dice_sum[4] + dice_sum[6]) / 48
    dice_sum[2] *= 15 / 16
    dice_sum[8] *= 15 / 16
    dice_sum[4] *= 47 / 48
    dice_sum[6] *= 47 / 48

    P = [[0] * 40 for _ in range(40)]
    for i in range(40):
        for j, d in enumerate(dice_sum):
            if (i + j) == G2J:
                P[i][JAIL] += d
            else:
                P[i][(i + j) % 40] += d
        P[i][JAIL] += triple_doubles

    # Community Chest
    for i in range(40):
        for cc in COMMUNITY_CHEST:
            p = P[i][cc]
            P[i][cc] *= 14 / 16
            P[i][GO] += p / 16
            P[i][JAIL] += p / 16

    # Chance
    for i in range(40):
        for ch in CHANCE:
            p = P[i][ch]
            P[i][ch] *= 6 / 16
            P[i][GO] += p / 16
            P[i][JAIL] += p / 16
            P[i][C1] += p / 16
            P[i][E3] += p / 16
            P[i][H2] += p / 16
            P[i][R1] += p / 16
            P[i][ch - 3] += p / 16
            r = R2 if ch == CHANCE[0] else (R3 if ch == CHANCE[1] else R1)
            P[i][r] += p / 8
            u = U2 if ch == CHANCE[2] else U1
            P[i][u] += p / 16

    return P


def get_stationary_distribution(P):
    Q = np.asarray(P)
    evals, evecs = np.linalg.eig(Q.T)
    evec1 = evecs[:, np.isclose(evals, 1)]
    evec1 = evec1[:, 0]
    stationary = evec1 / evec1.sum()
    stationary = stationary.real
    return list(stationary)
