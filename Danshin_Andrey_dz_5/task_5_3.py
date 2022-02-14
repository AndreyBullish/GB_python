tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
def check_gen(tutors: list, klasses: list):
    if len(tutors) > len(klasses):
        delta = len(tutors) - len(klasses)
        klasses.extend([None for i in range(delta)])
    for list_sum in zip(tutors, klasses):
        yield list_sum

generator = check_gen(tutors, klasses)
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
print('\n' 'end')


