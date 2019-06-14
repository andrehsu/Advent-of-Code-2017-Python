from util import read_input

INPUT = read_input(9)[0]

TEST_INPUTS = [
    '{}',
    '{{{}}}',
    '{{},{}}',
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<!!>},{<!!>},{<!!>},{<!!>}}',
    '{{<a!>},{<a!>},{<a!>},{<ab>}}',
]


def day9(input_: str):
    i = iter(input_)
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


for TEST_INPUT in TEST_INPUTS:
    day9(TEST_INPUT)

day9(INPUT)
