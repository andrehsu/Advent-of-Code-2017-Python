from typing import List

from util import read_input

INPUT = read_input(5)


def day5(input_: List[str]):
    jumps = list(map(int, input_))
    
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
    
    part1(jumps)
    part2(jumps)


day5(INPUT)
