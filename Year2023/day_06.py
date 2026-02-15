import math

from Year2023.file_helper import readfile

file_path = 'Data\\day06puzzle.txt'
lines = readfile(file_path)


class Race:
    def __init__(self, time):
        self.time = int(time)
        self.distance = 0

    def set_distance(self, distance):
        self.distance = distance

    def __repr__(self):
        return f'(time: {self.time}, distance {self.distance})'

    def solution_1(self):
        return sum(1 for charge in range(1, self.time) if self.dist_traveled(charge) > self.distance)

    def dist_traveled(self, charge_time):
        return (self.time - charge_time) * charge_time


races = list(map(Race, lines[0].split(':')[1].split()))
for race, dist in zip(races, lines[1].split(':')[1].split()):
    race.set_distance(int(dist))

multi = math.prod(race.solution_1() for race in races)
print(multi)
