from math import sqrt


def get_mean(my_list: list):
    return (sum(my_list)/len(my_list))


def print_mean(my_list: list):
    if (len(my_list) == 0):
        print('ERROR')
    else:
        mean = get_mean(my_list)
        print(f"mean : {mean}")


def get_median(my_list: list, size: int, x: int):

    if (size % x != 0):
        return (my_list[size//x])
    else:
        return ((my_list[size//x] + my_list[(size//x) - 1])/2)


def print_median(my_list: list):

    size = len(my_list)
    if (size == 0):
        print('ERROR')
    else:
        median = get_median(my_list, size, 2)
        print(f"median : {median}")


def print_quartile(my_list: list):

    list_to_sort = my_list.copy()
    size = len(list_to_sort)
    if (size == 0):
        print('ERROR')
    else:
        first_quartile = get_median(list_to_sort, size, 4)
        list_to_sort.sort(reverse=True)
        second_quartile = get_median(list_to_sort, size, 4)
        list_to_sort.sort(reverse=True)
        print(f"quartile : {[float(first_quartile), second_quartile]}")


def print_std(my_list: list):
    size = len(my_list)
    if (size == 0):
        print('ERROR')
    else:
        mean = get_mean(my_list)
        test = sum([float(pow(x - mean, 2)) for x in my_list])
        print(f"std : {sqrt(test/size)}")


def print_var(my_list: list):
    size = len(my_list)
    if (size == 0):
        print('ERROR')
    else:
        mean = get_mean(my_list)
        test = sum([float(pow(x - mean, 2)) for x in my_list])
        print(f"std : {(test/size)}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    my_list = list(args)
    my_list.sort()
    for key, values in kwargs.items():
        if (values == 'mean'):
            print_mean(my_list)
        elif (values == 'median'):
            print_median(my_list)
        elif (values == 'quartile'):
            print_quartile(my_list)
        elif (values == 'std'):
            print_std(my_list)
        elif (values == 'var'):
            print_var(my_list)
