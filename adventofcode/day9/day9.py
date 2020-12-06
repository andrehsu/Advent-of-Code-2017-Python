INPUT = open('input.txt').read()

TEST = [
    '{}',
    '{{{}}}',
    '{{},{}}',
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<!!>},{<!!>},{<!!>},{<!!>}}',
    '{{<a!>},{<a!>},{<a!>},{<ab>}}',
]


def day9(inp: str):
    i = iter(inp)
    sum_ = 0
    level = 0
    count = 0
    while True:
        c = next(i)
        
        if c == '{':
            level += 1
        elif c == '<':
            while True:
                garbage_c = next(i)
                if garbage_c == '!':
                    next(i)
                elif garbage_c == '>':
                    break
                else:
                    count += 1
        if c == '}':
            sum_ += level
            level -= 1
        
        if level == 0:
            break
    
    print(sum_)
    print(count)


if __name__ == '__main__':
    for case in TEST:
        day9(case)
    
    print('SOLUTION: ')
    day9(INPUT)
