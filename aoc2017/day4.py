from collections import Counter
from itertools import combinations
from typing import List

from util import read_input

INPUT = read_input(4)


def day4(input_: List[str]):
    phrases = list(map(str.split, input_))
    print(sum(len(p) == len(set(p)) for p in phrases))
    
    print(
        sum(
            all(Counter(a) != Counter(b)
                for a, b in combinations(p, 2))
            for p in phrases))


day4(INPUT)
