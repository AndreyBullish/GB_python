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
    if value[:1].isupper():
        x = value.lower()
        for key, val in dict.items():
            if val == x:
                return key.capitalize()
            else:
                None
    for key, val in dict.items():
        if val == value:
            return key
        else:
            None

print(num_translate("One"))
print(num_translate("Eight"))
print('\n''end')