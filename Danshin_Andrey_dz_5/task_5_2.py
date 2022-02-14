#я наверное не очень понял задание, надо было сделать именно через функцию без yield или все же можно было сделать без функции:)
n = 15
odd_nums = (num for num in range (1, n + 1, 2))
print(*odd_nums)
#print(next(odd_nums)) # если раскомментировать, то должно падать в traceback по StopIteration

print('\n' 'end')

