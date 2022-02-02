#Task_5a
from random import uniform
import math
def transfer_list_in_str(list_in):
    str_out = []
    for i in my_list:
        i = i * 100
        a = math.floor(i // 100)
        m = math.floor(i % 100)
        if a < 10:
            a = f'0{a}'
        n = f'{a}руб {m}коп'
        str_out.append(n)
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


#Task_5b
a=id(result_1)
def sort_prices(list_in):
    list_in.sort()
    return list_in

result_2 = sort_prices(result_1)
print(result_2)
b = id(sort_prices(result_1))
if a == b:
    print('списки одиннаковые')


#Task_5с

def sort_price_adv(list_in: list) -> list:
    list_out = sorted(list_in, reverse=True)
    return list_out

result_3 = sort_price_adv(result_1)
print(result_3)


#Task_5d
def check_five_max_elements(list_in: list) -> list:
    list_out = result_3[0:5]
    return list_out

result_4 = check_five_max_elements(result_3)
print(result_4)