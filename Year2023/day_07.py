from enum import Enum
from Year2023.file_helper import readfile
from collections import Counter

file_path = 'Data\\day07puzzle.txt'
lines = readfile(file_path)


class Rank(Enum):
    FIVE = 10
    FOUR = 9
    FULL_HOUSE = 8
    THREE = 7
    TWO_PAIR = 6
    ONE_PAIR = 5
    HIGH_CARD = 1


class Hand:
    def __init__(self, line):
        self.cards, self.bid = line.split()
        self.bid = int(self.bid)
        self.high_card = self.get_high_card()
        self.rank = self.get_rank()

    def __repr__(self):
        return f'cards: {self.cards}, bid: {self.bid}, {self.rank}, high: {self.high_card}'

    def get_rank(self):
        counts = sorted(Counter(self.cards).values(), reverse=True)
        match counts:
            case [5]:
                return Rank.FIVE
            case [4, 1]:
                return Rank.FOUR
            case [3, 2]:
                return Rank.FULL_HOUSE
            case [3, 1, 1]:
                return Rank.THREE
            case [2, 2, 1]:
                return Rank.TWO_PAIR
            case [2, 1, 1, 1]:
                return Rank.ONE_PAIR
        return Rank.HIGH_CARD

    def get_high_card(self):
        return max(Hand.get_card_value(c) for c in self.cards)

    @staticmethod
    def get_card_value(card):
        lookup = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        return lookup[card] if card in lookup else int(card)


hands = list(map(Hand, lines))
# sort first by the rank then by card value by index
hands.sort(key=lambda h: (h.rank.value, list(map(Hand.get_card_value, h.cards))))

total = sum(((key + 1) * hand.bid) for key, hand in enumerate(hands))
print(total)
