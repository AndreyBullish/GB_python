src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def get_uniq_numbers1(src: list):
    result = []
    for i in range(len(src)):
        if src.count(src[i]) == 1:
            result.append(src[i])
    return result

print(*get_uniq_numbers1(src))

def get_uniq_numbers2(src: list):
    num_set = set()
    num_set_final = set()
    for num in src:
        if not num in num_set:
            num_set_final.add(num)
        else:
            num_set_final.discard(num)
        num_set.add(num)
print(get_uniq_numbers2(src))

uniq_numbers = [num for num in src if src.count(num) == 1]
print(uniq_numbers)
print('\n' 'end')