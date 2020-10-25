from typing import Tuple, Generator

Point = Tuple[int, int]
Direction = int  # 0 — east, 1 — north, 2 — west, 3 — south


def get_direction_vector(direction: Direction) -> Point:
    return {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 0),
        3: (0, -1),
    }[direction]


def turtle(coord: Point, direction: Direction) -> Generator[Point, Direction, None]:
    position: Point = coord
    direction: Direction = direction

    while True:
        action = yield position
        if action == 'r':
            direction = (direction + 3) % 4
        elif action == 'l':
            direction = (direction + 1) % 4
        elif action == 'f':
            delta = get_direction_vector(direction)
            position = position[0] + delta[0], position[1] + delta[1]
        else:
            raise ValueError(f'unsupported turtle command "{action}"')
