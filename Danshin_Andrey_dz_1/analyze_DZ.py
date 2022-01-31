my_list = [i**3 for i in range(1, 100, 2)]
print(my_list)
def sum_of_digits(dgt):
    '''Вычисляет сумму цифр числа'''
    res = 0
    while dgt != 0:
        res += dgt % 10
        dgt //= 10
    return res

#def sum_list_1(dataset: list) -> int:
    '''Вычисляет сумму чисел списка dataset, сумма чисел которых делится нацело на 7'''
sum1 = 0
list2 = []
for elem in my_list:
    b = sum_of_digits(elem)
    # проверяем что полученная сумма цифр делится на 7 без остатка

    if b % 7 == 0:
        list2.append(elem)
print(list2)
    # считаем сумму чисел в list2
sum_final = 0
for i in list2:
    sum_final += i
print(sum_final)

#result_1 = sum_list_1(my_list)
print(sum1)
