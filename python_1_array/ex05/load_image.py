import cv2


def ft_load(path: str):
    try:
        image_bgr = cv2.imread(path)
        # image_bgr = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        img = image_bgr[..., ::-1]
        print(img.shape)
        print(img)
        return (image_bgr)
    except Exception as err:
        print("Error:", err)
