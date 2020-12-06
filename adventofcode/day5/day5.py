from typing import List

INPUT = open('input.txt').read().splitlines()


def day5(inp: List[str]):
    jumps = list(map(int, inp))
    part1(jumps)
    part2(jumps)


def part1(jumps: List[int]):
    jumps = jumps.copy()
    
    steps = 0
    i = 0
    while 0 <= i < len(jumps):
        jump = jumps[i]
        jumps[i] += 1
        
        i += jump
        
        steps += 1
    
    print(steps)


def part2(jumps: List[int]):
    jumps = jumps.copy()
    
    steps = 0
    i = 0
    while 0 <= i < len(jumps):
        jump = jumps[i]
        if jump >= 3:
            jumps[i] -= 1
        else:
            jumps[i] += 1
        
        i += jump
        
        steps += 1
    
    print(steps)


if __name__ == '__main__':
    day5(INPUT)
