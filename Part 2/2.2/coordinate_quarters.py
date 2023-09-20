# Coordinate quarters

# Необходимо подсчитать и вывести количество точек, лежащих в каждой
# координатной четверти.
number = int(input())
list_of_point = []
for i in range(1, number+1):
    tupl = tuple(input().split())
    list_of_point.append(tupl)
    print(tupl)
print(number, list_of_point)

first = 0
second = 0
three = 0
four = 0

for point in list_of_point:
    if int(point[0]) > 0 and int(point[1]) > 0:
        first += 1
    elif int(point[0]) > 0 and int(point[1]) < 0:
        four += 1
    elif int(point[0]) < 0 and int(point[1]) > 0:
        second += 1
    elif int(point[0]) < 0 and int(point[1]) < 0:
        three += 1

print(f"Первая четверть:{first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {three}")
print(f"Четвертая четверть: {four}")
