import os
from data__libs.system__properties__lib.list_games import *
from data__libs.games__lib.g__game_rand.game_rand import game_random
from data__libs.games__lib.g__game_massive_numbers.gamemassivenumbers import game_numbers
from data__libs.games__lib.g__game_rock_paper_scissors.game_rock_paper_scissors_main import rock_paper_scissors

lists_games()
GameSelection = 0
quantity_games = 3
while True:
    try:
        GameSelection = int(input("Введите номер игры(только число) - "))
    except ValueError:
        os.system("cls")
        print("Такого номера игры не существует!")
        continue
    if 1 <= GameSelection <= quantity_games:
        os.system("cls")
        match GameSelection:
            case 1:
                game_random()
            case 2:
                game_numbers()
            case 3:
                rock_paper_scissors()
        break
    else:
        os.system("cls")
        print("Введите корректный номер игры!")
os.system("pause")