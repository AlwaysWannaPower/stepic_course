# Индекс массы тела

# ИМТ= масса (кг)  / рост(м)× рост(м)
weight = float(input())
height = float(input())

index = weight/(height**2)
print(index)
if 18.5 <= index <= 25:
    print("Оптимальная масса")
elif 18.5 > index:
    print("Недостаточная масса")
else:
    print("Избыточная масса")
