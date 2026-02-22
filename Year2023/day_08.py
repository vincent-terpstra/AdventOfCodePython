import math

from Year2023.file_helper import readfile
from functools import reduce

file_path = 'Data\\day08puzzle.txt'
lines = readfile(file_path)


class Node:
    def __init__(self, line):
        self.id, _, self.left, self.right = line.split()
        self.left = self.left[1:-1]
        self.right = self.right[0:-1]

    def __repr__(self):
        return f'id: {self.id}, left: {self.left}, right: {self.right}'


instructions = lines[0]
nodes = list(map(Node, lines[2:]))
left_dict = {n.id: n.left for n in nodes}
right_dict = {n.id: n.right for n in nodes}


def solution_part_1(current_move='AAA', condition=lambda value: value != 'ZZZ'):
    index = 0
    while condition(current_move):
        move = instructions[index % len(instructions)]
        next_move = left_dict[current_move] if move == 'L' else right_dict[current_move]
        # print(f'start: {current_move} move: {move}, next {next_move}')
        index += 1
        current_move = next_move
    print(index)
    return index


def solution_part_2_brute_force():
    # note brute force does not work in a significant amount  of time
    ghost_starts = list(node.id for node in nodes if node.id[-1] == 'A')
    steps = 0
    while steps < 10 and not all(ghost[-1] == 'Z' for ghost in ghost_starts):
        move = instructions[steps % len(instructions)]
        print(ghost_starts)
        for i in range(len(ghost_starts)):
            ghost = ghost_starts[i]
            next_ghost = left_dict[ghost] if move == 'L' else right_dict[ghost]
            ghost_starts[i] = next_ghost
        steps += 1

    print(steps)
    print(ghost_starts)


def solution_part_2():
    ghost_starts = list(node.id for node in nodes if node.id[-1] == 'A')
    solutions = []
    for start in ghost_starts:
        solution = solution_part_1(start, lambda value: value[-1] != 'Z')
        solutions.append(solution)
        remainder = solution % len(instructions)
        # note IF all remainders are 0, we can use an LCM to determine loop
        if remainder != 0:
            raise 'need all loops to start and end over the same instruction set'
    result = reduce(math.lcm, solutions)
    print(result)


# solution_part_1()
solution_part_2()
