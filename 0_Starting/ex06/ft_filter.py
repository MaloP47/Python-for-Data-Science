"""Filter function rewrote"""


def ft_filter(function, iterable):
    """ft_filter using list comprehension"""
    if function:
        return (items for items in iterable if function(items))
    return (items for items in iterable if items)

# https://realpython.com/python-filter-function/

# print(filter.__doc__)
