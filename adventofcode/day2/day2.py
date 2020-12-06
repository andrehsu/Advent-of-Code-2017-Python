from itertools import combinations
from typing import List

INPUT = open('input.txt').read().splitlines()
TEST_1 = """
5 1 9 5
7 5 3
2 4 6 8
"""[1:-1].splitlines()
TEST_2 = """
5 9 2 8
9 4 7 3
3 8 6 5
"""[1:-1].splitlines()


def day2(inp: List[str]):
    def parse_line(line: str) -> List[int]:
        return list(map(int, line.split()))
    
    table = list(map(parse_line, inp))
    
    print(sum(max(l) - min(l) for l in table))
    
    sum_ = 0
    for row in table:
        for p in combinations(row, 2):
            a = max(p)
            b = min(p)
            if a % b == 0:
                sum_ += a // b
    
    print(sum_)


if __name__ == '__main__':
    day2(TEST_1)
    day2(TEST_2)
    day2(INPUT)
