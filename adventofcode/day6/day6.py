from typing import Set, Tuple

INPUT = open('input.txt').read()
TEST_INPUT = '0 2 7 0'


def day6(inp: str):
    banks = list(map(int, inp.split()))
    
    seen: Set[Tuple[int, ...]] = set()
    steps = 0
    first_seen = None
    while True:
        if tuple(banks) in seen:
            if first_seen is None:
                first_seen = steps
                repeat_config = tuple(banks)
            elif repeat_config == tuple(banks):
                break
        else:
            seen.add(tuple(banks))
        
        i = max(range(len(banks)), key=lambda k: banks[k])
        blocks = banks[i]
        banks[i] = 0
        
        for _ in range(blocks):
            i = (i + 1) % len(banks)
            banks[i] += 1
        
        steps += 1
    
    print(first_seen)
    print(steps - first_seen)


if __name__ == '__main__':
    day6(TEST_INPUT)
    day6(INPUT)
