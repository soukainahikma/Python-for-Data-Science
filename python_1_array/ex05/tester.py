from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import cv2 as cv2


array = ft_load("landscape.jpg")
inverted = ft_invert(array.copy())

cv2.imshow('Zoomed Image', inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
ft_red(array.copy())
ft_green(array.copy())
ft_blue(array.copy())
ft_grey(array.copy())
# print(ft_invert.__doc__)
