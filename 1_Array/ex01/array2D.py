"""1_Array ex01"""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints shape & returns sliced version"""

    if not isinstance(family, list):
        raise Exception("wrong type of container")

    if not isinstance(start, int) or not isinstance(end, int):
        raise Exception("wrong type of arguments")

    if any(not isinstance(item, list) or len(item) != len(family[0])
            for item in family):
        raise Exception("must be a 2D array")

    Shape = np.array(family)
    print(f'My shape is : {Shape.shape}')
    newShape = Shape[start:end]
    print(f'My new shape is : {newShape.shape}')
    return newShape.tolist()
