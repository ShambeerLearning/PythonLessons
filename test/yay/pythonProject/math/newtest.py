import os

print('Добро пожаловать в калькулятор')
opertaions = str(input('\nВведите операцию - '))
num1 = int(input('\nВведите первое число - '))
num2 = int(input('\nВведите второе число - '))

if opertaions == '+':
    result = num1 + num2
    print('\nРезультат - ', result)
elif opertaions == '-':
    result = num1 - num2
    print('\nРезультат - ', result)
elif opertaions == '*':
    result = num1 * num2
    print('\nРезультат - ', result)
elif opertaions == '/':
    result = num1 / num2
    print('\nРезультат - ', result)

os.system("pause")