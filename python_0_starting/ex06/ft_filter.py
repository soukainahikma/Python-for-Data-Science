
def ft_filter(myfunc, iter):
    if myfunc:
        return (item for item in iter if myfunc(item))
