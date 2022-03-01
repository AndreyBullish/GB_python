from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) == 1:
            print(f'{func.__name__} ', end='')
            print(f'{args[0]}:', type(args[0]), end='')
        if len(args) != 1:
            for i in args:
                print(f'{func.__name__} ', end='')
                print(f', {i}:', type(i), f' ', end='')
        return result
    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

calc_cube(5)

print('\n')
print('-'*100)
print('\n')

@type_logger
def calc_cube(x, y):
   return x ** 3

calc_cube(5, 6)

print('\n')
print('end')