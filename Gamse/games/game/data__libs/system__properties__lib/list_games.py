def lists_games():
    print("Добро пожаловать в сборник игр!")
    print("\nСписок игр")
    lists = ["Угадай число", "Плиточки", "Камень, ножницы, бумага!"]
    for i, game in enumerate(lists, start=1):
        print(f"{i}. {game}")