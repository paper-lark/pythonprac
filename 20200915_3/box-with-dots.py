
if __name__ == '__main__':
    line = input()
    xs = []
    ys = []
    zs = []
    while len(line) > 0:
        x, y, z = eval(line)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        line = input()
    if len(xs) < 2:
        print(0)
    else:
        print((max(xs) - min(xs)) * (max(ys) - min(ys)) * (max(zs) - min(zs)))
