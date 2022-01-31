#Задание a

dataset=[]
for number in range(1, 1000, 2):
    dataset.append(number ** 3)
def sum_list_1(dataset):
    for i in range(len(dataset)):
        summary = 0
        number = dataset[i]
        while(number != 0):
            summary = summary + number % 10
            number = number // 10
        if summary % 7 == 0:
            result =+ dataset[i]
    return result
print(sum_list_1(dataset))
print('end')
#Задание b

dataset=[]
for number in range(1, 1000, 2):
    dataset.append((number ** 3)+17)
def sum_list_2(dataset):
    for i in range(len(dataset)):
        summary = 0
        number = dataset[i]
        while(number != 0):
            summary = summary + number % 10
            number = number // 10
        if summary % 7 == 0:
            result =+ dataset[i]
    return result
print(sum_list_2(dataset))
print('end')
#Задание с

dataset=[]
for number in range(1, 1000, 2):
    dataset.append(number ** 3)
def sum_list_1(dataset):
    for i in range(len(dataset)):
        summary = 0
        number = (dataset[i]+17)
        while(number != 0):
            summary = summary + number % 10
            number = number // 10
        if summary % 7 == 0:
            result =+ dataset[i]
    return result
print(sum_list_1(dataset))
print('end')
