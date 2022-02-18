import sys


sale_sum_list = sys.argv[1:]
sale_sum_str = ''.join(sale_sum_list)
if len(sale_sum_str) == 6:
    with open('bakery.csv', 'a+', encoding='utf-8') as fw:
        fw.write(f'{sale_sum_str}\n')
else:
    print('в нашей задаче число должно быть длиной 6 символов, иначе я тогда совсем не знаю как это программировать')
