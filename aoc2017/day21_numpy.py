import numpy as np  # type: ignore

from util import read_input, test_case

INPUT = read_input(21)
TEST_INPUT = test_case("""
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""")


class PatternDict:
    
    def __init__(self):
        self.__rules = {}
    
    def __getitem__(self, key):
        return self.__rules[key.tobytes()]
    
    def __setitem__(self, key, value):
        self.__rules[key.tobytes()] = value


def day21(input_, iterations):
    rs = PatternDict()
    pattern = lambda s: np.array([[1 if i == '#' else 0 for i in line] for line in s.split('/')])
    for line in input_:
        a, b = map(pattern, line.split(' => '))
        rs[a] = b
        rs[np.rot90(a)] = b
        rs[np.fliplr(a)] = b
        rs[np.flipud(a)] = b
        rs[np.rot90(np.fliplr(a))] = b
        rs[np.rot90(np.flipud(a))] = b
    
    p = pattern('.#./..#/###')
    
    s_ = lambda i, f: slice(i * f, (i + 1) * f)
    
    for _ in range(iterations):
        if len(p) % 2 == 0:
            bl = 2
        elif len(p) % 3 == 0:
            bl = 3
        
        bsl = len(p) // bl
        bl1 = bl + 1
        p1 = np.full((bsl * bl1, bsl * bl1), 0)
        for i in range(bsl):
            for j in range(bsl):
                b = p[s_(i, bl), s_(j, bl)]
                b1 = rs[b]
                p1[s_(i, bl1), s_(j, bl1)] = b1
        p = p1
    
    print(p.sum())


day21(TEST_INPUT, 2)
day21(INPUT, 5)
day21(INPUT, 18)
