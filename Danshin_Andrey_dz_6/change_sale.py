import sys


number_sum_str = input('Введите номер элемента который хотите изменить: ')
new_sum_str = input('Введите новое значение: ')
number_sum_int = int(number_sum_str)
new_sum_int = int(new_sum_str)

if len(new_sum_str) != 6:
    print('Длина нового значения должна быть 6 символов')
    sys.exit(1)
else:
    with open('bakery.csv', 'r+', encoding='utf-8') as fr:
        content = fr.read()
        content_str = content.split('\n')
        content_str_accurate = content_str
        if int(number_sum_int) > (len(content_str_accurate)):
            print('элемента с таким номером нет')
            sys.exit(1)
        if int(number_sum_int) <= 0:
            print('элемента с таким номером нет')
            sys.exit(1)
        else:
            fr.seek((number_sum_int - 1) * 8, 0)
            fr.write(new_sum_str)
