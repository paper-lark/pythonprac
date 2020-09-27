from math import floor, ceil


def is_sum_of_cubes(n: int) -> bool:
    x_lim = ceil((n / 2) ** (1 / 3))
    for x in range(1, x_lim+1):
        x_cube = x**3
        y_appx = (n - x_cube) ** (1. / 3)
        for y in [ceil(y_appx), floor(y_appx)]:
            y_cube = y**3
            if y_cube + x_cube == n:
                return True
    return False


if __name__ == '__main__':
    num = int(input())
    if num < 2:
        raise ValueError(f'Number must be natural but got {num}')
    print('YES' if is_sum_of_cubes(num) else 'NO')
