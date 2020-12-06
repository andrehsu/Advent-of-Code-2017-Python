from collections import Counter
from typing import List

INPUT = open('input.txt').read()


def dist(path: List[str]) -> int:
    moves = Counter(path)
    
    def replace_pair(d0: str, d1: str, replace: str = None):
        reduce_amount = min(moves[d0], moves[d1])
        moves[d0] -= reduce_amount
        moves[d1] -= reduce_amount
        if replace is not None:
            moves[replace] += reduce_amount
    
    last = sum(moves.values())
    while True:
        replace_pair('ne', 'nw', 'n')
        replace_pair('se', 'sw', 's')
        replace_pair('ne', 's', 'se')
        replace_pair('nw', 's', 'sw')
        replace_pair('se', 'n', 'ne')
        replace_pair('sw', 'n', 'nw')
        replace_pair('sw', 'ne')
        replace_pair('nw', 'se')
        replace_pair('n', 's')
        curr = sum(moves.values())
        if curr == last:
            return curr
        last = curr


def day11(inp: str):
    path = inp.split(',')
    
    print(dist(path))
    
    print(max(dist(path[:i]) for i in range(1, len(path) + 1)))


if __name__ == '__main__':
    print('SOLUTION:')
    day11(INPUT)
