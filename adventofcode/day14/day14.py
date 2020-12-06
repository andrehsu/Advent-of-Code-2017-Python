from collections import deque
from functools import reduce
from operator import xor
from typing import List, Sized, Tuple

INPUT = 'ugkiagan'


def wrap_len(sized: Sized, i: int) -> int:
    if i < 0:
        return wrap_len(sized, i + len(sized))
    return (i) % len(sized)


def knot_hash_round(lengths: List[int],
                    string: List[int],
                    i: int = 0,
                    skip_size: int = 0) -> Tuple[List[int], int, int]:
    string = string.copy()
    
    for length in lengths:
        if length <= len(string):
            for j in range(length // 2):
                a = wrap_len(string, i + j)
                b = wrap_len(string, i + (length - 1 - j))
                string[a], string[b] = string[b], string[a]
            
            i = wrap_len(string, i + length + skip_size)
            skip_size += 1
    
    return string, i, skip_size


def knot_hash(inp: str) -> str:
    lengths = list(map(ord, inp)) + [17, 31, 73, 47, 23]
    string = list(range(256))
    
    i = skip_size = 0
    for _ in range(64):
        string, i, skip_size = knot_hash_round(lengths, string, i, skip_size)
    
    dense_hash = []
    for i in range(16):
        dense_hash.append(reduce(xor, string[i * 16:(i + 1) * 16]))
    
    return ''.join(hex(i)[2:].rjust(2, '0') for i in dense_hash)


def hex_to_bin(hex_: str) -> str:
    return bin(int(hex_, 16))[2:]


def day14(inp: str):
    mem: List[List[bool]] = [[] for _ in range(128)]
    
    for r in range(128):
        row_hash = knot_hash(f'{inp}-{r}')
        for b in hex_to_bin(row_hash).rjust(128, '0'):
            mem[r].append(b == '1')
    
    count = sum(i for row in mem for i in row)
    
    print(count)
    
    def remove_adjacent(x: int, y: int):
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            if 0 <= x < 128 and 0 <= y < 128 and mem[x][y]:
                mem[x][y] = False
                for i in range(x - 1, x + 2):
                    queue.append((i, y))
                for j in range(y - 1, y + 2):
                    queue.append((x, j))
    
    groups = 0
    for x in range(128):
        for y in range(128):
            if mem[x][y]:
                remove_adjacent(x, y)
                groups += 1
    
    print(groups)


if __name__ == '__main__':
    day14(INPUT)
