def all_thing_is_obj(object: any) -> int:
    if type(object) is str:
        print(f'{object} is in the kitchen: {type(object)}')
    elif type(object) is list:
        print(f'List : {type(object)}')
    elif type(object) is tuple:
        print(f'Tuple : {type(object)}')    
    elif type(object) is set:
        print(f'Set : {type(object)}')
    elif type(object) is dict:
        print(f'Dict : {type(object)}')
    else:
        print('Type not found')
    return(42)
