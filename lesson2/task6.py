""" В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное
пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное
число."""

import random


num = random.randint(0, 101)
try_numbers = 10
print('Я загадал число от 0 до 100, у вас 10 попыток, чтобы угадать!')
for i in range(10):
    user_number = int(input(f'Попытка {i+1}. Ваше предположение: '))
    if user_number > num:
        print('Мое число меньше!')
    elif user_number < num:
        print('Мое число больше!')
    else:
        print('Поздравляю, вы угадали!')
        break
print(f'Я загадал число {num}')

