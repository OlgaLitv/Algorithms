"""  Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна
вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце
следует вывести полученную матрицу """

matrixx = []
print(matrixx)
for i in range(5):
    lst = input(f'Введите {i+1} строку матрицы (3 числа) через пробел ').split()
    summ = 0
    for j in range(3):
        summ += float(lst[j])
    lst.append(summ)
    matrixx.append(lst)

for i in range(5):
    for j in range(4):
        print(f'{matrixx[i][j]}', end=' ')
    print('')
