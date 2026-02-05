from Year2023.file_helper import readfile
import re

file_path = 'Data\\day04puzzle.txt'
lines = readfile(file_path)


class Card:
    def __init__(self, value):
        parts = re.split('[:|]', value)
        self.numbers = list(map(int, parts[1].split()))
        self.winning = list(map(int, parts[2].split()))
        self.copies = 1

    def total(self):
        return sum(1 for num in self.numbers if num in self.winning)

    def score(self):
        matches = self.total()
        return matches if matches < 2 else pow(2, matches - 1)


cards = list(map(Card, lines))
total = sum(map(lambda c: c.score(), cards))
print(total)

for idx, card in enumerate(cards):
    wins = card.total()
    for val in range(0, wins):
        cards[idx + val + 1].copies += card.copies


total2 = sum(card.copies for card in cards)
print(total2)
