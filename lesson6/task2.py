""" Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
число и сумму его цифр. """


import sys


naturals = input('Введите натуральные числа через пробел: ')
max_summ = 0
save_num = 0
summ = 0
number = ''
for i in naturals:
    if i == ' ':
        if summ > max_summ:
            max_summ = summ
            save_num = number
        summ = 0
        number = ''
    else:
        summ += int(i)
        number += i
if summ > max_summ:
    #поскольку после последнего числа нет пробела, отдельно сравниваем его сумму цифр с сохраненной
    max_summ = summ
    save_num = number
print(sys.getsizeof(max_summ))
print(sys.getsizeof(save_num))
print(sys.getsizeof(naturals))
print(f'Число {save_num} имеет наибольшую сумму цифр, равную {max_summ}')

# со списком ********************************************************************************

naturals = input('Введите натуральные числа через пробел: ').split()
max_summ = 0
save_num = 0
for i in naturals:
    summ = sum(map(int, i))
    if summ > max_summ:
        max_summ = summ
        save_num = i
print(sys.getsizeof(max_summ))
print(sys.getsizeof(save_num))
print(sys.getsizeof(naturals))
print(f'Число {save_num} имеет наибольшую сумму цифр, равную {max_summ}')

""" Без преобразования в список расходует меньше памяти (82 против 216). 
По методичке для 64битного компьютера список должен занимать = 40 + 8*13 = 144, почему программа 
выдает больше?
И max_summ должно быть 24 (потому что int), а выводит 28 ? Хотя в первой задаче для int выводило 24


Введите натуральные числа через пробел: 1 2 3 4 5 6 12 13 14 999 30 32 41
28
52
82
Число 999 имеет наибольшую сумму цифр, равную 27
Введите натуральные числа через пробел: 1 2 3 4 5 6 12 13 14 999 30 32 41
28
52
216
Число 999 имеет наибольшую сумму цифр, равную 27

Process finished with exit code 0
"""

