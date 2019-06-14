import re
from collections import defaultdict
from typing import Dict, List, Tuple

from dataclasses import dataclass
from util import read_input

Vector = Tuple[int, int, int]

INPUT = read_input(20)


def vector(str_: str) -> Vector:
    x, y, z = map(int, re.findall(r'-?\d+', str_))
    return x, y, z


@dataclass
class Particle:
    _id_: int
    _p: Vector
    _v: Vector
    _a: Vector
    
    def move(self):
        px, py, pz = self._p
        vx, vy, vz = self._v
        ax, ay, az = self._a
        vx += ax
        vy += ay
        vz += az
        px += vx
        py += vy
        pz += vz
        self._v = (vx, vy, vz)
        self._p = (px, py, pz)
    
    @property
    def id(self) -> int:
        return self._id_
    
    @property
    def position(self) -> Vector:
        return self._p
    
    @property
    def dist(self):
        x, y, z = self._p
        return abs(x) + abs(y) + abs(z)
    
    @classmethod
    def from_line(cls, id_: int, line: str) -> 'Particle':
        p, v, a = map(vector, line.split())
        return cls(id_, p, v, a)


def day20(input_: List[str]):
    particles = [Particle.from_line(i, line) for i, line in enumerate(input_)]
    particles_col = particles.copy()
    
    for _ in range(1_000):
        for particle in particles:
            particle.move()
        
        particles_pos: Dict[Vector, List[Particle]] = defaultdict(list)
        for particle in particles_col:
            particles_pos[particle.position].append(particle)
        
        particles_col = [
            particle for v in particles_pos.values() if not len(v) > 1
            for particle in v
        ]
    
    print(min(particles, key=Particle.dist.fget))  # type: ignore
    print(len(particles_col))


day20(INPUT)
