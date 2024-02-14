def NULL_not_found(object: any) -> int:
    if object == 0 and type(object) is int:
        print(f'Zero: {object}',type(object))
    elif object == '':
        print(f'Empty: {object}',type(object))
    elif object is None:
        print(f'Nothing: {object}',type(object))
    elif type(object) is bool:
        print(f'Fake: {object}',type(object))
    elif type(object) is float:
        print(f'Cheese: {object}',type(object))
    else:
        print('Type not Found')
        return(1)
    return(0)