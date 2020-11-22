from functools import wraps
from typing import Type, Callable, Sequence, Generator, Union
import inspect


def TypeCheck(arg_types: Union[Generator[Type, None, None], Sequence[Type]], return_type: Type):
    arg_types = list(arg_types)
    def decorator(f: Callable):
        spec = inspect.getfullargspec(f)
        key_to_position = {name: pos for pos, name in enumerate(spec.args)}

        @wraps(f)
        def inner(*args, **kwargs):
            # fill default values
            if spec.defaults is not None:
                optional_args_start = len(spec.args) - len(spec.defaults)
                for pos, value in enumerate(spec.defaults, start=optional_args_start):
                    key = spec.args[pos]
                    if len(args) <= pos and key not in kwargs:
                        kwargs[key] = value
            if spec.kwonlydefaults is not None:
                for key, value in spec.kwonlydefaults.items():
                    if key not in kwargs:
                        kwargs[key] = value

            # check parameter quantity
            if len(args) + len(kwargs) != len(arg_types):
                raise TypeError(f'Function {f.__name__} must have {len(arg_types)} arguments')

            # check positional args
            for i, value in enumerate(args):
                expected_type = arg_types[i]
                if type(value) != expected_type:
                    raise TypeError(f'Type of argument {i+1} is not {expected_type}')

            # check named args
            for key, value in kwargs.items():
                if key in key_to_position:
                    expected_type = arg_types[key_to_position[key]]
                    if type(value) != expected_type:
                        raise TypeError(f'Type of argument \'{key}\' is not {expected_type}')

            # check keyword-only args
            if spec.kwonlyargs is not None:
                for i, key in enumerate(spec.kwonlyargs):
                    expected_type = arg_types[len(args) + i]  # NOTE: may cause out-of-range error
                    if key in kwargs:
                        if type(kwargs[key]) != expected_type:
                            raise TypeError(f'Type of argument \'{key}\' is not {expected_type}')
                    else:
                        raise TypeError(f'Type of argument \'{key}\' is not {expected_type}')

            # check additional kwargs
            kwarg_pos = len(args) + len(spec.kwonlyargs) if spec.kwonlyargs is not None else len(args)
            for key, value in kwargs.items():
                if key not in key_to_position and (spec.kwonlyargs is None or key not in spec.kwonlyargs):
                    expected_type = arg_types[kwarg_pos]
                    if type(value) != expected_type:
                        raise TypeError(f'Type of argument \'{key}\' is not {expected_type}')
                    kwarg_pos += 1

            # check result
            res = f(*args, **kwargs)
            if type(res) != return_type:
                raise TypeError(f'Type of result is not {return_type}')
            return res
        return inner
    return decorator
