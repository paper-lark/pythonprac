import re
from re import Pattern


def match_pattern(pattern: Pattern, s: str):
    named_groups = {}
    for name, index in pattern.groupindex.items():
        named_groups[index] = name
    match = pattern.search(s)
    if match:
        print(f'{match.start()}: {match.group()}')
        for i, value in enumerate(match.groups(), start=1):
            if value is not None and len(value) > 0:
                print(f'{i}/{match.start(i)}: {value}')

        for i, value in enumerate(match.groups(), start=1):
            if value is not None and len(value) > 0 and i in named_groups:
                print(f'{named_groups[i]}/{match.start(i)}: {value}')
    else:
        print('<NONE>')


def main():
    pattern = re.compile(input())
    line = input()
    while len(line) > 0:
        match_pattern(pattern, line)
        line = input()


if __name__ == '__main__':
    main()
