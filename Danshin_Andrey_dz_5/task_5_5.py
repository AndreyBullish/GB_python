def get_uniq_numbers(src: list):
    result = []
    for i in range(len(src)):
        if src.count(src[i]) == 1:
            result.append(src[i])
    return result

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
#оптимизировать как не приходит в голову, т.к. в задании указано с сохр порядкового номера, то есть использовать множества нельзя получается. Посдкажите, плиз, как сделать оптимизацию
print('\n' 'end')