"""1_Array ex04"""

# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.transpose

import numpy as np
import sys
from load_image import channel
from PIL import Image


def formatPrinting(arr):
    """Just change format of printing an array for visibility"""
    print(f'{arr[0, 0]}\n{arr[0, 1]}\n{arr[0, 2]}')
    print('...')
    print(f'{arr[-1, -3]}\n{arr[-1, -2]}\n{arr[-1, -1]}')


def myTranspose(img: Image) -> Image:
    """Transpose 90°"""
    width, height = img.size
    trans = Image.new('L', (height, width))

    originPix = img.load()
    transPix = trans.load()

    for x in range(width):
        for y in range(height):
            transPix[y, x] = originPix[x, y]
    return trans


def main():
    """Main function"""
    try:
        try:
            imgBefore = Image.open("./animal.jpeg")
        except Exception:
            sys.exit("could not open image")

        imgCrop = imgBefore.crop((450, 100, 850, 500))
        rotate = imgCrop.convert('L')
        # rotate = rotate.transpose(2)
        # rotate.save('./rotate.jpeg')

        norm = f'({rotate.size[1]}, {rotate.size[0]}, {channel(rotate.mode)})'
        print(f'New shape of image is: {norm} or {rotate.size}')
        pix = np.array(rotate)
        formatPrinting(pix)
        # print(pix)

        final = myTranspose(rotate)
        final.save('./rotate.jpeg')
        print(f'New shape after Transpose: {final.size}')
        finalTrans = np.array(final)
        print(finalTrans)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
