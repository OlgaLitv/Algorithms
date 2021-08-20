""" Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над
числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат. """

# в двоичной записи 5 - это 101, 6 - это 110
print(f'побитовое умножение: {bin(5 & 6)} = {5 & 6}')#побитово умножаем 101 & 110 = 100 - это 4 в десятичной записи
print(f'побитовое сложение: {bin(5 | 6)} = {5 | 6}')# побитово 101 | 110 = 111 - это 7
print(f'побитовое XOR: {bin(5 ^ 6)} = {5 ^ 6}')# исключающее ИЛИ, 101 ^ 110 = 011 - это 3

print(f'побитовый сдвиг влево на 2 знака числа 5 (101):{bin(5<<2)} = {5<<2}')#равносильно умножению на 4,
# 101 сдвигаем на 2 знака влево, получаем 10100 - это 20
print(f'побитовый сдвиг вправо на 2 знака числа 5 (101):{bin(5>>2)} = {5>>2}')# равносильно целочисленному
# делению на 4. 101 сдвигаем вправо на 2 знака, получаем 1, в двоичной системе это тоже 1