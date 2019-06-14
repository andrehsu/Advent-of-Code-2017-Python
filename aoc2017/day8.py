from collections import defaultdict
from typing import Dict, List

from util import test_case, read_input

INPUT = read_input(8)
TEST_INPUT = test_case("""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""")


def day8(input_: List[str]):
    registers: Dict[str, int] = defaultdict(int)
    
    max_held = -1
    
    for line in input_:
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


day8(TEST_INPUT)
day8(INPUT)
