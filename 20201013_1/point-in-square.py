from typing import Tuple
from random import random

Point = Tuple[float, float]


def randsquare(p1: Point, p2: Point) -> Point:
    center: Point = ((p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2)
    norm: Point = (-(p2[1] - p1[1]) / 2, (p2[0] - p1[0]) / 2)
    p3: Point = (center[0] + norm[0], center[1] + norm[1])
    p4: Point = (center[0] - norm[0], center[1] - norm[1])

    v1: Point = (p4[0] - p1[0], p4[1] - p1[1])
    v2: Point = (p3[0] - p1[0], p3[1] - p1[1])
    w1, w2 = random(), random()
    result: Point = (v1[0] * w1 + v2[0] * w2 + p1[0], v1[1] * w1 + v2[1] * w2 + p1[1])

    return result
