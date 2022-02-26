import random
import string
import os
from string import ascii_lowercase, digits
import pprint


def func_dict_size_files(BASE_DIR):
    my_project_location = os.path.dirname(BASE_DIR)
    letter_and_numbers = ''.join([ascii_lowercase, digits])
    folder_for_files = os.path.join(BASE_DIR, 'folder_for_files')
    try:
        if not os.path.exists(folder_for_files):
                    os.makedirs(folder_for_files)
    except Exception as e:
        print(f'{e.__class__.__name__} Поймали ошибку: {e}')

    if os.path.isfile(folder_for_files) == True: #чтобы каждый раз не создавать 1000 ноых файлов
        print(''.join(random.sample(letter_and_numbers, random.randint(5, 10))))
        for _ in range(1000): #комп не тянет 100_000
            f_name = ''.join(random.sample(letter_and_numbers, random.randint(5, 10)))
            f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
            with open(os.path.join(folder_for_files, f'{f_name}.bin'), 'wb') as f:
                f.write(f_content)
    #начинаем собирать словарь:
    dict_out = dict()

    #я знаю что сделал по-колхозному, но ДЗ_7 все очень сложное, жаль что было мало времени на его выполнение, так как я остаю от курса
    list_less_10 = [] #здесь кол-во элементов
    list_less_100 = []
    list_less_1000 = []
    list_less_10000 = []
    type_files_list_less_10 = [] #здесь типы элементов
    type_files_list_less_100 = []
    type_files_list_less_1000 = []
    type_files_list_less_10000 = []
    print(my_project_location)
    for root, dirs, files in os.walk(my_project_location):
        if files:
            for item in os.scandir(root):
                if os.stat(item).st_size < 10:
                    list_less_10.append(item)
                    str_ite_list_less_10 = str(item)
                    str_ite_list_less_10 = (str_ite_list_less_10.partition('.')[2])
                    type_files_list_less_10.append(str_ite_list_less_10[:-2])
                    files_list_less_10_final = []
                    for i in type_files_list_less_10:
                        if i not in files_list_less_10_final and i != '':
                            files_list_less_10_final.append(i)
                if os.stat(item).st_size < 100 and os.stat(item).st_size > 10:
                    list_less_100.append(item)
                    str_ite_list_less_100 = str(item)
                    str_ite_list_less_100 = (str_ite_list_less_100.partition('.')[2])
                    type_files_list_less_100.append(str_ite_list_less_100[:-2])
                    files_list_less_100_final = []
                    for i in type_files_list_less_100:
                        if i not in files_list_less_100_final and i != '':
                            files_list_less_100_final.append(i)
                if os.stat(item).st_size < 1000 and os.stat(item).st_size > 100:
                    list_less_1000.append(item)
                    str_ite_list_less_1000 = str(item)
                    str_ite_list_less_1000 = (str_ite_list_less_1000.partition('.')[2])
                    type_files_list_less_1000.append(str_ite_list_less_1000[:-2])
                    files_list_less_1000_final = []
                    for i in type_files_list_less_1000:
                        if i not in files_list_less_1000_final and i != '':
                            files_list_less_1000_final.append(i)
                if os.stat(item).st_size < 10000 and os.stat(item).st_size > 1000:
                    list_less_10000.append(item)
                    str_ite_list_less_10000 = str(item)
                    str_ite_list_less_10000 = (str_ite_list_less_10000.partition('.')[2])
                    type_files_list_less_10000.append(str_ite_list_less_10000[:-2])
                    files_list_less_10000_final = []
                    for i in type_files_list_less_10000:
                        if i not in files_list_less_10000_final and i != '':
                            files_list_less_10000_final.append(i)


    dict_out[10] = (len(list_less_10), files_list_less_10_final)
    dict_out[100] = (len(list_less_100), files_list_less_100_final)
    dict_out[1000] = (len(list_less_1000), files_list_less_1000_final)
    dict_out[10000] = (len(list_less_10000), files_list_less_10000_final)

    return dict_out

pprint.pprint(func_dict_size_files(__file__), width='32')
print('end')
