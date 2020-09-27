import re


def does_match_exist(x: str, y: str) -> bool:
    if len(y) == 0:
        return True
    if len(y) == 1:
        return x.find(y) != -1
    for first in map(lambda m: m.start(), re.finditer(y[0], x)):
        for second in map(lambda m: m.start(), re.finditer(y[1], x[first+1:])):
            start = first
            dist = second + 1
            if y == x[start::dist][:len(y)]:
                return True
    return False


if __name__ == '__main__':
    xs = input()
    ys = input()
    ok = does_match_exist(xs, ys)
    print('YES' if ok else 'NO')

