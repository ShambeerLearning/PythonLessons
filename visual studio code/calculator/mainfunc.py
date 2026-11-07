import mathfunc

def main():
    operation = input("Введите операцию для калькулятора: +, -, /, *: ")
    number1 = input("Введите первое число: ")
    number2 = input("Введите второе число: ")

    if operation == '+':
        plus(number1,number2)
