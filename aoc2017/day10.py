from functools import reduce
from operator import xor
from typing import List, Sized, Tuple

from util import read_input

INPUT = read_input(10)[0]
TEST_INPUT = '3, 4, 1, 5'


def wrap_len(list_like: Sized, i: int, inc: int = 1) -> int:
    return (i + inc) % len(list_like)


def knot_hash_round(lengths: List[int],
                    string: List[int],
                    i: int = 0,
                    skip_size: int = 0) -> Tuple[List[int], int, int]:
    string = string.copy()
    
    for length in lengths:
        if length <= len(string):
            section = []
            j = i
            for _ in range(length):
                section.append(string[j])
                j = wrap_len(string, j)
            
            section.reverse()
            
            j = i
            for s in section:
                string[j] = s
                j = wrap_len(string, j)
            
            i = wrap_len(string, i, length + skip_size)
            skip_size += 1
    
    return string, i, skip_size


def part1(input_: str, string_len: int = 256):
    lengths = list(map(int, input_.split(',')))
    string = list(range(string_len))
    
    string, *_ = knot_hash_round(lengths, string)
    print(string[0] * string[1])


def part2(input_: str):
    lengths = list(map(ord, input_)) + [17, 31, 73, 47, 23]
    string = list(range(256))
    
    i = skip_size = 0
    for _ in range(64):
        string, i, skip_size = knot_hash_round(lengths, string, i, skip_size)
    
    dense_hash = []
    for i in range(16):
        dense_hash.append(reduce(xor, string[i * 16:(i + 1) * 16]))
    
    print(''.join(hex(i)[2:].rjust(2, '0') for i in dense_hash))


part1(TEST_INPUT, 5)
part1(INPUT)

part2('')
part2(INPUT)
