from typing import Iterable, Generator, List


def YinYang(*args: Iterable[int]) -> Generator[int, None, None]:
    odd: List[int] = []
    for it in args:
        for elem in it:
            if elem & 0x1 == 0:
                yield elem
            else:
                odd.append(elem)
    for elem in odd:
        yield elem
