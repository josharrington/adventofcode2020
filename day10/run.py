import os
from functools import lru_cache

class Joltage():
    joltages = []

    def __init__(self, file: str):
        self.joltages = [int(x) for x in open(f'{os.path.dirname(__file__)}/{file}', 'r').read().splitlines()]
        self.joltages.sort()

    def part1(self):
        diffs = {'1': 0, '2': 0, '3': 0}
        previous_joltage = 0

        for joltage in self.joltages:
            diffs[str(joltage - previous_joltage)] += 1
            previous_joltage = joltage

        return diffs['1'] * (diffs['3'] + 1)

    def part2(self):
        def find_next(idx) -> list:
            window = self.joltages[idx+1:idx+4]
            r = []
            for index, v in enumerate(window):
                if idx == -1:
                    if v <= 3:
                        r.append(v)
                else:
                    if v - self.joltages[idx] <= 3:
                        r.append(v)
            return r

        # First, calculate the differences and store in a tree
        tree = {}
        tree['0'] = find_next(-1)
        for index, v in enumerate(self.joltages):
            tree[str(v)] = find_next(index)

        # Then, run through each possibility. Cache results to speed it up
        @lru_cache
        def h(idx):
            total = 0
            if len(tree[str(idx)]) == 0:
                return 1
            else:
                for x in tree[str(idx)]:
                    total += h(x)
            return total

        t = h(0)
        return t

if __name__ == "__main__":
    joltage = Joltage('input.txt')
    print(f"Part 1: {joltage.part1()}")
    print(f"Part 2: {joltage.part2()}")