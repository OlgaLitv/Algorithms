""" Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
число и сумму его цифр. """

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
print(f'Число {save_num} имеет наибольшую сумму цифр, равную {max_summ}')
