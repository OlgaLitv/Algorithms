""" Пользователь вводит номер буквы в алфавите. Определить, какая это буква. """

a1 = int(input('Введите номер буквы английского алфавита: '))
if a1 < 1 or a1 > 26:
    print('Некорректный ввод')
else:
    print(f'это буква {chr(a1+ord("a")-1)}')
