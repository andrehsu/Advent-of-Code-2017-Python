import numba

INPUT = (116, 299)
TEST = (65, 8921)


@numba.njit
def gen(start: int, factor: int, multiple_of: int = 1):
    value = start
    while True:
        value *= factor
        value %= 2147483647
        if value % multiple_of == 0:
            yield value


def day15(input_):
    a, b = input_
    gen_a = gen(a, 16807)
    gen_b = gen(b, 48271)
    
    matches = 0
    for _ in range(40_000_000):
        if (next(gen_a) & 65535) == (next(gen_b) & 65535):
            matches += 1
    
    print(matches)
    
    matches = 0
    
    gen_a = gen(a, 16807, 4)
    gen_b = gen(b, 48271, 8)
    
    for _ in range(5_000_000):
        if (next(gen_a) & 65535) == (next(gen_b) & 65535):
            matches += 1
    
    print(matches)


if __name__ == '__main__':
    day15(INPUT)
