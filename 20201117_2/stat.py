from collections import Counter
from typing import Optional, Tuple, Union, Any


def Stat(target: object, field: Optional[str] = None) -> Union[Tuple[int, int], object]:
    # get statistics
    if field is not None:
        read_count = getattr(target, '_read_count')
        write_count = getattr(target, '_write_count')

        return read_count[field], write_count[field]

    # decorate class
    setattr(target, '_read_count', Counter())
    setattr(target, '_write_count', Counter())

    class Desc:
        _private_name = None
        _name = None
        _default_value = None

        def __init__(self, name: str, value: Any):
            self._name = name
            self._default_value = value
            self._private_name = f'_stat_{name}'

        def __get__(self, obj, cls):
            cnt = getattr(obj, '_read_count')
            cnt[self._name] += 1
            return getattr(obj, self._private_name) \
                if hasattr(obj, self._private_name) else self._default_value

        def __set__(self, obj, val):
            cnt = getattr(obj, '_write_count')
            cnt[self._name] += 1
            setattr(obj, self._private_name, val)

    fields_to_watch = [k for k in vars(target) if not k.startswith('_')]
    for field in fields_to_watch:
        initial = getattr(target, field)
        setattr(target, field, Desc(field, initial))

    original_init = target.__init__

    def patched_init(self, *args, **kwargs):
        setattr(self, '_read_count', Counter())
        setattr(self, '_write_count', Counter())
        original_init(self, *args, **kwargs)

    target.__init__ = patched_init

    return target
