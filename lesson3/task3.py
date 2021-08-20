""" В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """

from random import randint

MAX_NUMBER = 100
lst = []
min_max = [MAX_NUMBER, -1, -MAX_NUMBER, -1]
#в массиве min_max первый элемент - минимальное значение, за ним будет хранится его позиция в списке,
# на третьем месте - максимальное значение, на 4ом месте - его позиция в списке
all_count = randint(10, 50)#всего элементов в списке
for i in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER)
    lst.append(number)
    if min_max[0] > number:
        min_max[0] = number
        min_max[1] = i
    if min_max[2] < number:
        min_max[2] = number
        min_max[3] = i
print('начальный список: ', lst)
print(f'изначально минимум {min_max[0]} был на {min_max[1]+1} месте. Максимум {min_max[2]} был на {min_max[3]+1} месте.')
lst[min_max[1]] = min_max[2]
lst[min_max[3]] = min_max[0]
print('измененный список: ', lst)
