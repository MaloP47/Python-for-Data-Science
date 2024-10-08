"""1_Array ex03"""

# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image

import numpy as np
import sys
from load_image import ft_load, channel
from PIL import Image


def formatPrinting(arr):
    """Just change format of printing an array for visibility"""
    print(f'{arr[0, 0]}\n{arr[0, 1]}\n{arr[0, 2]}')
    print('...')
    print(f'{arr[-1, -3]}\n{arr[-1, -2]}\n{arr[-1, -1]}')


def main():
    """Main function"""
    try:
        try:
            imgBefore = Image.open("./animal.jpeg")
        except Exception:
            sys.exit("could not open image")

        before = np.array(ft_load("./animal.jpeg"))
        formatPrinting(before)
        # print(before)

        imgCrop = imgBefore.crop((450, 100, 850, 500))
        grey = imgCrop.convert('L')
        grey.save('./zoomedIn.jpeg')

        norm = f'({grey.size[1]}, {grey.size[0]}, {channel(grey.mode)})'
        print(f'New shape after slicing: {norm} or {grey.size}')

        pix = np.array(grey)

        formatPrinting(pix)
        # print(pix)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
