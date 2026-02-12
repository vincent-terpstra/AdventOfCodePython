from Year2023.file_helper import readfile
import re

file_path = 'Data\\day05puzzle.txt'
lines = readfile(file_path)


class RangeToRange:
    def __init__(self, row):
        self.offset, self.min, self.range = map(int, row.split())
        self.max = self.min + self.range
        self.offset_max = self.offset + self.range

    def __str__(self):
        return f'{self.min}, {self.max}: {self.offset}'

    def __repr__(self):
        return f'({self.min}, {self.max}) => ({self.offset}, {self.offset_max})'

    def contains(self, value):
        return self.min <= value <= self.max

    def slice(self, values):
        min_value = self.offset
        max_value = self.offset_max

        if values[0] > self.min:
            min_value = values[0] - self.min + self.offset

        if values[1] < self.max:
            max_value = values[1] - self.min + self.offset

        return min_value, max_value


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

solution_1_seed = 30692976


def solution_part_1():
    min_target = 100000000000
    # for value in seeds:
    for value in seeds:
        seed = value
        for rangelist in ranges:
            match = next((x for x in rangelist if x.contains(seed)), None)
            if match is not None:
                seed = seed - match.min + match.offset
        if seed < min_target:
            min_target = seed
    print(min_target)


# note this is not optimal, brute force solution
def solution_part_2():
    seed_ranges = []
    min_range = 58120175
    min_range = 99751240
    max_range = 260178142
    for offset in range(int(len(seeds) / 2)):
        lower = seeds[offset * 2]
        bound = seeds[offset * 2 + 1]
        seed_ranges.append((lower, lower + bound))
    ranges.reverse()
    for value in range(min_range, max_range + 1):
        try:
            options = [value]
            for rangelist in ranges:
                current_options = options
                options = []
                for target in current_options:
                    inner = False
                    for x in rangelist:
                        if x.offset <= target <= x.offset_max:
                            options.append(target - x.offset + x.min)
                        if x.min <= target <= x.max:
                            inner = True
                    if not inner:
                        options.append(target)
            for opt in options:
                for seed in seed_ranges:
                    if seed[0] <= opt <= seed[1]:
                        print("solution found")
                        print(value)
                        return value
        except KeyboardInterrupt:
            print(value)


range_solution = 74139777


def solution_part_2_ranges():
    matches = []
    for offset in range(int(len(seeds) / 2)):
        lower = seeds[offset * 2]
        bound = seeds[offset * 2 + 1]
        matches.append((lower, lower + bound))
    for range_map in ranges:
        current_ranges = matches
        matches = []
        for match in current_ranges:
            matching_ranges = list(r for r in range_map if r.min <= match[1] and r.max >= match[0])
            matching_ranges.sort(key=lambda r: r.min)
            match_count = len(matching_ranges)
            if match_count > 0:
                if matching_ranges[0].min > match[0]:
                    matches.append((match[0], matching_ranges[0].min - 1))

                matches.append(matching_ranges[0].slice(match))

                for current_range, next_range in zip(matching_ranges[0:-1], matching_ranges[1:]):
                    if current_range.max < next_range.min:
                        matches.append((current_range.max + 1, next_range.min - 1))
                    matches.append(next_range.slice(match))

                if matching_ranges[-1].max < match[1]:
                    matches.append((matching_ranges[-1].max + 1, match[1]))
            else:
                matches.append(match)
    print(min(x[0] for x in matches))


# solution_part_1()
# solution_part_2()
solution_part_2_ranges()


