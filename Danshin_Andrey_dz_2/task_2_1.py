#Задание 2a
def convert_list(list_in):
#фильтруем кривым способом элементы "5" и "17"
    for i in my_list:
        if i.isdigit():
            if len(i) < 2:
                x = my_list.index(i)
                my_list[x] = f"', '0{i}', '"

    for i in my_list:
        if i.isdigit():
            x = my_list.index(i)
            my_list[x] = f"', '{i}', '"

#фильтруем еще более кривым способом элементы "+5"
    for i in my_list:
        if i.count('+'):
            if len(i) < 3:
                x = my_list.index(i)
                my_list[x] = f"', '+0{i[1:2]}', '"
    return my_list


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list(my_list)
print(result)
print('end')

#Задание 2b

def convert_list(list_in):
#фильтруем кривым способом элементы "5" и "17"
    for i in my_list:
        if i.isdigit():
            if len(i) < 2:
                x = my_list.index(i)
                my_list[x] = f" '0{i}' "

    for i in my_list:
        if i.isdigit():
            x = my_list.index(i)
            my_list[x] = f" '{i}' "

#фильтруем еще более кривым способом элементы "+5"
    for i in my_list:
        if i.count('+'):
            if len(i) < 3:
                x = my_list.index(i)
                my_list[x] = f" '+0{i[1:2]}' "
    return my_list

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list(my_list)
print(' '.join(result))
print('end')