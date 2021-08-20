""" Найти максимальный элемент среди минимальных элементов столбцов матрицы. """


from random import randint

MAX_NUMBER = 100
matrixx = []
result_lst = []
m_size = randint(1, 7)#всего строк в матрице
k_size = randint(2, 5)#всего столбцов в матрице
for i in range(m_size):
    lst = []
    for j in range(k_size):
        number = randint(-MAX_NUMBER, MAX_NUMBER)
        lst.append(number)
    matrixx.append(lst)
print(f'Исходная матрица размера {m_size} на {k_size}')
for lst in matrixx:
    for elem in lst:
        print(f'{elem:4d}', end=' ')
    print('')
# ищем минимальные в каждом столбце
for i in range(k_size):
    min_elem = matrixx[0][i] # первый элемент каждого столбца
    for j in range(1, m_size):
        if matrixx[j][i] < min_elem:
            min_elem = matrixx[j][i]
    result_lst.append(min_elem)
print('Список минимальных элементов каждого столбца')
print(result_lst)
print(f'Максимальный из минимальных элементов по столбцам равен {max(result_lst)}')
