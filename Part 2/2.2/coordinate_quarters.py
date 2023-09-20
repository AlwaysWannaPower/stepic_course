# Coordinate quarters

# Необходимо подсчитать и вывести количество точек, лежащих в каждой
# координатной четверти.
number = int(input())
list_of_point = []
for i in range(1, number+1):
    tupl = tuple(input().split())
    list_of_point.append(tupl)


count = [0, 0, 0, 0]

for point in list_of_point:
    x = int(point[0])
    y = int(point[1])
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1

# четверти можно в список строк и выводить элементы
print(f"Первая четверть:{count[0]}")
print(f"Вторая четверть: {count[1]}")
print(f"Третья четверть: {count[2]}")
print(f"Четвертая четверть: {count[3]}")
