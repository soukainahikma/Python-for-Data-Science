from ft_filter import ft_filter
import sys

def myFunc(x,num):
  if len(x) < num:
    return False
  else:
    return True

if __name__ == "__main__":
    try:
        if(len(sys.argv)!=3): 
            raise(AssertionError('the arguments are bad'))
        if(type(sys.argv[1]) is not str):
            raise(AssertionError('the arguments are bad'))
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(lambda item : myFunc(item,num),list(sys.argv[1].split(' ')))))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)