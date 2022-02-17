import sys
import json
import random


names = ['Александр', 'Андрей', 'Сергей', 'Михаил', 'Антон']
second_names = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев']
middle_names = ['Александрович', 'Андреевич', 'Сергеевич', 'Махайлович', 'Антонович']
hobbies = ['бег', 'плавание', 'подводное плавание', 'велоспорт', 'танцы', 'чтение', 'пение', 'музыка']

#генератор случайных ФИО
def generate_random_id():
    random_name = random.choice(names)
    random_second_names = random.choice(second_names)
    random_middle_names = random.choice(middle_names)
    return (f'{random_second_names},{random_name},{random_middle_names}')

# #генератор случайных хобби
def generate_random_hobby():
    random_hobby = random.choice(hobbies)
    return random_hobby

#создаем документы со именами и хобби
with open('users.csv', 'w', encoding='utf-8') as fw:
     for i in range(15):
         fw.write(f'{generate_random_id()}\n')

with open('hobby.csv', 'w', encoding='utf-8') as fw:
     for i in range(12):
         fw.write(f'{generate_random_hobby()}, {generate_random_hobby()}\n')

#собираем словарь, проверяя разницу между длинами user hobby
list_users = []
list_hobby = []

with open('users.csv', 'r', encoding='utf-8') as f1r, open('hobby.csv', 'r', encoding='utf-8') as f2r:
    for row in f1r:
        list_users.append(row.strip())
    for row in f2r:
        list_hobby.append(row.strip())
    if len(list_users) >= len(list_hobby):
        delta = len(list_users) - len(list_hobby)
        i = 0
        while i < delta:
            list_hobby.append(None)
            i += 1
        dict_user_hobby = dict(zip(list_users, list_hobby))
        with open('task_6_3_result.json', 'w', encoding='utf-8') as wjf:
            json.dump(dict_user_hobby, wjf, ensure_ascii=False, indent=2)
    else:
        sys.exit(1)

print('\n''end')
