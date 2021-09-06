""" Закодируйте любую строку из трех слов по алгоритму Хаффмана.



Вывод программы для phrase = 'one two three'

Counter({'e': 3, 'o': 2, ' ': 2, 't': 2, 'n': 1, 'w': 1, 'h': 1, 'r': 1})
правила кодирования {'t': '00', 'e': '01', 'o': '100', ' ': '101', 'n': '1100', 'w': '1101', 'h': '1110', 'r': '1111'}
закодированный текст 10011000110100110110010100111011110101

Process finished with exit code 0
"""


import collections
from tree_for_task2 import Tree, Node


phrase = 'one two three'
lst = list(phrase)
cnt = collections.Counter(lst)
print(cnt)
lst = [(l, Node(k)) for k, l in sorted(cnt.items(), key=lambda t: t[1])]
len_lst = len(lst)
count = 0
while len(lst) > 1:
    j1, left = lst[0]
    j2, right = lst[1]
    new_pos = j1 + j2
    flag = 0
    lst.pop(0)
    lst.pop(0)
    for k in range(len(lst)-1):
        if lst[k+1][0] > new_pos:
            lst.insert(k, (new_pos, Node(new_pos, left, right)))
            flag = 1
    if flag == 0:
        lst.append((new_pos, Node(new_pos, left, right)))

code = {}
if lst:  # если список пустой, то обходить нечего
    [(_freq, root)] = lst
    tree1 = Tree()
    tree1.root = root
    tree1.root.walk(code, '')
    print(f'правила кодирования {code}')
encoded = "".join(code[ch] for ch in phrase)  # кодируем
print(f'закодированный текст {encoded}')  # выведим закодированную строку
