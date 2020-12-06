from collections import Counter
from typing import List, Union, Tuple

INPUT = open('input.txt').read().splitlines()
TEST = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""[1:-1].splitlines()


def day7(inp: List[str]):
    def parse_line(line: str):
        words = line.replace(',', '').split()
        name = words[0]
        value = int(words[1][1:-1])
        children = words[3:]
        
        return name, (value, children)
    
    programs = dict(map(parse_line, inp))
    for name in programs:
        if all(name not in children for (_, children) in programs.values()):
            root = name
            break
    
    print(root)
    
    def weight(name: str) -> int:
        value, children = programs[name]
        return value + sum(weight(child) for child in children)
    
    def balanced_weight(name: str) -> Union[int, Tuple[int]]:
        _, children = programs[name]
        
        weights = [weight(child) for child in children]
        
        if len(set(weights)) <= 1:
            return (sum(weights),)
        
        c = Counter(weights).most_common()
        normal, _ = c[0]
        off, _ = c[-1]
        for child in children:
            if weight(child) == off:
                ret = balanced_weight(child)
                
                if isinstance(ret, tuple):
                    return normal - ret[0]
                
                return ret
        
        raise Exception()
    
    print(balanced_weight(root))


if __name__ == '__main__':
    day7(TEST)
    day7(INPUT)
