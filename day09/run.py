import os

class Debugger():
    preamble = 0
    lines = []

    def __init__(self, file: str, preamble: int):
        self.lines = [int(x) for x in open(f'{os.path.dirname(__file__)}/{file}', 'r').read().splitlines()]
        self.preamble = preamble

    def part1(self):
        found = False
        considering_index = self.preamble
        window_start = 0
        window_end = self.preamble

        while not found:
            window = self.lines[window_start:window_end]
            considering = self.lines[considering_index]

            for idx,num in enumerate(window):
                # If we're on the last item, our number isnt a sum of any two in the window
                if idx == self.preamble - 1:
                    return considering

                # If our number is greater than the considered number, and
                # we aren't on the final number in the window
                if num > considering and idx != self.preamble - 1:
                    continue

                # If we find that the considered number is the sum of the current num and
                # another num in the list, move on
                if considering - num in window:
                    break

            window_start += 1
            window_end += 1
            considering_index +=1

    def part2(self, target: int):
        start_idx = 0
        end_idx = 1
        running_total = self.lines[0] + self.lines[1]

        while running_total != target:
            if running_total < target:
                end_idx += 1
                running_total += self.lines[end_idx]
            if running_total > target:
                running_total -= self.lines[start_idx]
                start_idx += 1

        window = sorted(self.lines[start_idx:end_idx+1])
        return window[0] + window[-1]

if __name__ == "__main__":
    d = Debugger('input.txt', preamble=25)
    result_part1 = d.part1()
    print(f"Part 1: {result_part1}")
    print(f"Part 2: {d.part2(result_part1)}")
