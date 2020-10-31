from enum import Enum
from functools import reduce
from typing import List, Union, Tuple, Dict


class Spiral:
    _Sequence = Tuple[str, int]

    class _Direction(Enum):
        Left = 0
        Right = 1
        Top = 2
        Down = 3

        def step(self, x: int, y: int) -> Tuple[int, int]:
            if self == Spiral._Direction.Right:
                return x + 1, y
            if self == Spiral._Direction.Top:
                return x, y - 1
            if self == Spiral._Direction.Left:
                return x - 1, y
            if self == Spiral._Direction.Down:
                return x, y + 1

        def turn(self) -> 'Spiral._Direction':
            if self == Spiral._Direction.Right:
                return Spiral._Direction.Top
            if self == Spiral._Direction.Top:
                return Spiral._Direction.Left
            if self == Spiral._Direction.Left:
                return Spiral._Direction.Down
            if self == Spiral._Direction.Down:
                return Spiral._Direction.Right

    def __init__(self, text: str):
        self._seq: List[str] = []
        self._letters: Dict[str, int] = {}

        current: Union[None, str] = None
        for letter in text:
            if current is None or letter != current:
                current = letter
                self._seq.append(current)
                self._letters[current] = 1
            else:
                self._letters[current] += 1

    def __add__(self, other: 'Spiral'):
        obj = Spiral('')
        obj._seq = self._seq.copy()
        obj._letters = self._letters.copy()
        for k, v in other._letters.items():
            if k in obj._letters:
                obj._letters[k] += v
            else:
                obj._seq.append(k)
                obj._letters[k] = v
        return obj

    def __sub__(self, other: 'Spiral'):
        obj = Spiral('')
        for k, v in self._letters.items():
            cnt = v - other._letters[k] if k in other._letters else v
            if cnt > 0:
                obj._letters[k] = cnt
        obj._seq = list(filter(lambda letter: letter in obj._letters, self._seq))
        return obj

    def __mul__(self, m: int):
        obj = Spiral('')
        obj._seq = self._seq.copy()
        for k, v in self._letters.items():
            obj._letters[k] = v * m
        return obj

    def __iter__(self):
        for letter in self._seq:
            for _ in range(self._letters[letter]):
                yield letter

    def __len__(self):
        return reduce(lambda x, y: x + y, self._letters.values(), 0)

    def __str__(self):
        width, height, x, y = self._infer_spiral_params()
        field: List[List[str]] = [[' '] * width for _ in range(height)]
        direction = Spiral._Direction.Right
        i = 0
        to_walk = 1
        for s in self:
            field[y][x] = s
            x, y = direction.step(x, y)
            to_walk -= 1
            if to_walk == 0:
                direction = direction.turn()
                i += 1
                to_walk = i + 1

        return '\n'.join(map(lambda x: ''.join(x), field))

    def _infer_spiral_params(self) -> Tuple[int, int, int, int]:
        width = 1
        height = 1
        x0 = 0
        y0 = 0
        left = len(self)
        i = 0
        while left > 0:
            path_len = i + 1 if i > 1 else 2
            sub = min(left, path_len)
            if i == 0:
                width = max(sub, width)
            elif i % 2 == 0:
                if i % 4 == 2:
                    x0, y0 = x0 + max(0, sub + 1 - width), y0
                width = max(sub + 1, width)
            else:
                if i % 4 == 1:
                    x0, y0 = x0, y0 + max(0, sub + 1 - height)
                height = max(sub + 1, height)
            i += 1
            left -= sub

        return width, height, x0, y0
