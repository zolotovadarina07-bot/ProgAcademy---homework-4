import random
list_1 = []
for i in range(12):
    list_1.append(random.randint(7500, 15000))
average = round(sum(list_1) / len(list_1), 2)
print(list_1)
print('Average salary:', average)
