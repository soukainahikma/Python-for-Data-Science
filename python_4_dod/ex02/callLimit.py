
def callLimit(limit: int):
    count = 0

    def callLimiter(func):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if (count > limit):
                print(f"Error: {func} call too many times")
            else:
                return func()
        return limit_function
    return callLimiter
