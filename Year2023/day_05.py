from Year2023.file_helper import readfile
import re

file_path = 'Data\\day05puzzle.txt'
lines = readfile(file_path)


class RangeToRange:
    def __init__(self, row):
        self.offset, self.min, self.range = map(int, row.split())
        self.max = self.min + self.range

    def __str__(self):
        return f'{self.min}, {self.max}: {self.offset}'

    def contains(self, value):
        return self.min <= value <= self.max


class RangeList:
    pass


ranges = []

for line in lines:
    if line.startswith('seeds:'):
        seeds = list(map(int, line.split(':')[1].split()))
    elif len(line) > 0:
        if line[0].isdigit():
            current.append(RangeToRange(line))
        else:
            current = []
            ranges.append(current)
min_seed = 100000000000
for seed in seeds:
    for rangelist in ranges:
        match = next((x for x in rangelist if x.contains(seed)), None)
        if match is not None:
            seed = seed - match.min + match.offset
    min_seed = min(seed, min_seed)

print(min_seed)



