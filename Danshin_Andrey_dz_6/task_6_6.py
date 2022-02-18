import sys


sale_sum_list = sys.argv[1:]
sale_sum_str = ''.join(sale_sum_list)
file_1 = open('bakery.csv', 'r', encoding='utf-8')
    fw.write(f'{sale_sum_str}\n')