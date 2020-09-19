
if __name__ == '__main__':
    x = int(input())
    max_sum = None
    current = None

    while x != 0:
        if x < 0:
            max_sum = max(max_sum, current) if max_sum is not None else current

        current = max(x, current + x) if current is not None else x
        max_sum = max(max_sum, current) if max_sum is not None else current
        x = int(input())

    print(max_sum if max_sum is not None else 0)
