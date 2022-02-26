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
    list_less_10 = []
    list_less_100 = []
    list_less_1000 = []
    list_less_10000 = []
    print(my_project_location)
    for root, dirs, files in os.walk(my_project_location):
        if files:
            for item in os.scandir(root):
                if os.stat(item).st_size < 10:
                    list_less_10.append(item)
                if os.stat(item).st_size < 100 and os.stat(item).st_size > 10:
                    list_less_100.append(item)
                if os.stat(item).st_size < 1000 and os.stat(item).st_size > 100:
                    list_less_1000.append(item)
                if os.stat(item).st_size < 10000 and os.stat(item).st_size > 1000:
                    list_less_1000.append(item)

    dict_out[10] = len(list_less_10)
    dict_out[100] = len(list_less_100)
    dict_out[1000] = len(list_less_1000)
    dict_out[10000] = len(list_less_10000)

    return dict_out

pprint.pprint(func_dict_size_files(__file__), width='16')
print('end')
