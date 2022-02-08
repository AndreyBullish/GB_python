nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
import random
def get_jokes(count) -> list:
    list_out = []
    a = 0
    while a != count:
        noun = nouns[random.randint(0, len(nouns) - 1)]
        adv = adverbs[random.randint(0, len(adverbs) - 1)]
        adj = adjectives[random.randint(0, len(adjectives) - 1)]
        joke = (f"{noun} {adv} {adj}")
        list_out.append(joke)
        a += 1
    return list_out

print(get_jokes(2))
print(get_jokes(10))

print('\n')


def get_jokes_adv(count: int, repeat_joke: bool, **kwargs) -> list:
    list_out = []
    a = 0 #задаем ноль
    #определяем длину шутки в словах, на случай если списки noun, adv, adj разной длины
    if len(nouns) <= len(adverbs) or len(nouns) <= len(adjectives):
        len_joke = len(nouns)
    elif len(adverbs) <= len(nouns) or len(adverbs) <= len(adjectives):
        len_joke = len(adverbs)
    else:
        len_joke = len(adjectives)
    if repeat_joke == True:
        while a < count:
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            joke = (f"{noun} {adv} {adj}")
            list_out.append(joke)
            a += 1
    else:
        if len_joke >= count:
            while a < count:
                noun = nouns.pop(random.randrange(0, len_joke))
                adv = adverbs.pop(random.randrange(0, len_joke))
                adj = adjectives.pop(random.randrange(0, len_joke))
                joke = (f"{noun} {adv} {adj}")
                list_out.append(joke)
                len_joke -= 1
                a += 1
        else: list_out.append(f'Увы, максимум можем сочинить только {len_joke} шуток')
    return list_out

print(get_jokes_adv(3, True))
print(get_jokes_adv(4, False))

print('\n''end')

