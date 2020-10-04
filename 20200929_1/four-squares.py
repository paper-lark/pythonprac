from math import sqrt, ceil
from typing import List


if __name__ == '__main__':
    result: List[str] = []
    n = int(input())
    if n < 1:
        raise ValueError(f'Expected n ≥ 1 but got {n}')
    lim = ceil(sqrt(n))
    squares: List[int] = []
    for i in range(0, lim+1):
        squares.append(i*i)

    for n1 in range(lim, -1, -1):
        r1 = n - squares[n1]
        if r1 >= 0:
            for n2 in range(n1, -1, -1):
                r2 = r1 - squares[n2]
                if r2 >= 0:
                    for n3 in range(n2, -1, -1):
                        r3 = r2 - squares[n3]
                        if r3 >= 0:
                            n4 = int(sqrt(r3))
                            if r3 == squares[n4] and n4 <= n3:
                                result.append(f'{n1} {n2} {n3} {n4}')

    for line in reversed(result):
        print(line)
