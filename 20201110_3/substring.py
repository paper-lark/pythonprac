from collections import UserString, Counter


class SubString(UserString):
    __Counter = Counter

    def __sub__(self, other) -> 'SubString':
        cnt = self.__Counter(other)

        def should_keep(c: str) -> bool:
            if c not in cnt:
                return True
            cnt.subtract(c)
            if cnt[c] < 0:
                del cnt[c]
            return c not in cnt

        return type(self)(''.join(map(lambda c: str(c), filter(should_keep, self))))


del UserString, Counter
