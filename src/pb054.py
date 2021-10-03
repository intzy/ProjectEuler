"""
Problem 054 of Project Euler.

https://projecteuler.net/problem=054
"""


def problem054(filename="txt/pb054.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()

    p1_hands = []
    p2_hands = []
    for string in strings:
        x = [Card(c) for c in string.split()]
        p1_hands.append(PokerHand(x[:5]))
        p2_hands.append(PokerHand(x[5:]))

    p1_wins = 0
    for p1_hand, p2_hand in zip(p1_hands, p2_hands):
        if p1_hand.wins_against(p2_hand):
            p1_wins += 1
    return p1_wins


class Card:
    def __init__(self, cardstr):
        letter_suits = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
        self.suit = cardstr[1]
        val = cardstr[0]
        if val in letter_suits:
            self.val = letter_suits[val]
        else:
            self.val = int(val)


class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        self.suits = [c.suit for c in self.hand]
        self.vals = [c.val for c in self.hand]
        self.vals.sort()

    def wins_against(self, opponent):
        self_hands = [
            self.straigh_flush,
            self.four_of_a_kind,
            self.full_house,
            self.flush,
            self.straight,
            self.three_of_a_kind,
            self.two_pairs,
            self.pair,
            self.high_card,
        ]
        opponent_hands = [
            opponent.straigh_flush,
            opponent.four_of_a_kind,
            opponent.full_house,
            opponent.flush,
            opponent.straight,
            opponent.three_of_a_kind,
            opponent.two_pairs,
            opponent.pair,
            opponent.high_card,
        ]

        for self_hand, opponent_hand in zip(self_hands, opponent_hands):
            if self_hand() != opponent_hand():
                return self_hand() > opponent_hand()
        return False

    def straigh_flush(self):
        if self.straight() and self.flush():
            return self.vals[4]
        return 0

    def four_of_a_kind(self):
        if self.vals[0] == self.vals[3]:
            return self.vals[3]
        if self.vals[1] == self.vals[4]:
            return self.vals[4]
        return 0

    def full_house(self):
        if self.three_of_a_kind() and self.pair():
            if self.vals[0] == self.vals[2]:
                return 10 * self.vals[0] + self.vals[3]
            return 10 * self.vals[2] + self.vals[0]
        return 0

    def flush(self):
        if all(s == self.suits[0] for s in self.suits[1:]):
            return self.vals[4]
        return 0

    def straight(self):
        if all(val == self.vals[0] + i for i, val in enumerate(self.vals)):
            return self.vals[4]
        return 0

    def three_of_a_kind(self):
        if self.vals[0] == self.vals[1] == self.vals[2]:
            return self.vals[0]
        if self.vals[1] == self.vals[2] == self.vals[3]:
            return self.vals[1]
        if self.vals[2] == self.vals[3] == self.vals[4]:
            return self.vals[2]
        return 0

    def two_pairs(self):
        if self.vals[0] == self.vals[1]:
            if self.vals[2] == self.vals[3]:
                return self.vals[3] * 10 + self.vals[1]
            if self.vals[3] == self.vals[4]:
                return self.vals[4] * 10 + self.vals[1]
        if self.vals[1] == self.vals[2] and self.vals[3] == self.vals[4]:
            return self.vals[4] * 10 + self.vals[2]
        return 0

    def pair(self):
        if self.vals.count(self.vals[1]) == 2:
            return self.vals[1]
        if self.vals.count(self.vals[2]) == 2:
            return self.vals[2]
        if self.vals.count(self.vals[3]) == 2:
            return self.vals[3]
        return 0

    def high_card(self):
        return self.vals[4]
