from data__libs.game__data__lib.g__game_random.g__game_rand import game_rand

def select_game(num_game):
    match num_game:
        case 0:
            game_rand()
        case 1:
            print("Выбрана игра 2")
        case 2:
            print("Выбрана игра 3")