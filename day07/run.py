import os
import re 

def parse_file(file): 
    lines = open(f'{os.path.dirname(__file__)}/{file}', 'r').read().splitlines()
    results = {}
    for line in lines:
        s = list(map(str.strip, line.split("contain")))
        key = re.sub('bags?$', '', s[0]).strip()
        results[key] = {}

        if s[1] != "no other bags.":
            for item in s[1].split(','):
                item = re.sub('bags?\.?$', '', item).strip()
                count, subkey = item.split(' ', 1) 
                results[key][subkey] = int(count)
    return results

def part1(tree, find):
    done = False
    bags = set()
    to_find = [find]
    while not done:
        prev_count = len(bags)
        parents = []
        for item in to_find:
            parents += [x for x in tree if item in tree[x]]
        bags.update(parents)
        to_find = parents

        # If we're done searching
        done = prev_count == len(bags)

    return len(bags)

def part2_bags_inside(tree, find):
    # Use recursion to find each child's bag total. Then sum them all up
    total = 0
    total += sum([tree[find][x] + part2_bags_inside(tree, x)*tree[find][x] for x in tree[find].keys()])
    return total

tree = parse_file('input.txt')
print(f"Part 1: {part1(tree, 'shiny gold')}")
print(f"Part 2: {part2_bags_inside(tree, 'shiny gold')}")
