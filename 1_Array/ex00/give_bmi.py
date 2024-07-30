"""1_Array ex00"""

import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """Returns a list of BMI"""

    if len(height) != len(weight):
        raise Exception("List are not the same size")
    if not all(isinstance(hValue, (int, float)) for hValue in height):
        raise Exception("List of value must be of int or float")
    if not all(isinstance(wValue, (int, float)) for wValue in weight):
        raise Exception("List of value must be of int or float")

    heightArray = np.array(height)
    weightArray = np.array(weight)

    if np.any(heightArray <= 0) or np.any(weightArray <= 0):
        raise Exception("values in either lists must be positive")

    if np.any(heightArray >= 2.73) or np.any(weightArray >= 635):
        raise Exception("Value is beyond human limits")

    if np.any(heightArray <= 0.546) or np.any(weightArray <= 2.1):
        raise Exception("Value is below human limits.")

    giveBmi = weightArray / (heightArray ** 2)
    return giveBmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of wether or not the BMI is in target"""
    if not isinstance(limit, int) or limit < 0:
        raise Exception("wrong type")
    if not all(isinstance(bmiValue, (int, float)) for bmiValue in bmi):
        raise Exception("List of value must be of int or float")
    limitList = [elem > limit for elem in bmi]
    return limitList
