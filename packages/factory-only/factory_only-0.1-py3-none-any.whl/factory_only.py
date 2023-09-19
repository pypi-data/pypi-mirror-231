from __future__ import annotations

import inspect


def factory_only(fac: str):
    """Dataclass decorator to make factory-usage mandatory.

    Example
    =======

    @factory_only("my_factory")
    @dataclass
    class MyClass:
        arg1: int
        arg2: str

    def my_factory(a: int, b: int) -> MyClass:
        b_str = str(b)
        return MyClass(arg1=a, arg2=b_str)

    :param fac:
    :return:
    """
    if not fac:
        raise RuntimeError("Please provide a factory function to create your class.")

    def wrapper(cls):
        def inner(*args, **kwargs):
            parent = inspect.stack()[1].function
            if parent not in fac:
                raise RuntimeError(
                    f"You tried to __init__ should only be called from factory function but is called from {parent}")
            return cls(*args, **kwargs)

        return inner

    return wrapper
