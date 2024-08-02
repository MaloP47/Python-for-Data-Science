"""1_Array ex05"""

from PIL import Image
import numpy as np


def ft_invert(array: np.array) -> np.array:
    """invert colors: =, +, -, *"""
    img = 255 - array
    Image.fromarray(img).save('./modified/inverted.jpg')
    return img


def ft_red(array: np.array) -> np.array:
    """to red: =, *"""
    img = array.copy()
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    Image.fromarray(img).save('./modified/red.jpg')
    return img


def ft_green(array: np.array) -> np.array:
    """to green: =, -"""
    img = array.copy()
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    Image.fromarray(img).save('./modified/green.jpg')
    return img


def ft_blue(array: np.array) -> np.array:
    """to blue: ="""
    img = array.copy()
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    Image.fromarray(img).save('./modified/blue.jpg')
    return img


def ft_grey(array: np.array) -> np.array:
    """to grey: =, /"""
    img = array.copy()
    r = img[:, :, 0] // 3
    g = img[:, :, 1] // 3
    b = img[:, :, 2] // 3
    grey = r + g + b
    greyImg = np.stack([grey, grey, grey], axis=2)
    Image.fromarray(greyImg.astype(np.uint8)).save('./modified/grey.jpg')
    # im = Image.fromarray(img)
    # grey = im.convert('L')
    # grey.save('./modified/grey.jpg')
    # return np.array(grey)
    return np.array(greyImg)
