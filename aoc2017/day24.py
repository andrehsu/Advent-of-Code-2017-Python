from typing import Generator, List, Set, Tuple

from util import read_input, test_case

Part = Tuple[int, int]

INPUT = read_input(24)
TEST_INPUT = test_case('''
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
''')


def get_combinations(starts_with: int, parts: Set[Part]
                    ) -> Generator[Tuple[int, ...], None, None]:
    yield tuple()
    for part in parts:
        a, b = part
        if b == starts_with:
            a, b = b, a
        if a == starts_with:
            new_parts = parts.copy()
            new_parts.remove(part)
            for combination in get_combinations(b, new_parts):
                yield part + combination


def day24(input_: List[str]):
    parts = set()
    for line in input_:
        a, b = map(int, line.split('/'))
        parts.add((a, b))

    combinations = list(get_combinations(0, parts))
    print(max(sum(comb) for comb in combinations))

    max_len = max(len(comb) for comb in combinations)
    print(max(sum(comb) for comb in combinations if len(comb) == max_len))


day24(TEST_INPUT)
day24(INPUT)
