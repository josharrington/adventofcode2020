import os

class Gameboy():
    accumulator = 0
    visited_lines = []
    current_line = 0
    commands = []

    def __init__(self, file):
        self.parse_file(file)
    
    def parse_file(self, file): 
        lines = open(f'{os.path.dirname(__file__)}/{file}', 'r').read().splitlines()
        self.commands = [[x[0:3], int(x[4:])] for x in lines]

    def clear(self):
        self.accumulator = 0
        self.visited_lines = []
        self.current_line = 0

    def run(self):
        self.clear()
        while self.current_line not in self.visited_lines:
            if self.current_line >= len(self.commands):
                return self.accumulator, "EXIT_END"

            if self.current_line < 0:
                return self.accumulator, "EXIT_OOB"

            self.visited_lines.append(self.current_line)
            command, argument = self.commands[self.current_line]

            if command == 'nop':
                pass
            elif command == 'acc':
                self.accumulator += argument
            elif command == 'jmp':
                self.current_line = self.current_line + argument
            
            if command != 'jmp':
                self.current_line += 1
        return self.accumulator, "EXIT_LOOP"

    def part1(self):
        self.run()
        return self.accumulator
        
    def part2(self):
        # Toggle each noop or jump and try it to see if it exits. 
        # Brute force
        for line, (command, argument) in enumerate(self.commands):
            if command == 'acc':
                continue
            
            if command == 'jmp':
                self.commands[line][0] = 'nop'
            else:
                self.commands[line][0] = 'jmp'

            if self.run()[1] == "EXIT_END":
                return self.accumulator
            else:
                self.commands[line][0] = command

game = Gameboy('input.txt')
print(game.part1())
print(game.part2())