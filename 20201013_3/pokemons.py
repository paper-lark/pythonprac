from collections import defaultdict
from functools import reduce
from sys import stdin
from typing import Dict, Set

if __name__ == '__main__':
    # Read people and their desks
    person_desks: Dict[str, Set[int]] = defaultdict(set)
    desk_cards: Dict[int, Set[str]] = defaultdict(set)

    for line in stdin:
        line = line.strip()
        if len(line) == 0:
            break
        pt1, pt2 = line.split(' / ')
        if pt1.isnumeric():
            # Desk card
            desk_cards[int(pt1)].add(pt2)
        else:
            # Person's desk
            person_desks[pt1].add(int(pt2))

    # Find distinct cards for each person
    person_cards_cnt: Dict[str, int] = {}
    for person, desks in person_desks.items():
        person_cards_cnt[person] = len(reduce(lambda a, b: a | b, map(lambda desk: desk_cards[desk], desks)))

    # Find top owners
    top = None
    for person, cnt in sorted(person_cards_cnt.items(), key=lambda x: (-x[1], x[0])):
        if top is not None and cnt != top:
            break
        top = cnt
        print(person)
