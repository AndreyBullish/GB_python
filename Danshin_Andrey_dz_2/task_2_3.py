#my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

def convert_name_extract(list):
    #дробим список на списки
    my_list_sep = [i.split() for i in my_list]
    #собираем список из имен
    names = []
    for i in my_list_sep:
        names.append(i[-1])
    #делаем еще один новый список с красивыми именами (@Анатолий, будет классно если вы покажите как делать такие операции короче
    final_names = []
    for i in names:
        final_names.append(i.capitalize())
    #лепим финальный список с именами
    list_out = []
    for i in final_names:
        list_out.append(f'Привет, {i}!')
    return(list_out)

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
print('end')