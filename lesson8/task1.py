""" Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
 состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. """


import hashlib


def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    count = 0
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            count += 1
    return count


print(rabin_karp('qwwwwjqwwwer', 'ww'))
