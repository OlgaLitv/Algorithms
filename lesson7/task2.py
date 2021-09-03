"""  Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы. """


from random import uniform, randint


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


MAX_NUMBER = 50
numbers_lst = []
all_count = randint(5, 20)  # всего элементов в списке от 5 до 20
for _ in range(all_count):
    number = uniform(0, MAX_NUMBER-1)
    numbers_lst.append(number)
print(f'Начальный список: {numbers_lst}')
lst2 = merge_sort(numbers_lst)
print(f'отсортированный: {lst2}')

