""" Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего. """


from random import randint
import collections


companies = {}
MAX_NUMBER = 1000
all_count = randint(4, 10) #всего компаний в списке от 4 до 20
ooo_names = ['ООО Первый', 'OOO Прорыв', 'ООО Энергия', 'ООО Сила', 'ООО Ракета', 'ОАО Вестник',
             'ЗАО Композит', 'ООО Цветочный рай', 'ЗАО Секретики', 'ООО Бобры']
for i in range(all_count):
    lst = []
    for j in range(4):
        lst.append(randint(10, MAX_NUMBER))
    companies[ooo_names[i]] = lst
print(companies)

""" ВВОД С КЛАВИАТУРЫ
all_count = int(input('Введите количество предприятий: '))
for i in range(all_count):
    lst = []
    company_name = input('Введите название организации ')
    for j in range(4):
        lst.append(int(input(f'введите прибыль за {j+1} квартал: ')))
    companies[company_name] = lst
"""

avrg_profit = sum([sum(t) for t in companies.values()])/all_count
ordered_companies = collections.OrderedDict(sorted(companies.items(), key=lambda t: sum(t[1]), reverse=True))
print(ordered_companies)
print(f'Средняя прибыль составила: {avrg_profit:.2f}')
for key, item in ordered_companies.items():
    if sum(item) > avrg_profit:
        print(f'прибыль выше среднего: {key}, ср прибыль = {sum(item)}')
    else:
        print(f'прибыль НИЖЕ среднего: {key}, ср прибыль = {sum(item)}')
