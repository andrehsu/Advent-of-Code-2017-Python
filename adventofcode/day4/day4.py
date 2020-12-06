from collections import Counter
from itertools import combinations
from typing import List

INPUT = open('input.txt').read().splitlines()


def day4(inp: List[str]):
    phrases = list(map(str.split, inp))
    print(sum(len(p) == len(set(p)) for p in phrases))
    
    print(
        sum(
            all(Counter(a) != Counter(b)
                for a, b in combinations(p, 2))
            for p in phrases))


if __name__ == '__main__':
    day4(INPUT)
