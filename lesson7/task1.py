""" 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна
быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

2 функции сортировки пузырьком - стандартная и модифицированная (меняем при каждом проходе 2 соседних элемента,
если i-ый меньше (i+1)-ого, если таких замен не было, то массив отсортирован и флаг остался равен 0, выходим)

пример работы программы

Начальный список:       [1, -37, 4, -94, 67, 92, 73, 88, 58, -22, 26, 56, 43, -69, -88, 69, 63, 26]

выполнено 153 сравнений
Отсортированный список: [92, 88, 73, 69, 67, 63, 58, 56, 43, 26, 26, 4, 1, -22, -37, -69, -88, -94]

выполнено 143 сравнений
Отсортированный список: [92, 88, 73, 69, 67, 63, 58, 56, 43, 26, 26, 4, 1, -22, -37, -69, -88, -94]

Process finished with exit code 0
"""


from random import randint


def bubble_sort(lst_to_sort):
    lst = lst_to_sort.copy()
    count = 0
    for i in range(all_count):
        idx_min = i
        for j in range(i + 1, all_count):
            count += 1
            if lst[j] > lst[idx_min]:
                idx_min = j
        lst[idx_min], lst[i] = lst[i], lst[idx_min]
    print(f'выполнено {count} сравнений')
    return lst


def bubble_sort2(lst_to_sort):
    lst = lst_to_sort.copy()
    count = 0
    for i in range(all_count):
        idx_min = i
        flag = 0
        for j in range(all_count-i-1):
            count += 1
            if lst[j+1] > lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
                flag = 1
        if flag == 0:
            break
        # lst[idx_min], lst[i] = lst[i], lst[idx_min]
    print(f'выполнено {count} сравнений')
    return lst


MAX_NUMBER = 100
numbers_lst = []
all_count = randint(5, 20)  # всего элементов в списке от 5 до 49
for _ in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER-1)
    numbers_lst.append(number)
print(f'Начальный список:       {numbers_lst}\n')
lst2 = bubble_sort(numbers_lst)
print(f'Отсортированный список: {lst2}\n')
lst2 = bubble_sort2(numbers_lst)
print(f'Отсортированный список: {lst2}')
