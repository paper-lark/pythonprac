from typing import List


def No_2Zero(n: int, k: int):
    valid_cnt: List[int] = [0] * (n + 1)
    with_trailing_zero_cnt: List[int] = [0] * (n + 1)
    valid_cnt[1] = k - 1
    with_trailing_zero_cnt[1] = 0

    for i in range(2, n + 1):
        valid_cnt[i] = (valid_cnt[i - 1] + with_trailing_zero_cnt[i - 1]) * (k - 1)
        with_trailing_zero_cnt[i] = valid_cnt[i - 1]

    return valid_cnt[n] + with_trailing_zero_cnt[n]
