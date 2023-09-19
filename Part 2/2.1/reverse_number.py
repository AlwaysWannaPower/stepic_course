# Переворот числа

number = input()

if len(number) == 5:
    print(int(number[::-1]))
else:
    print(int(number[0]+number[:0:-1]))
