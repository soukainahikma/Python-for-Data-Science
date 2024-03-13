import sys

def myfunc(morse_code,string):
    res = []
    for i in string:
        code = morse_code.get(i.upper())
        res.append(code)
        if code is None:
            raise(AssertionError('the arguments are bad'))
    return("".join(res))

if __name__ == "__main__":
    NESTED_MORSE = { ' ': '/',
    'A': '.-',
    'N': '-.',
    'B': '-...',
    'O': '---',
    'C': '-.-.',
    'P': '.--.',
    'D': '-..',
    'Q': '--.-',
    'E': '.',
    'R': '.-.',
    'F': '..-.',
    'S': '...',
    'G': '--.',
    'T': '-',
    'H': '....',
    'U': '..-',
    'I': '..',
    'V': '...-',
    'J': '.---',
    'W': '.--',
    'K': '-.-',
    'X': '-..-',
    'L': '.-..',
    'Y': '-.--' ,
    'M': '--',
    'Z': '--..',
    '1': '.----',
    '6': '-....',
    '2': '..---',
    '7': '--...',
    '3': '...--',
    '8': '---..',
    '4': '....-',
    '9': '----.',
    '5': '.....',
    '0': '-----',
    }
    try:
        if(len(sys.argv)!=2): 
            raise(AssertionError('the arguments are bad'))
        res =myfunc(NESTED_MORSE,sys.argv[1])
        print(res )
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    pass