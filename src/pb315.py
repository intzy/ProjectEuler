"""
Problem 315 of Project Euler.

https://projecteuler.net/problem=315

For Sam's, the algorithm is simply two times the amount of LEDs of each number
For Max's, the algorithm is the amount of LEDs of the first number,
            + the amount of LEDS of the last number,
            + the number of LEDs that are different between each number in the cycle
"""

from lib.primes import list_primes


def problem315(lower_bound=10_000_000, upper_bound=20_000_000):
    sams_transitions = []
    maxs_transitions = []
    primes = [p for p in list_primes(upper_bound) if p >= lower_bound]

    for n in range(0, 10):
        sams_transitions.append(2 * DISPLAY[n].display_count)
        maxs_transitions.append(DISPLAY[n].display_count)

    for n in range(10, 9 * len(str(upper_bound)) + 1):
        # The second step of the digital root sequence can't be more than
        # 9 * num_digits(upper_bound)
        root = digital_root(n)
        sams_transitions.append(2 * turn_on(n) + sams_transitions[root])
        maxs_transitions.append(switch(n, root) + maxs_transitions[root])

    sams_transition_count = 0
    maxs_transition_count = 0
    for p in primes:
        root = digital_root(p)
        sams_transition_count += 2 * turn_on(p) + sams_transitions[root]
        maxs_transition_count += turn_on(p) + switch(p, root) + maxs_transitions[root]

    return sams_transition_count - maxs_transition_count


def digital_root(num):
    root = 0
    x = num
    while x > 0:
        root += x % 10
        x //= 10
    return root


def turn_on(x):
    transitions = 0
    while x > 0:
        transitions += DISPLAY[x % 10].display_count
        x //= 10
    return transitions


def switch(n1, n2):
    transitions = 0
    while n2 != 0:
        for dis1, dis2 in zip(DISPLAY[n1 % 10].display, DISPLAY[n2 % 10].display):
            if dis1 != dis2:
                transitions += 1
        n1 //= 10
        n2 //= 10

    while n1 != 0:
        transitions += DISPLAY[n1 % 10].display_count
        n1 //= 10
    return transitions


class Display:
    def __init__(self, display):
        self.display = display
        self.display_count = sum(1 for dis in display if dis)


#    -----0-----
#    =         =
#    5         1
#    =         =
#    -----6-----
#    =         =
#    4         2
#    =         =
#    -----3-----


ZERO_DISPLAY = [True, True, True, True, True, True, False]
ONE_DISPLAY = [False, True, True, False, False, False, False]
TWO_DISPLAY = [True, True, False, True, True, False, True]
THREE_DISPLAY = [True, True, True, True, False, False, True]
FOUR_DISPLAY = [False, True, True, False, False, True, True]
FIVE_DISPLAY = [True, False, True, True, False, True, True]
SIX_DISPLAY = [True, False, True, True, True, True, True]
SEVEN_DISPLAY = [True, True, True, False, False, True, False]
EIGHT_DISPLAY = [True, True, True, True, True, True, True]
NINE_DISPLAY = [True, True, True, True, False, True, True]

DISPLAY = [
    Display(ZERO_DISPLAY),
    Display(ONE_DISPLAY),
    Display(TWO_DISPLAY),
    Display(THREE_DISPLAY),
    Display(FOUR_DISPLAY),
    Display(FIVE_DISPLAY),
    Display(SIX_DISPLAY),
    Display(SEVEN_DISPLAY),
    Display(EIGHT_DISPLAY),
    Display(NINE_DISPLAY),
]
