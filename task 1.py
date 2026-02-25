list_1 =  [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for i in list_1:
    if i % 2 != 0:
        count = count + 1
print('Кількість непарних:', count)