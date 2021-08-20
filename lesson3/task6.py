"""  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать. """

from random import randint

MAX_NUMBER = 100
lst = []
result_max_num = -MAX_NUMBER
min_max = [MAX_NUMBER, -1, -MAX_NUMBER, -1]
#в массиве min_max первый элемент - минимальное значение, за ним будет хранится его позиция в списке,
# на третьем месте - максимальное значение, на 4ом месте - его позиция в списке

all_count = randint(10, 50) #всего элементов в списке от 10 до 49
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
index1, index2 = min_max[1], min_max[3] # границы от и до для суммирования элементов
if index1 > index2:# меняем местами, если границы не по возрастанию
    index1, index2 = index2, index1
summ = 0
for i in range(index1+1, index2):
    summ += lst[i]
print(f'Сумма элементов массива между минимальным и максимальным элементами (с позиции {index1} по {index2}) '
      f'равна {summ}')
