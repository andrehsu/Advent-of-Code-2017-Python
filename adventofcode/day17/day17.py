import numba

INPUT = 371


@numba.njit
def wrap_len(len_: int, i: int) -> int:
    if i < 0:
        return wrap_len(len_, i + len_)
    
    return i % len_


@numba.njit
def day17(input_: int):
    buffer = [0]
    i = 0
    
    for value in range(1, 2017 + 1):
        i = wrap_len(len(buffer), i + input_ + 1)
        buffer.insert(i, value)
    
    print(buffer[buffer.index(2017) + 1])
    
    i = 0
    len_ = 1
    value = 0
    for j in range(1, 50_000_000 + 1):
        i = wrap_len(len_, i + input_)
        len_ += 1
        i = wrap_len(len_, i + 1)
        if i == 1:
            value = j
    
    print(value)


if __name__ == '__main__':
    day17(INPUT)
