from Year2023.file_helper import readfile
from Models.map import Map

file_path = 'Data\\day03puzzle.txt'

lines = readfile(file_path)
puzzle = Map(lines)
total = 0


def is_part(x, y):
    if puzzle.get(x-1, y-1) != '.' or puzzle.get(x-1, y) != '.' or puzzle.get(x-1, y+1) != '.':
        return True

    while puzzle.get(x, y).isdigit():
        if puzzle.get(x, y - 1) != '.' or puzzle.get(x, y + 1) != '.':
            return True
        x = x+1

    if puzzle.get(x, y-1) != '.' or puzzle.get(x, y) != '.' or puzzle.get(x, y+1) != '.':
        return True

    return False


for line in puzzle.get_rows():
    for number in line.get_numbers():
        if is_part(number[0], line.y):
            total += number[1]

print(total)
