from itertools import count
from typing import List, Tuple

INPUT = open('input.txt').read().splitlines()


def day13(inp: List[str]):
    def parse_line(line: str) -> Tuple[int, int]:
        a, b = (map(int, line.split(': ')))
        return a, b
    
    guards = {guard: depth for guard, depth in map(parse_line, inp)}
    max_guard = max(guards)
    
    severity = 0
    for i in range(max_guard + 1):
        if i in guards and i % ((guards[i] - 1) * 2) == 0:
            severity += i * guards[i]
    
    print(severity)
    
    def caught(delay: int) -> bool:
        for i in range(max_guard + 1):
            if i in guards and (i + delay) % ((guards[i] - 1) * 2) == 0:
                return True
        return False
    
    print(next(delay for delay in count() if not caught(delay)))


if __name__ == '__main__':
    (day13(INPUT))
