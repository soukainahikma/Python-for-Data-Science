import cv2


def ft_load(path: str):
    try:
        image_bgr = cv2.imread(path)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        print(image_rgb.shape)
        return (image_rgb)
    except Exception as err:
        print("Error:", err)
