def thesaurus_adv(*args) -> dict:
# функция сортировке по первой букве фамилии
    dict_out_second_letter = {}
    for person in args:
        b = person.rpartition(' ')[2]
        key = b[0:1]
        if dict_out_second_letter.get(key) == None:
            dict_out_second_letter[key] = [person]
        else:
            dict_out_second_letter[key] += [person]

# дальше собираем лист где потом будем второй аргумент пересобирать
    dict_out_len = len(dict_out_second_letter)
    dict_out = {}
    for i in range(dict_out_len):
        a = list(dict_out_second_letter.popitem())
        item_1 = a[0]
        item_2 = a[1]
        dict_out2 = {}
        for y in item_2:
            key = y[0:1]
            if dict_out2.get(key) == None:
                dict_out2[key] = [y]
            else:
                dict_out2[key] += [y]
        dict_out[item_1] = dict_out2
    return dict_out

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

#Тоже самое только с сортировкой

def thesaurus_adv(*args) -> dict:
    dict_out_second_letter = {}
    for person in args:
        b = person.rpartition(' ')[2]
        key = b[0:1]
        if dict_out_second_letter.get(key) == None:
            dict_out_second_letter[key] = [person]
        else:
            dict_out_second_letter[key] += [person]
    dict_out_len = len(dict_out_second_letter)
    dict_out = {}
    for i in range(dict_out_len):
        a = list(dict_out_second_letter.popitem())
        item_1 = a[0]
        item_2 = a[1]
        dict_out2 = {}
        for y in item_2:
            key = y[0:1]
            if dict_out2.get(key) == None:
                dict_out2[key] = [y]
            else:
                dict_out2[key] += [y]
        dict_out[item_1] = dict_out2
    sorted_d = dict(sorted(dict_out.items(), key=lambda f: f[0]))
    return sorted_d

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print('\n''end')
