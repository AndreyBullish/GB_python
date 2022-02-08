
def thesaurus(*args) -> dict:
    dict_out = {}
    for person in args:
        key = person[0:1]
        if dict_out.get(key) == None:
            dict_out[key] = [person]
        else:
            dict_out[key] += [person]
    return dict_out

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Андрей"))
print('\n''end')