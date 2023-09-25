"""
На вход программе подается строка текста из натуральных
чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние
элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то
последний остается на своем месте.
"""
numbers = [int(i) for i in input().split()]


if len(numbers) % 2 == 0:
    for ind in range(0, len(numbers), 2):
        numbers[ind], numbers[ind+1] = numbers[ind+1], numbers[ind]

else:
    for ind in range(0, len(numbers)-1, 2):
        numbers[ind], numbers[ind+1] = numbers[ind+1], numbers[ind]
print(' '.join(map(str, numbers)))
