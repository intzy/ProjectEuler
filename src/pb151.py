"""
Problem 151 of Project Euler.

https://projecteuler.net/problem=151

Memoization works fine here.

Let "state" be sum state of the envelope, and let state_next be a possible
state of the envelope after taking a piece of paper from state.
Then by the law of conditional expectation, if E[state] is the expected value
of a single sheet of paper being the envelope, then

    E[state] = sum(E[state_next] * p(state_next) for state_next after state),

with suitable base cases.
"""


def problem151(papersize=5):
    state = [0] * papersize
    state[0] = 1
    return round(expected_num(state, {}, papersize) - 2, 6)


def expected_num(state, cache, papersize):
    if tuple(state) in cache:
        return cache[tuple(state)]

    num_sheets = sum(state)
    if num_sheets == 0:
        return 0
    expected_val = 1 if num_sheets == 1 else 0

    for i in range(papersize):
        if state[i] == 0:
            continue
        state_next = state.copy()
        state_next[i] -= 1
        for j in range(i + 1, papersize):
            state_next[j] += 1

        expected_val += (
            expected_num(state_next, cache, papersize) * state[i] / num_sheets
        )

    cache[tuple(state)] = expected_val
    return expected_val
