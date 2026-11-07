import math

print('Приложение для решения дискриминанта\n')
a = int(input('Введите число a - '))
b = int(input('\nВведите число b - '))
c = int(input('\nВведите число c - '))

D = (b * b) - (4 * a * c)

if D < 0:
    print('Корней нет\n')
elif D == 0:
    x0 = (-1 * b) / a
    print('Единственный корень - ', x0, '\n')
elif D > 0:
    x1 = (-1 * b) - math.sqrt(D) / (2 * a)
    x2 = (-1 * b) + math.sqrt(D) / (2 * a)
    print('Первый корень - ', x1, '\n')
    print('Второй корень - ', x2, '\n')
else:
    print('Вы ввели некорректные данные\n')
