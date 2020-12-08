import os
import re 

def parse_file(file): 
    lines = open(f'{os.path.dirname(__file__)}/{file}', 'r').read().splitlines()
    results = {}
    for line in lines:
        parent, children = re.match(r'^(.*) bags contain (.*)\.$', line).groups()
        children = {child[1]: int(child[0]) for child in re.findall('(\d+) (.+?) bag', children)}
        results[parent] = children
    return results

def part1_find_parents(tree, find):
    # I'm not happy with the O() complexity of this one and I'm sure there's a better
    # computer sciencey approach. However, for this data set it's quite fast.
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
    total += sum([tree[find][child] + part2_bags_inside(tree, child) * tree[find][child] 
                  for child in tree[find].keys()])
    return total

tree = parse_file('input.txt')
print(f"Part 1: {part1_find_parents(tree, 'shiny gold')}")
print(f"Part 2: {part2_bags_inside(tree, 'shiny gold')}")
