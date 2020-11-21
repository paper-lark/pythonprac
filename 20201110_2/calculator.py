import re
import builtins

id_prefix = 'ID__'
identifier_re = re.compile(r'[a-zA-z_]\w*')
allowed_symbols_re = re.compile(r'(\b[a-zA-z_]\w*\b|\b\d+\b|[()+/*%-])+')
syntax_errors_re = re.compile(r'//|\*\*|\w\(')


def main():
    context = {}
    line = input()

    while line:
        try:
            # check comment
            if line.startswith('#'):
                continue

            # check statement
            if '=' in line:
                identifier, expr = map(lambda s: s.strip(), line.split('=', 1))
                if not identifier_re.fullmatch(identifier):
                    raise Exception('Assignment error')
            else:
                identifier = None
                expr = line

            # validate expression
            expr = ''.join(c for c in expr if not c.isspace())
            if not allowed_symbols_re.fullmatch(expr):
                raise Exception('Syntax error')
            if syntax_errors_re.search(expr):
                raise Exception('Syntax error')

            # evaluate expresion
            try:
                expr = identifier_re.sub(f'{id_prefix}\\g<0>', expr).replace('/', '//')
                value = eval(expr, builtins.__dict__, context)
            except NameError:
                raise Exception('Name error')
            except Exception:
                raise Exception('Runtime error')

            # process expression result
            if identifier is not None:
                context[id_prefix + identifier] = value
            else:
                print(value)

        except Exception as e:
            print(e.args[0])
        finally:
            line = input()


if __name__ == '__main__':
    main()
