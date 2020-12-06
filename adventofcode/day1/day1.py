INPUT = open('input.txt').read()


def day1(inp: str) -> None:
    digits = list(map(int, inp))
    
    sum_ = 0
    for i in range(len(digits) - 1):
        a, b = digits[i:i + 2]
        if a == b:
            sum_ += a
    
    if digits[-1] == digits[0]:
        sum_ += digits[-1]
    
    print(sum_)
    
    sum_ = 0
    digits_len = len(digits)
    for i in range(digits_len):
        a = digits[i]
        b = digits[(i + digits_len // 2) % digits_len]
        if a == b:
            sum_ += a
    
    print(sum_)


if __name__ == '__main__':
    day1(INPUT)
