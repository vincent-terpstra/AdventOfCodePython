import math

from Year2023.file_helper import readfile

file_path = 'Data\\day06puzzle.txt'
lines = readfile(file_path)


class Race:
    def __init__(self, parts):
        self.time = int(parts[0])
        self.distance = int(parts[1])

    def set_distance(self, distance):
        self.distance = distance

    def __repr__(self):
        return f'(time: {self.time}, distance {self.distance})'

    def solution_1(self):
        return sum(1 for charge in range(1, self.time) if self.dist_traveled(charge) > self.distance)

    def dist_traveled(self, charge_time):
        return (self.time - charge_time) * charge_time


def int_from_row(line):
    return int(line.split(':')[1].replace(" ", ""))


def solution_1():
    races = list(map(Race, zip(lines[0].split(':')[1].split(), lines[1].split(':')[1].split())))
    multi = math.prod(race.solution_1() for race in races)
    print(multi)


def solution_2():
    time = int_from_row(lines[0])
    distance = int_from_row(lines[1])
    race = Race((time, distance))
    # note using solution1 to solve is slightly suboptimal
    # 32583852
    print(race.solution_1())


solution_2()


# solution_1()

