""" В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
собой (оба являться минимальными), так и различаться. """

from random import randint

MAX_NUMBER = 1000
lst = []
all_count = randint(10, 20) #всего элементов в списке от 10 до 49
for i in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER)
    lst.append(number)

print('начальный список: ', lst)
lst.sort()
print(lst[:2])
