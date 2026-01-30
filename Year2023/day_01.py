from Year2023.file_helper import readfile

file_path = 'Data\\day01puzzle.txt'

lines = readfile(file_path)

map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def find_number(path):
    for i in path:
        if i.isdigit():
            return int(i)


def find_number_with_map(path):
    indicies = {}
    for key, value in map.items():
        start_idx = 0
        while True:
            idx = path.find(key, start_idx)
            if idx == -1:
                break
            indicies[idx] = value
            start_idx = idx + 1
    for index, value in enumerate(path):
        if value.isdigit():
            indicies[index] = int(value)

    items = sorted(indicies.items())
    return items[0][1] * 10 + items[-1][1]


sum = 0
for line in lines:
    sum += 10 * find_number(line) + find_number(reversed(line))


part2 = 0
for line in lines:
    part2 += find_number_with_map(line)


print(sum)
print(part2)