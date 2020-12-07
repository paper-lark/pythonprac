import inspect
from itertools import chain


class checked(type):
    def __new__(mcs, name, parents, props):
        patched_props = {}
        for k, v in props.items():
            if callable(v):
                v = mcs.with_type_check(v)
            patched_props[k] = v
        return super(checked, mcs).__new__(mcs, name, parents, patched_props)

    @staticmethod
    def with_type_check(f):
        spec = inspect.getfullargspec(f)
        typed = f.__annotations__

        def a(*args, **kwargs):
            for name, v in chain(zip(spec.args, args), kwargs.items()):
                if name in typed and not isinstance(v, typed[name]):
                    raise TypeError(f'Type mismatch: {name}')

            if spec.varargs is not None and len(args) > len(spec.args):
                name = spec.varargs
                for v in args[len(spec.args):]:
                    if name in typed and name in typed and not isinstance(v, typed[name]):
                        raise TypeError(f'Type mismatch: {name}')

            if spec.varkw is not None and spec.varargs in typed:
                name = spec.varkw
                for k, v in kwargs.items():
                    if k not in spec.args and k not in spec.kwonlyargs:
                        if name in typed and not isinstance(v, typed[name]):
                            raise TypeError(f'Type mismatch: {k}')

            value = f(*args, **kwargs)
            if 'return' in typed and not isinstance(value, typed['return']):
                raise TypeError('Type mismatch: return')
            return value

        return a
