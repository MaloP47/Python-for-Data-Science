"""4_Dod ex00"""

from typing import Any


def Mean(total: float, nbArgs: int) -> None:
    """Print Mean"""
    print(f'mean : {total / nbArgs}')


def Median(args: list, nbArgs: int) -> None:
    """Print Median"""
    args.sort()
    median = nbArgs // 2
    if nbArgs % 2 == 0:
        res = (args[median - 1] + args[median]) / 2
    else:
        res = args[median]
    print(f'median : {res}')


def Quartile(args: list, nbArgs: int) -> None:
    """Print Quartile"""
    args.sort()
    quarter = nbArgs // 4
    threeQ = quarter * 3
    res25 = args[quarter]
    res75 = args[threeQ]
    print(f'quartile : [{res25.__float__()}, {res75.__float__()}]')


def Std(args: list, total: float, nbArgs: int, Var: str) -> float:
    """Std & Var because I'm lazy"""
    mean = total / nbArgs
    totalVar = 0
    for arg in args:
        totalVar += (arg - mean) ** 2
    var = totalVar / nbArgs
    if Var:
        return var
    print(f'std : {var ** 0.5}')


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Stats"""

    nbArgs = 0
    total = 0
    lst = []

    for arg in args:
        try:
            lst.append(arg)
            nbArgs += 1
            total += arg
        except TypeError:
            return

    if nbArgs == 0:
        for kwarg in kwargs.items():
            print('ERROR')
        return

    for kwarg in kwargs.values():
        match kwarg:
            case('mean'):
                Mean(total, nbArgs)
            case('median'):
                Median(lst, nbArgs)
            case('quartile'):
                Quartile(lst, nbArgs)
            case('std'):
                Std(lst, total, nbArgs, '')
            case('var'):
                print(f"var : {Std(lst, total, nbArgs, 'yes')}")
