from collections import Counter
from typing import List

from util import read_input

INPUT = read_input(11)[0]
TEST_INPUT = 'ne,ne,s,s'


def day11(input_: str):
    path = input_.split(',')
    
    def dist(path: List[str]) -> int:
        moves = Counter(path)
        
        def remove_pair(d0: str, d1: str, replace: str = None):
            reduce_amount = min(moves[d0], moves[d1])
            moves[d0] -= reduce_amount
            moves[d1] -= reduce_amount
            if replace is not None:
                moves[replace] += reduce_amount
        
        remove_pair('ne', 'nw', 'n')
        remove_pair('se', 'sw', 's')
        remove_pair('ne', 's', 'se')
        remove_pair('nw', 's', 'sw')
        remove_pair('se', 'n', 'ne')
        remove_pair('sw', 'n', 'nw')
        remove_pair('sw', 'ne')
        remove_pair('nw', 'se')
        remove_pair('n', 's')
        return sum(moves.values())
    
    print(dist(path))
    
    print(max(dist(path[:i]) for i in range(1, len(path) + 1)))


day11(TEST_INPUT)
day11(INPUT)
