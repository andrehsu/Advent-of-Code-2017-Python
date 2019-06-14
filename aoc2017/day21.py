from typing import Dict, List, Tuple

from util import empty_list, read_input, test_case

INPUT = read_input(21)
TEST_INPUT = test_case("""
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""")

Pattern = Tuple[Tuple[str, ...], ...]
MutablePattern = List[List[str]]


class Rules:

    def __init__(self, rules: Dict[Pattern, Pattern]):
        self.__rules = rules

    def __getitem__(self, key: MutablePattern):
        return self.__rules[self.frozen(key)]

    @staticmethod
    def pattern(str_: str) -> MutablePattern:
        return [list(line) for line in str_.split('/')]

    @staticmethod
    def frozen(pattern: MutablePattern) -> Pattern:
        return tuple(tuple(row) for row in pattern)

    @staticmethod
    def unfrozen(pattern: Pattern) -> MutablePattern:
        return [list(row) for row in pattern]

    @staticmethod
    def flip_x(pattern: Pattern) -> Pattern:
        ret = Rules.unfrozen(pattern)
        for i in range(len(pattern) // 2):
            ret[i], ret[-i - 1] = ret[-i - 1], ret[i]
        return Rules.frozen(ret)

    @staticmethod
    def flip_y(pattern: Pattern) -> Pattern:
        ret = Rules.unfrozen(pattern)
        for row in ret:
            for c in range(len(ret) // 2):
                row[c], row[-c - 1] = row[-c - 1], row[c]
        return Rules.frozen(ret)

    @staticmethod
    def transpose(pattern: Pattern) -> Pattern:
        ret = Rules.unfrozen(pattern)
        for r in range(len(ret)):
            for c in range(len(ret)):  # pylint: disable=consider-using-enumerate
                ret[c][r] = pattern[r][c]
        return Rules.frozen(ret)

    @staticmethod
    def rotate(pattern: Pattern) -> Pattern:
        ret = Rules.flip_y(Rules.transpose(pattern))
        return ret

    @classmethod
    def from_input(cls, input_: List[str]) -> 'Rules':
        rules: Dict[Pattern, Pattern] = {}
        for line in input_:
            a, b = map(Rules.frozen, map(Rules.pattern, line.split(' => ')))
            rules[a] = b
            rules[Rules.flip_x(a)] = b
            rules[Rules.flip_y(a)] = b
            rules[Rules.rotate(a)] = b
            rules[Rules.rotate(Rules.rotate(a))] = b
            rules[Rules.rotate(Rules.rotate(Rules.rotate(a)))] = b
            rules[Rules.rotate(Rules.flip_x(a))] = b
            rules[Rules.rotate(Rules.flip_y(a))] = b

        return cls(rules)


def expand(rules: Rules, pattern: MutablePattern,
           block_size: int) -> MutablePattern:
    new_block_size = block_size + 1
    blocks_len = len(pattern) // block_size
    new_pattern = empty_list((new_block_size * blocks_len,
                              new_block_size * blocks_len))
    for blocks_i in range(blocks_len):
        for blocks_j in range(blocks_len):
            block = []
            for i in range(blocks_i * block_size, (blocks_i + 1) * block_size):
                row: List[str] = []
                block.append(row)
                for j in range(blocks_j * block_size,
                               (blocks_j + 1) * block_size):
                    row.append(pattern[i][j])
            new_block = iter(rules[block])
            for i in range(blocks_i * new_block_size,
                           (blocks_i + 1) * new_block_size):
                new_row = iter(next(new_block))
                for j in range(blocks_j * new_block_size,
                               (blocks_j + 1) * new_block_size):
                    new_pattern[i][j] = next(new_row)

    return new_pattern


def day21(input_: List[str], iterations: int = 5):
    rules = Rules.from_input(input_)
    pattern = Rules.pattern('.#./..#/###')

    for _ in range(iterations):
        if len(pattern) % 2 == 0:
            pattern = expand(rules, pattern, 2)
        elif len(pattern) % 3 == 0:
            pattern = expand(rules, pattern, 3)

    print(sum(sum(i == '#' for i in row) for row in pattern))


day21(TEST_INPUT, 2)
day21(INPUT)
day21(INPUT, 18)
