from collections import defaultdict
from typing import Dict, List

INPUT = open('input.txt').read().splitlines()
TEST = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""[1:-1].splitlines()


def day8(inp: List[str]):
    registers: Dict[str, int] = defaultdict(int)
    
    max_held = -1
    
    for line in inp:
        r, command, value, _, comp_r, comp, comp_value = line.split()
        if eval(f'{registers[comp_r]} {comp} {comp_value}'):  # pylint:disable= eval-used
            if command == 'inc':
                registers[r] += int(value)
            else:
                registers[r] -= int(value)
        max_ = max(registers.values())
        if max_ > max_held:
            max_held = max_
    
    print(max(registers.values()))
    
    print(max_held)


if __name__ == '__main__':
    day8(TEST)
    day8(INPUT)
