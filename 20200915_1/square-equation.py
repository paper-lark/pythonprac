from math import sqrt


if __name__ == '__main__':
    a, b, c = eval(input())
    if a == 0:
        if b == 0:
            print(-1 if c == 0 else 0)
        else:
            print(-c / b)
    else:
        disc = b**2 - 4*a*c
        if disc < 0:
            print(0)
        elif disc == 0:
            print(-b / (2 * a))
        else:
            x1 = (-b - sqrt(disc)) / (2 * a)
            x2 = (-b + sqrt(disc)) / (2 * a)
            if x1 > x2:
                print(x2, x1)
            else:
                print(x1, x2)
