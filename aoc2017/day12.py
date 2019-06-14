import re
from collections import defaultdict, deque
from typing import Dict, List, Set

from util import read_input, test_case

INPUT = read_input(12)
TEST_INPUT = test_case("""
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""")


def day12(input_: List[str]):
    pipes: Dict[int, Set[int]] = defaultdict(set)
    for line in input_:
        a, *bs = map(int, re.findall(r'\d+', line))
        for b in bs:
            pipes[a].add(b)
            pipes[b].add(a)
    
    count = 0
    queue = deque([0])
    seen: Set[int] = set()
    
    while queue:
        node = queue.popleft()
        if node not in seen:
            seen.add(node)
            queue.extend(pipes[node])
            count += 1
    
    print(count)
    
    groups = 0
    while pipes:
        queue = deque([next(iter(pipes))])
        seen = set()
        while queue:
            node = queue.popleft()
            if node not in seen:
                seen.add(node)
                queue.extend(pipes[node])
                pipes = {
                    k: {i for i in v if i != node
                       } for k, v in pipes.items() if k != node
                }
        groups += 1
    
    print(groups)


day12(TEST_INPUT)
day12(INPUT)
