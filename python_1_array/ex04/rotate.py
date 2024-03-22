from load_image import ft_load
import cv2 as cv2


def ft_crop(image_array):
    (x, y, z) = image_array.shape

    xoff = int(x / 2)
    yoff = int(y / 2)
    if xoff < 400:
        xoff = 400
    cropped_image = image_array[xoff - 400:xoff, yoff:yoff + 400, 0:1]

    return (cropped_image)


def ft_rotate(image_array):
    return (cv2.transpose(image_array))
    pass


if __name__ == "__main__":
    image_array = ft_load("animal.jpeg")
    # print(image_array)
    image_crop = ft_crop(image_array)
    print(image_crop)
    image_rotation = ft_rotate(image_crop)
    cv2.imshow('Zoomed', image_crop)

    cv2.imshow('Zoomed Image', image_rotation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
