"""  Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа
сохранить в виде комментариев в файле с кодом.



В решете Эратосфена надо заранее задать длину списка - до какого числа проверяем. Поскольку нам надо найти
 какое-то по счету простое число, то сразу неизвестно, сколько чисел надо проверить, чтобы его найти. Например,
 100ое простое число - это 541, то есть просмотреть надо почти в 6 раз больше чисел, чем 100. А 1000ое число
- это 7919, тут уже почти в 8 раз больше чисел просмотреть. Закономерность я нашла на сайте 
http://www.ega-math.narod.ru/Liv/Zagier.htm в таблице 4 и ниже формула с натуральным логарифмом. Поэтому 
число всех чисел, которые надо проверить, чтобы найти i-тое простое число вычисляю по формуле
i * log(10)*ceil(log(i, 10)+1) """


import cProfile
from math import isqrt, log, ceil


def func1(num):
    prime_lst = [2, 3] # список простых чисел, немного заполнили известными простыми числами
    current_number = 3 # текущее число, которое проверяем, простое оно или нет.
                       # Сейчас это число 3, в цикле сразу увеличим на 1
    while len(prime_lst) < num:
        current_number += 1
        is_prime = True
        for i in range(2, isqrt(current_number) + 1):
            if current_number % i == 0:# делится на что-то, значит, не простое
                is_prime = False
                break
        if is_prime:# если простое, то добавляем его в список простых чисел
            prime_lst.append(current_number)
    print(f'функция 1, результат = {prime_lst[num-1]}')


def func2(num, start, num20):# решето Эратосфена из методички без списка простых чисел
    n = num20
    global a
    #print('aaaaaa=',a)
    lst = [0] * n  # создание массива с n количеством элементов
    a.extend(lst)
    #print('a1=',a)
    for i in range(start, start + n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1
    #print('a2=', a)
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n + start:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    count = 0
    index = 0
    for i in range(2, start+n):
        if a[i] != 0:
            count += 1
        if count == num:
            index = i
            break
    if index < num:
        func2(num, start+num, num * 2) # на всякий случай, если не нашли iое простое число, то запускаем
                                       # поиск в списке, длиной в 2 раза больше
    else:
        print(f'функция 2, результат = {a[index]}')
        del a


def func3(num):
    prime_lst = [2, 3] # список простых чисел, немного заполнили известными простыми числами
    current_number = 3 # текущее число, которое проверяем, простое оно или нет.
                       # Сейчас это число 3, в цикле сразу увеличим на 1
    len_prime_lst = 2 # сейчас длина prime_lst = 2
    while len_prime_lst < num:
        current_number += 1
        is_prime = True
        for i in range(2, isqrt(current_number) + 1):
            if current_number % i == 0:# делится на что-то, значит, не простое
                is_prime = False
                break
        if is_prime:# если простое, то добавляем его в список простых чисел
            prime_lst.append(current_number)
            len_prime_lst += 1
    print(f'функция 3, результат = {prime_lst[num - 1]}')


def func4(limit, number): # решето Эратосфена с генераторными списками
    is_prime = [x % 2 for x in range(limit)]
    is_prime[1] = 0
    is_prime[2] = 1
    for candidate in range(3, limit, 2):
        if is_prime[candidate]:
            for product in range(candidate * 3, limit, candidate * 2):
                is_prime[product] = 0
    count = 0
    index = 0
    for i in range(2, limit):
        if is_prime[i] != 0:
            count += 1
        if count == number:
            index = i
            break
    print(f' функция 4, результат = {index}')




number = int(input('Какое по счету простое число надо найти? '))
a = [0, 1]
len_lst = int(number * log(10)*ceil(log(number, 10)+1))
cProfile.run('func1(number)')
cProfile.run('func2(number, 2, len_lst)')
cProfile.run('func3(number)')
cProfile.run('func4(len_lst, number)')


""" 
Функция 1 - проверяет все числа, простое ли оно (путем деления на числа до квадратного корня из числа), пока
не найдет нужное по счету. Видоизменила функцию 1 (убрала вычисление длины в цикле), оформила в функцию 3, 
она немного быстрее на каких-то параметрах, на каких-то медленнее.
Функция 2 - решето Эратосфена, как в методичке, функция 4 - тоже решето, но с генераторными списками, получилась 
быстрее. 

СЛОЖНОСТЬ АЛГОРИТМОВ:
первый и третий с одинаковой сложность, при увеличении числа i в 10 раз, время увеличивалось примерно в 35 раз
второй алгорит: при увеличении числа i в 10 раз, время увеличивалось примерно в 14 раз 
четвертый алгоритм: при увеличении числа i в 10 раз, время увеличивалось примерно в 10-14 
не совсем линейная сложность, какая-то более сложная формула, но в приближении можно считать линейной 
с коэффициентом (3.5 для первой и третьей, примерно 1.3 для второй и четвертой)


1 тест, 10.000 простое число
функция 1: 0.223 seconds
функция 2: 0.086 seconds
функция 3: 0.231 seconds 
функция 4: 0.033 seconds

Какое по счету простое число надо найти? 10000
функция 1, результат = 104729
         219456 function calls in 0.223 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.223    0.223 <string>:1(<module>)
        1    0.194    0.194    0.223    0.223 task2.py:20(func1)
        1    0.000    0.000    0.223    0.223 {built-in method builtins.exec}
   104727    0.010    0.000    0.010    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   104726    0.017    0.000    0.017    0.000 {built-in method math.isqrt}
     9998    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


функция 2, результат = 104729
         6 function calls in 0.086 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.086    0.086 <string>:1(<module>)
        1    0.085    0.085    0.086    0.086 task2.py:36(func2)
        1    0.000    0.000    0.086    0.086 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.001    0.001    0.001    0.001 {method 'extend' of 'list' objects}


функция 3, результат = 104729
         114729 function calls in 0.231 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.231    0.231 <string>:1(<module>)
        1    0.213    0.213    0.231    0.231 task2.py:70(func3)
        1    0.000    0.000    0.231    0.231 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   104726    0.017    0.000    0.017    0.000 {built-in method math.isqrt}
     9998    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 функция 4, результат = 104729
         6 function calls in 0.033 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
        1    0.025    0.025    0.032    0.032 task2.py:88(func4)
        1    0.007    0.007    0.007    0.007 task2.py:89(<listcomp>)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




**********************************************************************************************************

Теперь 100.000 ое простое число: 
функция 1: 8.254 seconds
функция 2: 1.225 seconds
функция 3: 7.691 seconds 
функция 4: 0.478 seconds

Какое по счету простое число надо найти? 100000
функция 1, результат = 1299709
         2699416 function calls in 8.254 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    8.254    8.254 <string>:1(<module>)
        1    7.890    7.890    8.253    8.253 task2.py:20(func1)
        1    0.000    0.000    8.254    8.254 {built-in method builtins.exec}
  1299707    0.132    0.000    0.132    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1299706    0.217    0.000    0.217    0.000 {built-in method math.isqrt}
    99998    0.014    0.000    0.014    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


функция 2, результат = 1299709
         6 function calls in 1.225 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    1.225    1.225 <string>:1(<module>)
        1    1.218    1.218    1.222    1.222 task2.py:36(func2)
        1    0.000    0.000    1.225    1.225 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.004    0.004    0.004    0.004 {method 'extend' of 'list' objects}


функция 3, результат = 1299709
         1399709 function calls in 7.691 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    7.691    7.691 <string>:1(<module>)
        1    7.466    7.466    7.690    7.690 task2.py:70(func3)
        1    0.000    0.000    7.691    7.691 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1299706    0.211    0.000    0.211    0.000 {built-in method math.isqrt}
    99998    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 функция 4, результат = 1299709
         6 function calls in 0.478 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.478    0.478 <string>:1(<module>)
        1    0.378    0.378    0.474    0.474 task2.py:88(func4)
        1    0.097    0.097    0.097    0.097 task2.py:89(<listcomp>)
        1    0.000    0.000    0.478    0.478 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0




*********************************************************************************************

Как сработала программа при запросе найти миллионное простое число? 
функция 1: 289.348 seconds
функция 2:  17.456 seconds
функция 3: 298.082 seconds 
функция 4:   6.192 seconds

Какое по счету простое число надо найти? 1000000
функция 1, результат = 15485863
         31971724 function calls in 289.348 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016  289.348  289.348 <string>:1(<module>)
        1  283.964  283.964  289.332  289.332 task2.py:20(func1)
        1    0.000    0.000  289.348  289.348 {built-in method builtins.exec}
 15485861    1.952    0.000    1.952    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
 15485860    3.179    0.000    3.179    0.000 {built-in method math.isqrt}
   999998    0.237    0.000    0.237    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


функция 2, результат = 15485863
         6 function calls in 17.456 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.045    0.045   17.456   17.456 <string>:1(<module>)
        1   17.350   17.350   17.411   17.411 task2.py:36(func2)
        1    0.000    0.000   17.456   17.456 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.062    0.062    0.062    0.062 {method 'extend' of 'list' objects}


функция 3, результат = 15485863
         16485863 function calls in 298.082 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016  298.082  298.082 <string>:1(<module>)
        1  294.589  294.589  298.066  298.066 task2.py:70(func3)
        1    0.000    0.000  298.082  298.082 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
 15485860    3.246    0.000    3.246    0.000 {built-in method math.isqrt}
   999998    0.230    0.000    0.230    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 функция 4, результат = 15485863
         6 function calls in 6.192 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.043    0.043    6.192    6.192 <string>:1(<module>)
        1    4.738    4.738    6.150    6.150 task2.py:88(func4)
        1    1.412    1.412    1.412    1.412 task2.py:89(<listcomp>)
        1    0.000    0.000    6.192    6.192 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0
*********************************************************************************************
на 10.000.000 запустила только 4ю функцию

Какое по счету простое число надо найти? 10000000
 функция 4, результат = 179424673
         6 function calls in 63.739 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.474    0.474   63.732   63.732 <string>:1(<module>)
        1   48.380   48.380   63.258   63.258 task2.py:90(func4)
        1   14.867   14.867   14.867   14.867 task2.py:91(<listcomp>)
        1    0.007    0.007   63.739   63.739 {built-in method builtins.exec}
        1    0.010    0.010    0.010    0.010 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0


 """