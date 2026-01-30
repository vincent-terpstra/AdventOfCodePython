import math

from Year2023.file_helper import readfile

file_path = 'Data\\day02puzzle.txt'

lines = readfile(file_path)


class Reveal:
    def __init__(self, line):
        self.values = {}
        for part in line.split(','):
            parts = part.strip().split(' ')
            self.values[parts[1]] = int(parts[0])

    def is_possible(self, values):
        return all(values[key] >= item for key, item in self.values.items())


class Game:
    def __init__(self, line):
        parts = line.split(':')
        self.id = int(parts[0].split(' ')[1])
        self.reveals = list(map(Reveal, parts[1].split(';')))

    def is_possible(self, values):
        return all(rev.is_possible(values) for rev in self.reveals)

    def required_max(self, key):
        return max(map(lambda rev: rev.values.get(key, 1), self.reveals))

    def required(self):
        keys = ['red', 'green', 'blue']
        return dict(zip(keys, map(self.required_max, keys)))

    def product(self):
        return math.prod(self.required().values())


possible = { 'red': 12, 'green': 13, 'blue': 14 }
total = sum(game.id for game in map(Game, lines) if game.is_possible(possible))
print(total)

total = sum(game.product() for game in map(Game, lines))
print(total)



