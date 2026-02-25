import random

list_1 = []
for i in range(4):
    list_1.append(random.randint(1, 10))

list_2 = list_1.copy()  # копіюємо перший список
for n in list_1:
    list_2.append(n * 2)
print(list_1)
print(list_2)