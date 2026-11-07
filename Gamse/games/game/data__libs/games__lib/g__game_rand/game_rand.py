import os
import random

def game_rand_func(difficultys, b):
    print(difficultys, "уровень сложности! Нужно отгадать число от 1 до", b)
    a = random.randint(0, b)

    while True:
        try:
            print("\nВведите число от 0 до", b, "- ", end='')
            result = int(input())
        except ValueError:
            os.system("cls")
            print("Введите число корректно!\n")
            continue
        if 0 <= result <= b:
            if result == a:
                os.system('cls')
                print("Поздравляю с победой\n")
                break
            else:
                os.system("cls")
                print("Вы не угадали число!\n")
                continue
        else:
            os.system("cls")
            print("Число не входит в диапазон допустимых значений!\n")

def game_random():
    print("Добро пожаловать в игру Угадай число!\n")

    while True:
        try:
            difficulty_level= int(input("\nПожалуйста выберите уровень сложности: 1 - Легкий, 2 - Средний, 3 - Сложный, 4 - Свой: "))
        except ValueError:
            os.system("cls")
            print("Такого номера сложности не существует!\n")
            continue
        if 1 <= difficulty_level <= 4:
            match difficulty_level:
                case 1:
                    game_rand_func("Легкий", 10)
                case 2:
                    game_rand_func("Средний", 50)
                case 3:
                    game_rand_func("Сложный", 100)
                case 4:
                    while True:
                        try:
                            x = int(input("Введите число - "))
                        except ValueError:
                            os.system("cls")
                            print("Такого числа в игре не существует!\n")
                            continue
                        if 0 <= x:
                            game_rand_func("Свой", x)
                            break
                        else:
                            os.system("cls")
                            print("Введите число больше 0!\n")
            break
        else:
            os.system("cls")
            print("Введите корректный уровень сложности!\n")