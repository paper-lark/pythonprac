from decimal import Decimal, getcontext
from typing import Generator


def fact_nk(n: int) -> Generator[Decimal, None, None]:
    """
    Calculates (nk)! where k=0…infinity
    """
    fact = Decimal(1)
    last_i = 0
    k = 0
    while True:
        if k != 0:
            for _ in range(0, n):
                last_i += 1
                fact *= last_i
        k += 1
        yield fact


def linear(c: Decimal, a: Decimal) -> Generator[Decimal, None, None]:
    """
    Calculates c + a*k where k=0…infinity
    """
    k = 0
    value = c
    while True:
        if k != 0:
            value += a
        k += 1
        yield value


def power(c: Decimal, a: Decimal) -> Generator[Decimal, None, None]:
    """
    Calculates c*(a**k) where k=0…infinity
    """
    k = 0
    value = c
    while True:
        if k != 0:
            value *= a
        k += 1
        yield value


def PiGen() -> Generator[Decimal, None, None]:
    # Read more: https://ru.wikipedia.org/wiki/Алгоритм_Чудновского
    getcontext().prec = 10001
    series_sum = Decimal(0)
    k = 0
    fact_6k = fact_nk(n=6)
    fact_3k = fact_nk(n=3)
    fact_k = fact_nk(n=1)
    linear_multiplier = linear(c=Decimal(13591409), a=Decimal(545140134))

    a = Decimal(640320) * Decimal(640320) * Decimal(640320)
    c = Decimal.sqrt(a)
    pow_divider = power(c=c, a=a)

    while True:
        elem = Decimal(-1) if k & 0x1 == 1 else Decimal(1)
        elem *= next(fact_6k)
        elem *= next(linear_multiplier)
        elem /= next(fact_3k)
        elem /= next(fact_k)**3
        elem /= next(pow_divider)

        series_sum += elem
        yield Decimal(1) / (series_sum * Decimal(12))
        k += 1
