from itertools import count
from typing import List, Tuple

from util import read_input, test_case

INPUT = read_input(13)
TEST_INPUT = test_case("""
0: 3
1: 2
4: 4
6: 4
""")


def day13(input_: List[str]):
    
    def parse_line(line: str) -> Tuple[int, int]:
        a, b = (map(int, line.split(': ')))
        return a, b
    
    guards = {guard: depth for guard, depth in map(parse_line, input_)}
    max_guard = max(guards)
    
    severity = 0
    for i in range(max_guard + 1):
        if i in guards and i % ((guards[i] - 1) * 2) == 0:
            severity += i * guards[i]
    
    print(severity)
    
    def caught(delay: int) -> bool:
        for i in range(max_guard + 1):
            if i in guards and (i + delay) % ((guards[i] - 1) * 2) == 0:
                return True
        return False
    
    print(next(delay for delay in count() if not caught(delay)))


# day13(TEST_INPUT)
(day13(INPUT))
