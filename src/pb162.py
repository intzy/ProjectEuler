"""
Problem 162 of Project Euler.

https://projecteuler.net/problem=162

Consider k = 5.
The number of strings with 5 digits that don't contain any of 0, 1, A,
will be the number of 4 digit strings that don't times however many
digits we can append to it, i.e., times 13.
For example, 3567_ will be a string that doesn't contain
any of 0, 1, A if we append any of the other thirteen digits to 3567.

By condering string with none of 0, 1, A,
strings with exactly one of 0, 1, A (say 0),
string with exactly two of 0, 1, A (say 1, A),
and strings with all three of 0, 1, A,
we can come up with a recurrence relation for each possiblity.

Summing over all n <= k for the number of n-digit strings with
all of 0, 1, A, will give the final result.

Note that we account for no leading zeros in the base case.
"""


def problem162(k=16):
    n_digit_occurences = [HexadecimalCombinations(n + 1) for n in range(k)]
    for n in range(k):
        n_digit_occurences[n].count_occurences(n_digit_occurences[n - 1])
    return hex(sum(x.value() for x in n_digit_occurences[1:]))[2:].upper()


class HexadecimalCombinations:
    def __init__(self, n):
        self.n = n
        self.count_ = None
        self.count0 = None
        self.count1 = None
        self.countA = None
        self.count01 = None
        self.count0A = None
        self.count1A = None
        self.count01A = None

    def value(self):
        return self.count01A

    def count_occurences(self, prev):
        if self.n == 1:
            self.count_ = 13
            self.count0 = 0
            self.count1 = 1
            self.countA = 1
            self.count01 = 0
            self.count0A = 0
            self.count1A = 0
            self.count01A = 0
            return

        self.count_ = 13 * prev.count_
        self.count0 = 14 * prev.count0 + prev.count_
        self.count1 = 14 * prev.count1 + prev.count_
        self.countA = 14 * prev.countA + prev.count_
        self.count01 = 15 * prev.count01 + prev.count0 + prev.count1
        self.count0A = 15 * prev.count0A + prev.count0 + prev.countA
        self.count1A = 15 * prev.count1A + prev.count1 + prev.countA
        self.count01A = 16 * prev.count01A + prev.count01 + prev.count0A + prev.count1A
