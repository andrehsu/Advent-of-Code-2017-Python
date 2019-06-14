from util import read_input
from collections import defaultdict

INPUT = read_input(3)[0]
TEST_INPUT = '1024'


def day3(input_: str):
    port = int(input_)
    
    d = 0
    min_x = 0
    max_x = 1
    min_y = 0
    max_y = 0
    x = y = 0
    
    grid = defaultdict(lambda: 0, {(0, 0): 1})
    
    part2 = None
    for _ in range(2, port + 1):
        if d == 0 and x == max_x:
            d = 1
            max_y += 1
        elif d == 1 and y == max_y:
            d = 2
            min_x -= 1
        elif d == 2 and x == min_x:
            d = 3
            min_y -= 1
        elif d == 3 and y == min_y:
            d = 0
            max_x += 1
        
        if d == 0:
            x += 1
        elif d == 1:
            y += 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y -= 1
        
        value = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                value += grid[(i, j)]
        grid[(x, y)] = value

        if part2 is None and value > port:
            part2 = value
    
    print(abs(x) + abs(y))
    print(part2)


day3(TEST_INPUT)
day3(INPUT)
