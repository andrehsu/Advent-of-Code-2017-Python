from collections import defaultdict
from typing import Dict, List

INPUT = open('input.txt').read().splitlines()


def part1(input_: List[str]):
    registers: Dict[str, int] = defaultdict(int)

    def value(x):
        try:
            return int(x)
        except ValueError:
            return registers[x]

    mul_count = 0

    i = 0
    while 0 <= i < len(input_):
        line = input_[i]
        words = line.split()

        if words[0] == 'set':
            registers[words[1]] = value(words[2])
        elif words[0] == 'sub':
            registers[words[1]] -= value(words[2])
        elif words[0] == 'mul':
            registers[words[1]] *= value(words[2])
            mul_count += 1

        if words[0] == 'jnz' and value(words[1]) != 0:
            i += value(words[2])
        else:
            i += 1

    print(mul_count)


def part2(input_: List[str]):
    b = c = int(input_[0].split()[2])
    b = b * 100 + 100_000
    c = b + 17000
    h = 0

    g = 2
    while g != 0:
        f = 1
        d = 2
        while d * d < b:
            if b % d == 0:
                f = 0
            d += 1
        if f == 0:
            h += 1

        g = b - c
        b += 17

    print(h)


def day23(input_: List[str]):
    part1(input_)
    part2(input_)


if __name__ == '__main__':
    day23(INPUT)
