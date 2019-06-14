from typing import Tuple, Generator

INPUT = (703, 516)
TEST_INPUT = (65, 8921)


def gen(start: int, factor: int) -> Generator[int, None, None]:
    value = start
    while True:
        yield value
        value = (value * factor) % 2147483647


def day15(input_: Tuple[int, int]):
    a, b = input_
    gen_a = gen(a, 16807)
    gen_b = gen(b, 48271)
    
    matches = 0
    for _ in range(40_000_000):
        if bin(next(gen_a))[-16:] == bin(next(gen_b))[-16:]:
            matches += 1
    
    print(matches)
    
    gen_a = (i for i in gen(a, 16807) if i % 4 == 0)
    gen_b = (i for i in gen(b, 48271) if i % 8 == 0)
    matches = 0
    for _ in range(5_000_000):
        if bin(next(gen_a))[-16:] == bin(next(gen_b))[-16:]:
            matches += 1
    
    print(matches)


day15(TEST_INPUT)
day15(INPUT)
