""" 
Напишите программу для определения, является ли
число произведением двух чисел из данного набора.
Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
"""

n = int(input())
li = []
for i in range(1, n+1):
    li.append(int(input()))
target = int(input())
TEXT = "НЕТ"

for index, val in enumerate(li):
    for ind, vl in enumerate(li):
        if index != ind and val*vl == target:
            TEXT = "ДА"
            break

print(TEXT)
