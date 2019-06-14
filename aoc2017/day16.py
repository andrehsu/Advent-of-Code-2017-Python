from typing import Dict, List, Tuple

from util import read_input

INPUT = read_input(16)[0]
TEST_INPUT = 's1,x3/4,pe/b'


def dance(programs: List[str], steps: List[str]):
    for step in steps:
        if step[0] == 's':
            x = int(step[1:])
            programs[:] = programs[-x:] + programs[:-x]
        elif step[0] == 'x':
            pos0, pos1 = map(int, step[1:].split('/'))
            programs[pos0], programs[pos1] = programs[pos1], programs[pos0]
        elif step[0] == 'p':
            name0, name1 = step[1:].split('/')
            pos0 = programs.index(name0)
            pos1 = programs.index(name1)
            programs[pos0], programs[pos1] = programs[pos1], programs[pos0]


def day16(input_: str, programs_num: int = 16):
    programs = [chr(i) for i in range(ord('a'), ord('a') + programs_num)]
    
    steps = input_.split(',')
    
    dance(programs, steps)
    
    print(''.join(programs))
    
    cycle = 0
    first_i = 0
    seen: Dict[Tuple[str, ...], int] = {}
    for i in range(1, 1_000_000_000):
        t = tuple(programs)
        if t in seen:
            cycle = i - seen[t]
            first_i = seen[t]
            break
        else:
            seen[t] = i
        dance(programs, steps)
    
    for _ in range((1_000_000_000 - first_i) % cycle):
        dance(programs, steps)
    
    print(''.join(programs))


day16(TEST_INPUT, 5)
day16(INPUT)
