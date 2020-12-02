import re 
import os

class PasswordPolicy:
    num1: int
    num2: int
    search: str
    password: str

    def __init__(self, line):
        splits = line.strip('\n').split(' ')
        self.num1, self.num2 = [int(x) for x in splits[0].split('-')]
        self.search = splits[1][0]
        self.password = splits[2]

    def check_part1(self):
        return self.num1 <= self.password.count(self.search) <= self.num2

    def check_part2(self):
        # Use a nor operator to identify good passwords
        return (self.password[self.num1-1] == self.search) ^ (self.password[self.num2-1] == self.search)

policies = [PasswordPolicy(line) for line in open(f'{os.path.dirname(__file__)}/input.txt', 'r').readlines()]
print(f"Part 1: {[x.check_part1() for x in policies].count(True)}")
print(f"Part 2: {[x.check_part2() for x in policies].count(True)}")