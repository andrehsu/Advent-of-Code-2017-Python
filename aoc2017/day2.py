from itertools import combinations
from typing import List

from util import test_case, read_input

INPUT = read_input(2)
TEST_INPUT = test_case("""
5 1 9 5
7 5 3
2 4 6 8
""")
TEST_INPUT_1 = test_case("""
5 9 2 8
9 4 7 3
3 8 6 5
""")


def day2(input_: List[str]):
    
    def parse_line(line: str) -> List[int]:
        return list(map(int, line.split()))
    
    table = list(map(parse_line, input_))
    
    print(sum(max(l) - min(l) for l in table))
    
    sum_ = 0
    for row in table:
        for p in combinations(row, 2):
            a = max(p)
            b = min(p)
            if a % b == 0:
                sum_ += a // b
    
    print(sum_)


day2(TEST_INPUT)

day2(TEST_INPUT_1)
day2(INPUT)
