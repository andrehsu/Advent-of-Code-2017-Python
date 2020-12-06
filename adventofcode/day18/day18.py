from collections import defaultdict, deque
from typing import Deque, Dict, Iterable, List

INPUT = open('input.txt').read().splitlines()


def part1(input_: List[str]):
    registers: Dict[str, int] = defaultdict(int)
    
    def value(x: str) -> int:
        try:
            return int(x)
        except ValueError:
            return registers[x]
    
    snd = 0
    
    i = 0
    while 0 <= i < len(input_):
        line = input_[i]
        words = line.split()
        if words[0] == 'snd':
            snd = value(words[1])
        elif words[0] == 'set':
            registers[words[1]] = value(words[2])
        elif words[0] == 'add':
            registers[words[1]] += value(words[2])
        elif words[0] == 'mul':
            registers[words[1]] *= value(words[2])
        elif words[0] == 'mod':
            registers[words[1]] %= value(words[2])
        elif words[0] == 'rcv':
            if value(words[1]) != 0:
                print(snd)
                break
        
        if words[0] == 'jgz' and value(words[1]) > 0:
            i = i + value(words[2])
        else:
            i += 1


class Program:
    def __init__(self, code: List[str], p: int):
        self._registers = defaultdict(int, {'p': p})
        self._i = 0
        self._queue: Deque[int] = deque()
        self._send_count = 0
        self._code = code
    
    def _value(self, x: str) -> int:
        try:
            return int(x)
        except ValueError:
            return self._registers[x]
    
    def extend_queue(self, iterable: Iterable):
        self._queue.extend(iterable)
    
    def run_until_wait(self) -> List[int]:
        snds = []
        while 0 <= self._i < len(self._code):
            line = self._code[self._i]
            words = line.split()
            if words[0] == 'snd':
                self._send_count += 1
                snds.append(self._value(words[1]))
            elif words[0] == 'set':
                self._registers[words[1]] = self._value(words[2])
            elif words[0] == 'add':
                self._registers[words[1]] += self._value(words[2])
            elif words[0] == 'mul':
                self._registers[words[1]] *= self._value(words[2])
            elif words[0] == 'mod':
                self._registers[words[1]] %= self._value(words[2])
            elif words[0] == 'rcv':
                if self._queue:
                    v = self._queue.popleft()
                    self._registers[words[1]] = v
                else:
                    break
            
            if words[0] == 'jgz' and self._value(words[1]) > 0:
                self._i = self._i + self._value(words[2])
            else:
                self._i += 1
        
        return snds
    
    @property
    def empty_queue(self):
        return not self._queue
    
    @property
    def send_count(self):
        return self._send_count


def part2(input_: List[str]):
    program0 = Program(input_, 0)
    program1 = Program(input_, 1)
    
    while True:
        sends = program0.run_until_wait()
        program1.extend_queue(sends)
        
        sends = program1.run_until_wait()
        program0.extend_queue(sends)
        
        if program0.empty_queue and program1.empty_queue:
            break
    
    print(program1.send_count)


def day18(input_: List[str]):
    part1(input_)
    part2(input_)


if __name__ == '__main__':
    day18(INPUT)
