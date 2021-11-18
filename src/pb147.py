"""
Problem 147 of Project Euler.

https://projecteuler.net/problem=147

The basic idea behind the counting is to count build the grid
starting from a 1xh grid, and building it up column by column.
Then the number of rectangles in a bxh grid
is the number of rectangles in at (b - 1)xh grid
plus the number of rectangles that use the last column.

I split up the counting of rectangles in the last column by the horizontal rectangles,
the diagonal rectangles touching the outher edge,
and the diagonal rectangles not touching the outher edge but still in the last column.

The actual counting of the rectangles in the last column,
I leave as an exercise to the reader.
(The horizontal rectangles are easy,
but the diagonal rectangles require a clever counting argument.
Start with a rectangle in the last column and see the number of
rectangles where the starting point is the right-most corner.)
"""

from functools import cache


def problem147(height=47, base=43):
    @cache
    def num_rectangles(b, h):
        """
        Number or rectangles that use the right-most column of the grid.
        """
        if b == 0:
            return 0
        return (
            num_horizontal_rectangles_last_column(b, h)
            + num_flush_diagonals_last_column(b, h)
            + num_offset_diagonals_last_column(b, h)
            + num_rectangles(b - 1, h)
        )

    return sum(
        num_rectangles(b, h) for h in range(1, height + 1) for b in range(1, base + 1)
    )


def num_horizontal_rectangles_last_column(b, h):
    return b * h * (h + 1) // 2


def num_flush_diagonals_last_column(base, height):
    diag_base = 2 * base - 1
    ans = 0
    for i, h in enumerate(range(height - 1, 0, -1)):
        i = min(2 * (i + 1), diag_base)
        for b in range(i):
            ans += min(2 * h, diag_base - b)
    return ans


def num_offset_diagonals_last_column(base, height):
    diag_base = 2 * (base - 1)
    ans = 0
    for i, h in enumerate(range(height, 0, -1)):
        i = min(2 * i + 1, diag_base)
        for b in range(i):
            ans += min(2 * h - 1, diag_base - b)
    return ans
