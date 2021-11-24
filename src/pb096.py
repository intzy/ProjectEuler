"""
Problem 096 of Project Euler.

https://projecteuler.net/problem=096

I simply used a backtracking algorithm, with no optimizations.

Could probably be made significantly faster if I changed the 2d 9*9 lists
into a 1d 1*81 list.
"""

from lib.misc import concat_ints


def problem096(filename="txt/pb096.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        string = f.readline()
        sodukus = []
        while string:
            soduku = []
            for _ in range(1, 10):
                string = f.readline()
                row = [int(d) for d in string[:9]]
                soduku.append(row)
            sodukus.append(soduku)
            string = f.readline()

    summation = 0
    for soduku in sodukus:
        soduku = solve_soduku(soduku)
        summation += concat_ints(soduku[0][0], soduku[0][1], soduku[0][2])
    return summation


def solve_soduku(soduku):
    return solve_soduku_helper(soduku, 0)


def solve_soduku_helper(soduku, i):
    if i == 81:
        return soduku
    row = i // 9
    column = i % 9
    if soduku[row][column] != 0:
        return solve_soduku_helper(soduku, i + 1)
    for d in availabe_digits(soduku, column, row):
        soduku[row][column] = d
        if solve_soduku_helper(soduku, i + 1):
            return soduku
    soduku[row][column] = 0
    return False


def availabe_digits(soduku, column, row):
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    column_digits = digits - {soduku[r][column] for r in range(9)}
    row_digits = digits - {soduku[row][c] for c in range(9)}
    box_digits = digits - {
        soduku[3 * (row // 3) + i][3 * (column // 3) + j]
        for i in range(3)
        for j in range(3)
    }
    return column_digits.intersection(row_digits, box_digits)
