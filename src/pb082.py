"""
Problem 082 of Project Euler.

https://projecteuler.net/problem=082

Dynamic programming.
"""

from math import inf

from lib.misc import file_to_matrix


def problem082(filename="txt/pb082.txt"):
    M = file_to_matrix(filename, ",")
    M = list(map(list, zip(*M)))

    for k in range(1, len(M)):
        new_row = list(M[k])
        row = M[k]
        prev_row = M[k - 1]
        for i in range(len(M)):
            new_row[i] += min(
                prev_row[i],
                min((sum(row[j:i]) + prev_row[j] for j in range(i)), default=inf),
                min(
                    (
                        sum(row[i + 1 : j + 1]) + prev_row[j]
                        for j in range(i + 1, len(M))
                    ),
                    default=inf,
                ),
            )
        M[k] = new_row
    return min(M[-1])
