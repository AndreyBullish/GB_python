def get_numbers(src: list):
    src_compr = src[1:]
    result = []
    for i in range(len(src_compr)):
        if src_compr[i] > src[i]:
            result.append(src_compr[i])
    return result

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))

print('\n' 'end')

