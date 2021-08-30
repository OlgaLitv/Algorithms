"""  Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]. """


RULES = '0123456789ABCDEF'


def add_two_numbers(first_, second_):
    ff, ss, len_f, len_s = first_, second_, len(first_), len(second_)
    if len_f < len_s:
        ff, ss = ss, ff
    ss.reverse()
    ff.reverse()
    for i in range(abs(len_f - len_s)): # дополним нулями, чтобы zip не обрезала цифры
        ss.append('0')
    next_ = 0
    result = ''
    for i, j in zip(ff, ss):
        num1 = RULES.find(i)
        num2 = RULES.find(j)
        if num1 + num2 + next_ >= 16: # переход через разряд
            result += RULES[(num1 + num2 + next_) % 16]
            next_ = 1
        else:
            result += RULES[num1 + num2 + next_]
            next_ = 0
    if next_ == 1:
        result += '1'
    return result[::-1]


def multiplication(first_, second_):
    ff, ss, len_f, len_s = first_, second_, len(first_), len(second_)
    if len_f < len_s:
        ff, ss = ss, ff
    ss.reverse()
    ff.reverse()
    next_ = 0
    number0 = ''
    result_lst = []
    for item1 in ss: # умножение столбиком
        num1 = RULES.find(item1)
        result = number0
        for item2 in ff:
            num2 = RULES.find(item2)
            if num1 * num2 + next_ >= 16:
                result += RULES[(num1 * num2 + next_) % 16]
                next_ = (num1 * num2 + next_) // 16
            else:
                result += RULES[num1 * num2 + next_]
                next_ = 0
        if next_ != 0:
            result += RULES[next_]
            next_ = 0
        result_lst.append(result[::-1])
        number0 += '0'
    result_sum = '0'
    for item in result_lst:
        result_sum = add_two_numbers(list(result_sum), list(item))
    return result_sum


first = input('Введите первое число в 16ричной записи ')
second = input('Введите второе число в 16ричной записи ')

print(f'Сложение {first} + {second} = {add_two_numbers(list(first), list(second))}')

print(f'Умножение {first} * {second} = {multiplication(list(first), list(second))}')
