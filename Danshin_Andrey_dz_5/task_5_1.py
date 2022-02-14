def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for num in range(1, number + 1, 2):
        yield num

'''
odd_to_5 = odd_nums(5)
print(next(odd_to_5)) #1
print(next(odd_to_5)) #3
print(next(odd_to_5)) #5
print(next(odd_to_5)) #StopIteration
'''

n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

print('\n' 'end')