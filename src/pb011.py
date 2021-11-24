"""
Problem 011 of Project Euler.

https://projecteuler.net/problem=011
"""

from itertools import product
from math import prod

from lib.misc import file_to_matrix


def problem011(length=4, filename="txt/pb011.txt"):
    grid = file_to_matrix(filename, " ")

    size = len(grid)
    grid_products = []

    for x, y in product(range(0, size), repeat=2):

        # check veritcal row downwards
        if x + length < size:
            grid_products.append(prod(grid[i][y] for i in range(x, x + length)))

        # check horixonal row rightwards
        if y + length < size:
            grid_products.append(prod(grid[x][i] for i in range(y, y + length)))

        # check down-right diagonal
        if x + length < size and y + length < size:
            grid_products.append(prod(grid[x + i][y + i] for i in range(length)))

        # check down-left diagonal
        if x + length < size and y - length + 1 >= 0:
            grid_products.append(prod(grid[x + i][y - i] for i in range(length)))

    return max(grid_products)
