from typing import TypeVar, Type, Tuple, List

T = TypeVar('T')


def fcounter(c: Type[T], *args) -> Tuple[List[str], List[str], List[str], List[str]]:
    def get_fields(obj) -> List[str]:
        return list(filter(lambda x: not x.startswith('_') and not callable(getattr(obj, x)), dir(obj)))

    def get_methods(obj) -> List[str]:
        return list(filter(lambda x: not x.startswith('_') and callable(getattr(obj, x)), dir(obj)))

    class_methods = get_methods(c)
    class_fields = get_fields(c)
    inst = c(*args)
    inst_methods = list(set(get_methods(inst)) - set(class_methods))
    inst_fields = list(set(get_fields(inst)) - set(class_fields))

    return sorted(class_methods), sorted(class_fields), sorted(inst_methods), sorted(inst_fields)
