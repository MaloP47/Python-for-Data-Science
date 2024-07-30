
"""Package from 42Paris Python Piscine"""


def count_in_list(lst, key):
    """Returns the number of key item in a container"""
    if lst is None or key is None:
        raise Exception("Wrong arguments")
    return lst.count(key)
