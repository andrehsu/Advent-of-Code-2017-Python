from typing import List, Tuple

INPUT = open('input.txt').read().splitlines()


def move(d: str, r: int, c: int) -> Tuple[int, int]:
    if d == 'd':
        r += 1
    elif d == 'u':
        r -= 1
    elif d == 'l':
        c -= 1
    elif d == 'r':
        c += 1
    return r, c


def valid_path(path: List[List[str]], r: int, c: int) -> bool:
    try:
        return path[r][c] != ' '
    except IndexError:
        return False


def day19(input_: List[str]):
    path = [list(line) for line in input_]
    r = 0
    c = path[r].index('|')
    d = 'd'
    steps = 0
    
    letters: List[str] = []
    while True:
        symbol = path[r][c]
        
        if symbol == ' ':
            break
        
        steps += 1
        
        if symbol == '+':
            if d in ('l', 'r'):
                if valid_path(path, r - 1, c):
                    r = r - 1
                    d = 'u'
                    continue
                
                if valid_path(path, r + 1, c):
                    r = r + 1
                    d = 'd'
                    continue
            
            if d in ('u', 'd'):
                if valid_path(path, r, c + 1):
                    c = c + 1
                    d = 'r'
                    continue
                
                if valid_path(path, r, c - 1):
                    c = c - 1
                    d = 'l'
                    continue
        else:
            r, c = move(d, r, c)
            if symbol not in ('-', '|'):
                letters.append(symbol)
    
    print(''.join(letters))
    print(steps)


if __name__ == '__main__':
    day19(INPUT)
