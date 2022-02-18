import sys


sale_sum = sys.argv[1:]
for i in range(len(sale_sum)):
    if i >= 0 and i < 2:
        first_int = sale_sum[:1]
        second_int = sale_sum[1:2]
    else:
        print('Вы ввели неверное кол-во аргументов, кол-во аргументов должно быть от 0 до 2 (включительно)')
        sys.exit(1)

with open('bakery.csv', 'r', encoding='utf-8') as fr:
    if len(sys.argv[1:]) == 0:
        print(fr.read())
    if len(sys.argv[1:]) == 1:
        first_int_str = ''.join(first_int)
        first_int_num = int(first_int_str)
        sum_int = fr.seek(first_int_num * 8, 0)
        print(fr.read())
    if len(sys.argv[1:]) == 2:
        first_int_str = ''.join(first_int)
        first_int_num = int(first_int_str)
        second_int_str = ''.join(second_int)
        second_int_num = int(second_int_str)
        sum_int = fr.seek(first_int_num * 8, 0)
        str_1 = (fr.read())
        sum_int = fr.seek(second_int_num * 8, 0)
        str_2 = (fr.read())
        if str_2 in str_1:
            print(str_1.replace(str_2, ''))




