from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def formatPrinting(arr):
    """Just change format of printing an array for visibility"""
    print(f'{arr[0, 0]}\n{arr[0, 1]}\n{arr[0, 2]}')
    print('...')
    print(f'{arr[-1, -3]}\n{arr[-1, -2]}\n{arr[-1, -1]}')


array = ft_load("landscape.jpg")

formatPrinting(array)

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
print("####")
grey = ft_grey(array)
formatPrinting(grey)
print(ft_invert.__doc__)
