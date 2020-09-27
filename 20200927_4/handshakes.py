from typing import List, Set, Dict


if __name__ == '__main__':
    group_to_user: Dict[int, List[int]] = {}
    user_to_group: Dict[int, List[int]] = {}

    # read groups and users
    line = input()
    group_id = 0
    while len(line) > 0:
        members = list(map(lambda y: int(y), filter(lambda x: len(x) > 0, line.split(','))))
        group_to_user[group_id] = members
        for mem in members:
            if mem in user_to_group:
                user_to_group[mem].append(group_id)
            else:
                user_to_group[mem] = [group_id]
        group_id += 1
        line = input()

    if len(group_to_user) < 2:
        print('YES')
        exit(0)

    # run wave algorithm
    connected: Set[int] = set()
    used_users: Set[int] = set()
    queue: List[int] = []
    connected.add(0)
    for user in group_to_user[0]:
        used_users.add(user)
    queue += group_to_user[0]
    while len(queue) > 0:
        user = queue.pop()
        for gr in user_to_group[user]:
            connected.add(gr)
            for user in filter(lambda u: u not in used_users, group_to_user[gr]):
                queue.append(user)
                used_users.add(user)
        if len(connected) == len(group_to_user):
            break

    print('YES' if len(connected) == len(group_to_user) else 'NO')
