""" В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию
в массиве. """

from random import randint

MAX_NUMBER = 10
lst = []
result_max_num = -MAX_NUMBER
all_count = randint(10, 50) #всего элементов в списке от 10 до 49
for i in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER)
    lst.append(number)
"""# либо ввод с клавиатуры:
lst = input('Введите элементы массива через пробел ').split()
print(lst)
for element in lst:
    if result_max_num < int(element) < 0:
        result_max_num = element
"""
print(lst)
for element in lst:
    if result_max_num < element < 0:
        result_max_num = element 
print(f'Максимальное отрицательное число здесь {result_max_num}')
