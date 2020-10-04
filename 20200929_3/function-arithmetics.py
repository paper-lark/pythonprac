from typing import Union, Callable, TypeVar

A = TypeVar('A')
R = TypeVar('R')
F = Union[Callable[[A], R], R]


def ADD(f: F, g: F) -> F:
    def result(value: A) -> R:
        v1 = f(value) if callable(f) else f
        v2 = g(value) if callable(g) else g
        return v1 + v2
    return result


def SUB(f: F, g: F) -> F:
    def result(value: A) -> R:
        v1 = f(value) if callable(f) else f
        v2 = g(value) if callable(g) else g
        return v1 - v2
    return result


def DIV(f: F, g: F) -> F:
    def result(value: A) -> R:
        v1 = f(value) if callable(f) else f
        v2 = g(value) if callable(g) else g
        return v1 / v2
    return result


def MUL(f: F, g: F) -> F:
    def result(value: A) -> R:
        v1 = f(value) if callable(f) else f
        v2 = g(value) if callable(g) else g
        return v1 * v2
    return result
