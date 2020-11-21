from collections import deque
from typing import List, Optional, Dict, Tuple
import re


class Linearization:
    def __init__(self, cls: List[str]):
        self.__l = deque(cls)
        self.__d = {}
        for c in cls:
            self.__d[c] = True

    def __len__(self) -> int:
        return len(self.__l)

    def contains(self, cls: str) -> bool:
        return cls in self.__d

    def delete_first(self, cls):
        if len(self.__l) == 0 or cls != self.__l[0]:
            return
        self.__l.popleft()
        del self.__d[cls]

    def get_first(self) -> str:
        return self.__l[0]


def merge(classname: str, superclasses: List[List[str]]) -> List[str]:
    result: List[str] = [classname]
    if len(superclasses) == 0:
        return result
    lins: Dict[str, Linearization] = {
        classname: Linearization(list(map(lambda l: l[0], superclasses)))}
    for s in superclasses:
        lins[s[0]] = Linearization(s)

    def is_candidate_valid(cls: str) -> bool:
        for o in lins.values():
            if o.contains(cls) and o.get_first() != cls:
                return False
        return True

    def find_next_class() -> Optional[str]:
        for current in lins.values():
            candidate_class = current.get_first()
            if is_candidate_valid(candidate_class):
                return candidate_class
        return None

    while len(lins) > 0:
        selected_class = find_next_class()
        if selected_class is None:
            raise ValueError(f'Cannot merge linearizations for class {classname}')
        result.append(selected_class)
        to_remove = []
        for key, other in lins.items():
            other.delete_first(selected_class)
            if len(other) == 0:
                to_remove.append(key)
        for key in to_remove:
            del lins[key]

    return result


def main():
    class_re = re.compile(r'class (\w+)(\((.+)\)|):')
    linearizations: Dict[str, List[str]] = {}

    try:
        line = input()
        while line:
            match = class_re.match(line)
            if match:
                groups = match.groups()
                cls = groups[0]
                superclasses = list(map(lambda s: s.strip(), groups[2].split(','))) \
                    if groups[2] is not None else []
                lin = merge(cls, superclasses=list(map(lambda dep: linearizations[dep], superclasses)))
                linearizations[cls] = lin
            line = input()
    except ValueError as e:
        print(e)
        print('No')
    except EOFError:
        print('Yes')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
