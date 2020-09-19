
if __name__ == '__main__':
    max1, max2 = None, None
    x = int(input())
    while x != 0:
        if max1 is None or x > max1:
            max2 = max1
            max1 = x
        elif (max2 is None or x > max2) and max1 != x:
            max2 = x
        x = int(input())
    print(max2 if max2 is not None else 'NO')
