

def square(x: int | float) -> int | float:

    return (x * x)


def pow(x: int | float) -> int | float:

    return (x ** x)


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        i = 0
        count += 1
        res = x
        while (i < count):
            res = function(res)
            i += 1
        return res
    return inner
