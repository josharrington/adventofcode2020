from collections import Counter
import os

def parse_file(name) -> list:
    lines = open(f'{os.path.dirname(__file__)}/{name}', 'r').read().splitlines()
    groups = []
    group_lines = []

    for index, line in enumerate(lines):
        if line == "":
            groups.append(group_lines)
            group_lines = []
            continue

        group_lines.append(line)
        
        # If we're on the last line, create a group
        if index == len(lines) - 1:
            groups.append(group_lines)
    return groups

def part1(groups):
    tally = 0
    for group in groups:
        count = Counter(''.join(group))
        tally += len(count)
    return tally

def part2(groups):
    tally = 0
    for group in groups:
        if len(group) == 1:
            tally += len(group[0])
            continue
        sets = [set(g) for g in group]
        intersection = sets[0].intersection(*sets)
        tally += len(intersection)
    return tally

groups = parse_file('input.txt')
print(f'Part 1: {part1(groups)}')
print(f'Part 2: {part2(groups)}')