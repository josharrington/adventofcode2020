import os
import re

class Passport():
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def __init__(self, input):
        # Lines will have fields from a batch item in no particular order
        for field in input.split(' '):
            key,value = field.split(':')
            setattr(self, key, value)
    
    def is_valid_part1(self):
        # Valid passports have all fields filled out with cid optional.
        # Can't do a normal "return self.byr and self.iyr..." here since python needs
        # to determine truthiness.
        if self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid:
            return True
        else: 
            return False
    
    def is_valid_part2(self):
        # Skip any passports that don't have all the required fields
        if not self.is_valid_part1():
            return False

        if not 1920 <= int(self.byr) <= 2002:
            return False

        if not 2010 <= int(self.iyr) <= 2020:
            return False

        if not 2020 <= int(self.eyr) <= 2030:
            return False
        
        if not self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        #pid
        if not re.match('^[0123456789]{9}$', self.pid):
            return False

        #hcl
        if not re.match('^#[0123456789abcdef]{6}$', self.hcl):
            return False

        #hgt
        try:
            if self.hgt.endswith('cm'):
                units = self.hgt[:-2]
                valid_hgt = 150 <= int(units) <= 193
            elif self.hgt.endswith('in'):
                units = self.hgt[:-2]
                valid_hgt = 59 <= int(units) <= 76
            else:
                valid_hgt = False
        except:
            valid_hgt = False
        
        if not valid_hgt:
            return False

        # Everything passed
        return True

def parse_file(name) -> list:
    lines = open(f'{os.path.dirname(__file__)}/{name}', 'r').read().splitlines()
    passport_lines = []
    passports = []

    for index, line in enumerate(lines):
        if line == "":
            passports.append(Passport(' '.join(passport_lines)))
            passport_lines = [] 
            continue
        
        passport_lines.append(line)
        
        # If we're on the last line, create a passport
        if index == len(lines) - 1:
            passports.append(Passport(' '.join(passport_lines)))
    return passports

passports = parse_file('input.txt')
print(f"Part 1: {[p.is_valid_part1() for p in passports].count(True)}")
print(f"Part 2: {[p.is_valid_part2() for p in passports].count(True)}")
