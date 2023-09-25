"""
На вход программе подается строка текста из натуральных чисел
. Из неё формируется список чисел. Напишите программу подсчета
количества чисел, которые больше предшествующего им в этом списке числа.
"""
numbers = [int(el) for el in input().split()]
COUNT = 0
for index, el in enumerate(numbers):
    if index != len(numbers) - 1 and el < numbers[index+1]:
        COUNT += 1
print(COUNT)
