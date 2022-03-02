from functools import wraps
def func_filter(*args):
    if len(args) != 1:
        msg = f'wrong type of {args}'
        raise ValueError(msg)
    elif type(args[0]) != int:
        msg = f'wrong type of {args}'
        raise ValueError(msg)
    elif args[0] <= 0:
        msg = f'wrong type of {args}'
        raise ValueError(msg)
    else:
        return args[0] ** 3

def filter_wrapper(func_second_wrapper):
    def type_logger(func):
        @wraps(func)
        def wrapper(*args):
            func_second_wrapper(*args)
            result = func(*args)
            return result
        return wrapper
    return type_logger

@filter_wrapper(func_filter)
def calc_cube(x):
   return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
    print(calc_cube('0'))

    print('\n')
    print('end')