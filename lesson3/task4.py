"""  Определить, какое число в массиве встречается чаще всего. """


from random import randint

MAX_NUMBER = 10
lst = []
result_max_num = [None, 0]
all_count = randint(10, 50) #всего элементов в списке от 10 до 49
for i in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER)
    lst.append(number)
""" либо ввод с клавиатуры:
lst = input('Введите элементы массива через пробел ').split()
"""
print(lst)

for element in lst:
    i = lst.count(element)
    print(element, ' - ', i)
    if i > result_max_num[1]:
        result_max_num[0] = element
        result_max_num[1] = i
print(f'Больше всего раз встречается число {result_max_num[0]}. Встречается {result_max_num[1]} раз.')
