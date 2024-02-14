import sys
if(len(sys.argv)>1):
    try:
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if (len(sys.argv)>2):
            raise AssertionError('more than one argument is provided')
        res = "I'm Even." if (num % 2) ==0  else "I'm Odd"
        print(res)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
