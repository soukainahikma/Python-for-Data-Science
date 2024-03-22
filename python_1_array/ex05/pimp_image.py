from array import array
import cv2 as cv2
import numpy as np


def ft_invert(array) -> array:
    """
    Inverts the color of image received
    """
    image_bgr = 255 - array
    return (image_bgr)


def ft_red(array) -> array:
    red_image = array.copy()
    red_image[:, :, 0] = 0
    red_image[:, :, 1] = 0
    return (red_image)


def ft_green(array) -> array:
    green_image = array.copy()
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0
    return (green_image)


def ft_blue(array) -> array:
    blue_image = array.copy()
    blue_image[:, :, 1] = 0
    blue_image[:, :, 2] = 0
    return (blue_image)


def ft_grey(array) -> array:
    gray_image = np.sum(array, axis=2)
    grey_array = (gray_image / 3).astype(np.uint8)
    cv2.imshow('red Image', grey_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
