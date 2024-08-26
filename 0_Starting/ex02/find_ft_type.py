# def all_thing_is_obj(object: any) -> int:
#     if isinstance(object, list):
#         print(f'List : {type(object)}')
#     elif isinstance(object, tuple):
#         print(f'Tuple : {type(object)}')
#     elif isinstance(object, set):
#         print(f'Set : {type(object)}')
#     elif isinstance(object, dict):
#         print(f'Dict : {type(object)}')
#     elif isinstance(object, str):
#         print(object + f' is in the kitchen : {type(object)}')
#     else:
#         print('Type not found')
#     return 42


def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print(f'List : {type(object)}')
    elif type(object) is tuple:
        print(f'Tuple : {type(object)}')
    elif type(object) is set:
        print(f'Set : {type(object)}')
    elif type(object) is dict:
        print(f'Dict : {type(object)}')
    elif type(object) is str:
        print(object + f' is in the kitchen : {type(object)}')
    else:
        print('Type not found')
    return 42
