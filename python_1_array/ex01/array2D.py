import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        arr = np.array(family, dtype='f')
        print(f'My shape is : {np.asarray(family).shape}')
        res = arr[start:end]
        print(f'My new shape is : {np.asarray(res).shape}')
        return (res)
    except Exception as err:
        print("Error:", err)
