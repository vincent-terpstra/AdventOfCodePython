from Year2023.file_helper import readfile
from Models.map import Map
from Models.map import Point

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


def get_adjacent_numbers(point: Point):
    numbers = []
    get_number(point.x - 1, point.y, numbers)
    get_number(point.x + 1, point.y, numbers)

    if not get_number(point.x, point.y + 1, numbers):
        get_number(point.x - 1, point.y + 1, numbers)
        get_number(point.x + 1, point.y + 1, numbers)

    if not get_number(point.x, point.y - 1, numbers):
        get_number(point.x - 1, point.y - 1, numbers)
        get_number(point.x + 1, point.y - 1, numbers)

    return numbers


def get_number(x, y, numbers):
    if not puzzle.get(x, y).isdigit():
        return False
    while puzzle.get(x, y).isdigit():
        x -= 1
    x += 1
    digit = 0
    while puzzle.get(x, y).isdigit():
        digit = digit * 10 + int(puzzle.get(x, y))
        x += 1
    numbers.append(digit)
    return True


for line in puzzle.get_rows():
    for number in line.get_numbers():
        if is_part(number[0], line.y):
            total += number[1]


gears = puzzle.get_chars('*')
gear_total = 0;
for gear in gears:
    adj = get_adjacent_numbers(gear)
    if len(adj) == 2:
        gear_total += adj[0] * adj[1]

print(total)
print(gear_total)
