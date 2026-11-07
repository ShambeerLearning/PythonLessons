import os
import random

user_score = 0
robot_score = 0
quantity_rounds = 0

def quantity_round():
    global quantity_rounds
    while True:
        try:
            quantity_rounds_local = int(input("Введите количество раундов для победы - "))
        except ValueError:
            os.system("cls")
            print("Опечатка!")
            continue
        if quantity_rounds_local > 0:
            os.system("cls")
            quantity_rounds = quantity_rounds_local
            break
        else:
            os.system("cls")
            print("Введите неотрицательное число!")

def game_situation(robot_result, lower_input, result_game_situation):
    print(f"Ход робота - {robot_result}")
    print(f"Ваш ход - {lower_input}")
    print(f"Итог - {result_game_situation}\n")

def check_win(lower_input, robot_result, robot_result1, robot_result2, robot_result3):
    global user_score, robot_score

    if lower_input == robot_result1:
        game_situation(robot_result, lower_input, "Ничья")
    elif lower_input == robot_result2:
        game_situation(robot_result, lower_input, "Вы проиграли!")
        robot_score += 1
    elif lower_input == robot_result3:
        game_situation(robot_result, lower_input, "Вы выиграли!")
        user_score += 1

def rock_paper_scissors():
    robot_options = ["камень", "ножницы", "бумага"]
    print(f"Добро пожаловать в игру 'Камень, ножницы, бумага'! Цель - выиграть выбранное количество раз!")
    quantity_round()

    while user_score < quantity_rounds and robot_score < quantity_rounds:
        while True:
            reflections_of_a_robot = random.randint(0, 2)
            robot_result = robot_options[reflections_of_a_robot]
            try:
                user_input = str(input("Выберите: камень, ножницы или бумагу - "))
                lower_input = user_input.lower()
            except ValueError:
                os.system("cls")
                print("Такого действия не существует")
                continue
            if lower_input == robot_options[0] or lower_input == robot_options[1] or lower_input == robot_options[2]:
                if robot_result == robot_options[0]:
                    os.system("cls")
                    check_win(lower_input, robot_result, robot_options[0], robot_options[1], robot_options[2])
                    print(f"\nCчёт: Вы - {user_score} Робот - {robot_score}\n")
                elif robot_result == robot_options[1]:
                    os.system("cls")
                    check_win(lower_input, robot_result, robot_options[1], robot_options[2], robot_options[0])
                    print(f"\nCчёт: Вы - {user_score} Робот - {robot_score}\n")
                elif robot_result == robot_options[2]:
                    os.system("cls")
                    check_win(lower_input, robot_result, robot_options[2], robot_options[0], robot_options[1])
                    print(f"\nCчёт: Вы - {user_score} Робот - {robot_score}\n")
                break
            else:
                os.system("cls")
                print("Введите корректно действие")
        if user_score == quantity_rounds:
            os.system("cls")
            print(f"\nCчёт: Вы - {user_score} Робот - {robot_score}\n")
            print("ПОЗДРАВЛЯЮ, ВЫ ВЫИГРАЛИ")
        elif robot_score == quantity_rounds:
            os.system("cls")
            print(f"\nCчёт: Вы - {user_score} Робот - {robot_score}\n")
            print("ВЫ ПРОИГРАЛИ!")