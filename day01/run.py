import os 
from itertools import combinations

def find_pair(values, target: int):
    seen = {}
    for v in values:
        if seen.get(target - v):
            return [v, target - v]
        else:
            seen[v] = True

def find_triple(values, target: int):
    comb = combinations(values, 3)
    for v in comb:
        if sum(v) == target:
            return v

inputs = [int(line) for line in open(f'{os.path.dirname(__file__)}/input.txt', 'r').readlines()]

pair = find_pair(values=inputs, target=2020)
print(f"{pair[0]} * {pair[1]} = {pair[0] * pair[1]}")

triple = find_triple(values=inputs, target=2020)
print(f"{triple[0]} * {triple[1]} * {triple[2]} = {triple[0] * triple[1] * triple[2]}")
