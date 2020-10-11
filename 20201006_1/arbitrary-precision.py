from decimal import Decimal, getcontext


if __name__ == '__main__':
    expr = input()
    precision = int(input())
    getcontext().prec = precision + 2

    start = Decimal('-1.5')
    end = Decimal('1.5')
    x = end
    f = compile(expr, '<decimal.Decimal>', 'eval')

    while end - start >= Decimal(f'1e-{precision}'):
        x = (start + end) / Decimal(2)
        fx = eval(f)
        if fx < 0:
            start = x
        elif fx == 0:
            end = x
            break
        else:
            end = x
    getcontext().prec = precision
    print('{{:.{}f}}'.format(precision).format(end))
