def transform_string(number):
    if number%10 == 0:
        return f'{number} процентов'
    if number == 1:
        return f'{number} процент'
    if number in range(1,5):
        return f'{number} процента'
    elif number > 14 and number%10 == 1:
        return f'{number} процент'
    elif number > 14 and number%10 <= 4:
        return f'{number} процента'
    elif number >= 11 and number <= 14:
        return f'{number} процентов'
    elif number%10 > 4:
        return f'{number} процентов'
for n in range(1, 101):
    print(transform_string(n))
print('end')