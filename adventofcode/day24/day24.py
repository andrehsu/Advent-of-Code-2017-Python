from typing import Generator, List, Set, Tuple


Part = Tuple[int, int]

INPUT = open('input.txt').read().splitlines()


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


if __name__ == '__main__':
    day24(INPUT)
