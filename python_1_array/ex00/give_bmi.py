
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    try:
        if (len(height) != len(weight)):
            raise AssertionError('List not the same size')
        bmi_res = []

        for i in range(len(height)):
            if (not isinstance(height[i], (int, float)) or not
               isinstance(weight[i], (int, float))):
                raise AssertionError('list must be int or float')
            bmi_res.append(weight[i] / pow(height[i], 2))
    except AssertionError as error:
        return (AssertionError.__name__ + ":", error)

    return (bmi_res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    try:
        if (not isinstance(limit, (int, float))):
            raise (AssertionError(
                "The value you have intered is not a number"))
        if (type(bmi) is list):
            for i in bmi:
                if (i > limit):
                    res.append(True)
                else:
                    res.append(False)
            return (res)
    except AssertionError as error:
        return (AssertionError.__name__ + ":", error)
