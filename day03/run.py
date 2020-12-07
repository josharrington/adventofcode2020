import os 
from math import prod

def calculate_trees(geology, slope_x, slope_y):
    x = 0
    trees = 0
    x_max = len(geology[0])
    for index, y in enumerate(range(0, len(geology), slope_y)):
        x = index * slope_x
        if geology[y][x % x_max] == '#':
            trees += 1
    return trees

lines = open(f'{os.path.dirname(__file__)}/input.txt', 'r').read().splitlines()
print(f"Part 1 Trees encountered: {calculate_trees(lines, slope_x=3, slope_y=1)}")

product = prod([
    calculate_trees(lines, slope_x=1, slope_y=1),
    calculate_trees(lines, slope_x=3, slope_y=1),
    calculate_trees(lines, slope_x=5, slope_y=1),
    calculate_trees(lines, slope_x=7, slope_y=1),
    calculate_trees(lines, slope_x=1, slope_y=2),
]) 

print(f"Part 2 Product: {product}")