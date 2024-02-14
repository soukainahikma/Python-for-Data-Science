import sys
import string
def main(myString):
    upperCase = 0
    lowerCase = 0
    punctuation = 0
    digits = 0
    spaces = 0
    for i in myString:
        if i.isdigit():
            digits+=1
        if i.isspace():
            spaces+=1
        if i in string.punctuation:
            punctuation+=1
        if i.islower():
            lowerCase+=1
        if i.isupper():
            upperCase+=1
    print(f'The text contains {len(myString)} characters:')
    print(f'{upperCase} upper letters')
    print(f'{lowerCase} lower letters')
    print(f'{punctuation} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')

if __name__ == "__main__":
    try:
        if(len(sys.argv)>2): 
            raise(AssertionError('more than one argument is provided'))
        if(len(sys.argv) == 2):
            myString=sys.argv[1]
            main(myString)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)