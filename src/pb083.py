"""
Problem 083 of Project Euler.

https://projecteuler.net/problem=083

Bellman-Ford.
"""

from math import inf

from lib.misc import file_to_matrix


def problem083(filename="txt/pb083.txt"):
    M = file_to_matrix(filename, ",")
    l = len(M)
    D = [[inf for _ in range(l + 2)] for _ in range(l + 2)]
    D[1][1] = M[0][0]
    modified = True

    while modified:
        modified = False

        for i in range(1, l + 1):
            for j in range(1, l + 1):
                x = min(D[i - 1][j], D[i + 1][j], D[i][j - 1], D[i][j + 1])
                if M[i - 1][j - 1] + x < D[i][j]:
                    modified = True
                    D[i][j] = M[i - 1][j - 1] + x

    return D[-2][-2]
