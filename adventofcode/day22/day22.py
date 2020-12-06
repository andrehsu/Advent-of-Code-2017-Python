from collections import defaultdict
from typing import Dict, List, Tuple


Coord = Tuple[int, int]

INPUT = open('input.txt').read().splitlines()


def part1(input_: List[str]):
    plane: Dict[Coord, bool] = defaultdict(bool)
    for r, line in enumerate(input_):
        for c, i in enumerate(line):
            plane[r, c] = i == '#'
    
    r = len(input_) // 2
    c = len(input_[r]) // 2
    d = 0
    
    infections = 0
    for _ in range(10_000):
        infected = plane[(r, c)]
        if infected:
            d = (d + 1) % 4
            plane[(r, c)] = False
        else:
            d = (d + 3) % 4
            plane[(r, c)] = True
            infections += 1
        
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        elif d == 3:
            c -= 1
    
    print(infections)


def part2(input_: List[str]):
    plane: Dict[Coord, str] = defaultdict(lambda: 'C')
    for r, row in enumerate(input_):
        for c, i in enumerate(row):
            if i == '#':
                plane[(r, c)] = 'I'
    
    r = len(input_) // 2
    c = len(input_[r]) // 2
    d = 0
    
    infections = 0
    
    for _ in range(10_000_000):
        state = plane[(r, c)]
        if state == 'C':
            d = (d + 3) % 4
            state = 'W'
        elif state == 'W':
            infections += 1
            state = 'I'
        elif state == 'I':
            d = (d + 1) % 4
            state = 'F'
        elif state == 'F':
            d = (d + 2) % 4
            state = 'C'
        
        plane[(r, c)] = state
        
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        elif d == 3:
            c -= 1
    
    print(infections)


def day22(input_: List[str]):
    part1(input_)
    part2(input_)


if __name__ == '__main__':
    day22(INPUT)
