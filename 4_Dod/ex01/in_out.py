"""4_Dod ex00"""


def square(x: int | float) -> int | float:
    """Square"""
    return x.__mul__(x)


def pow(x: int | float) -> int | float:
    """Power"""
    return x.__pow__(x)


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        """outer & inner"""
        nonlocal count
        count += 1
        result = x
        i = count
        while i > 0:
            result = function(result)
            i -= 1
        return result
    return inner
