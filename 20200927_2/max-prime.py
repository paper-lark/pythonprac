from math import sqrt, floor


def is_prime(x: int) -> bool:
    for y in range(2, floor(sqrt(x))):
        if x % y == 0:
            return False
    return True


def find_prime(limit: int) -> int:
    # NOTE: since limit ≥ 2, prime always exists
    for x in range(limit, 0, -1):
        if is_prime(x):
            return x


if __name__ == '__main__':
    lim = int(input())
    if lim < 2:
        raise ValueError(f'Limit must be greater than 1 but got {lim}')
    prime = find_prime(lim)
    print(prime)
