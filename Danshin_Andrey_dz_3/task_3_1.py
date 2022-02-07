def num_translate(value: str) -> str:
    dict = {
        'один': 'one',
        'два': 'two',
        'три': 'three',
        'четыре': 'four',
        'пять': 'five',
        'шесть': 'six',
        'семь': 'seven',
        'восемь': 'eight',
        'девять': 'nine',
        'десять': 'ten'
    }
    for str_out, val in dict.items():

        if val == value:
            return str_out
        else:
            None

print(num_translate("one"))
print(num_translate("eight"))
print('\n''end')
