"""  В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
собой (оба являться минимальными), так и различаться. """

from random import randint
import cProfile


MAX_NUMBER = 1000
lst = []
all_count = 100000


def func1():
    lst.sort()
    print(lst[:2])


def func2():
    min1, min2 = MAX_NUMBER, MAX_NUMBER #  в min1 всегда самое маленькое, в min2 - второе самое маленькое
    for element in lst:
        if element < min1:
            min1, min2 = element, min1
            continue
        if element < min2:
            min2 = element

    print(min1, min2)


for i in range(all_count):
    number = randint(-MAX_NUMBER, MAX_NUMBER)
    lst.append(number)
print(f'в списке было {all_count} случайных чисел ')
cProfile.run('func1()')
cProfile.run('func2()')


""" СЛОЖНОСТЬ АЛГОРИТМА ЛИНЕЙНАЯ

в списке было 100.000 случайных чисел 


 [-1000, -1000]
         6 function calls in 0.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.000    0.000    0.020    0.020 task1.py:13(func1)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.020    0.020    0.020    0.020 {method 'sort' of 'list' objects}


-1000 -1000
         5 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 task1.py:18(func2)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


*******************************************************************************

в списке было 1.000.000 случайных чисел


[-1000, -1000]
         6 function calls in 0.202 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.202    0.202 <string>:1(<module>)
        1    0.000    0.000    0.202    0.202 task1.py:13(func1)
        1    0.000    0.000    0.202    0.202 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.202    0.202    0.202    0.202 {method 'sort' of 'list' objects}


-1000 -1000
         5 function calls in 0.130 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.130    0.130 <string>:1(<module>)
        1    0.130    0.130    0.130    0.130 task1.py:18(func2)
        1    0.000    0.000    0.130    0.130 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
***********************************************************************************************************

в списке было 10.000.000 случайных чисел 
[-1000, -1000]
         6 function calls in 2.173 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.173    2.173 <string>:1(<module>)
        1    0.000    0.000    2.173    2.173 task1.py:13(func1)
        1    0.000    0.000    2.173    2.173 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    2.173    2.173    2.173    2.173 {method 'sort' of 'list' objects}


-1000 -1000
         5 function calls in 1.311 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.311    1.311 <string>:1(<module>)
        1    1.311    1.311    1.311    1.311 task1.py:18(func2)
        1    0.000    0.000    1.311    1.311 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0

********************************************************************************************


в списке было 100000000 случайных чисел 
[-1000, -1000]
         6 function calls in 25.064 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   25.064   25.064 <string>:1(<module>)
        1    0.000    0.000   25.064   25.064 task1.py:13(func1)
        1    0.000    0.000   25.064   25.064 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1   25.064   25.064   25.064   25.064 {method 'sort' of 'list' objects}


-1000 -1000
         5 function calls in 15.081 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   15.080   15.080 <string>:1(<module>)
        1   15.080   15.080   15.080   15.080 task1.py:18(func2)
        1    0.000    0.000   15.081   15.081 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0

 """