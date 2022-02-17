import random
import sys
import json
import string

random_number = random.randrange(5, 10)
random_number2 = random.randrange(1, 5)

#генератор случайных ФИО
def generate_random_id(length):
    letters_upper = string.ascii_uppercase
    letters_lower = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters_upper) for i in range(1)) + ''.join(random.choice(letters_lower) for i in range(length))
    return f'{rand_string},{rand_string},{rand_string}'

#генератор случайных хобби
def generate_random_hobby(length):
     letters_lower = string.ascii_lowercase
     rand_string = ''.join(random.choice(letters_lower) for i in range(length))
     random_hobby_list = (list(f'{rand_string},' for i in range(random_number2)))
     return random_hobby_list

#создаем документы со именами и хобби
with open('users.csv', 'w', encoding='utf-8') as fw:
    for i in range(6):
        fw.write(f'{generate_random_id(5)}\n')
with open('hobby.csv', 'w', encoding='utf-8') as fw:
    for i in range(5):
        fw.write(f'{generate_random_hobby(10)}\n')

#собираем словарь, проверяя разницу между длинами user  hobby
list_users = []
list_hobby = []

with open('users.csv', 'r', encoding='utf-8') as f1r, open ('hobby.csv', 'r', encoding='utf-8') as f2r:
    for row in f1r:
        list_users.append(row)
    for row in f2r:
        list_hobby.append(row)
    if len(list_users) >= len(list_hobby):
        delta = len(list_users) - len(list_hobby)
        i = 0
        while i < delta:
            list_hobby.append('None')
            i += 1
        dict_user_hobby = dict(zip(list_users, list_hobby))
        with open('task_6_3_result.json', 'w', encoding='utf-8') as wjf:
            json.dump(dict_user_hobby, wjf, ensure_ascii=False, indent=2)
    else:
        print(int(1)) #тут я не понял что значит выходим из скрипта с кодом 1

print('\n''end')

