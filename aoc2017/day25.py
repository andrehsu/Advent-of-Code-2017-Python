from collections import defaultdict


def day25():
    t = defaultdict(int)
    state = 'A'
    i = 0

    for _ in range(12368930):
        if state == 'A':
            if t[i] == 0:
                t[i] = 1
                i += 1
                state = 'B'
            else:
                t[i] = 0
                i += 1
                state = 'C'
        elif state == 'B':
            if t[i] == 0:
                t[i] = 0
                i -= 1
                state = 'A'
            else:
                t[i] = 0
                i += 1
                state = 'D'
        elif state == 'C':
            if t[i] == 0:
                t[i] = 1
                i += 1
                state = 'D'
            else:
                t[i] = 1
                i += 1
                state = 'A'
        elif state == 'D':
            if t[i] == 0:
                t[i] = 1
                i -= 1
                state = 'E'
            else:
                t[i] = 0
                i -= 1
                state = 'D'
        elif state == 'E':
            if t[i] == 0:
                t[i] = 1
                i += 1
                state = 'F'
            else:
                t[i] = 1
                i -= 1
                state = 'B'
        else:
            if t[i] == 0:
                t[i] = 1
                i += 1
                state = 'A'
            else:
                t[i] = 1
                i += 1
                state = 'E'
    print(sum(t.values()))


day25()
