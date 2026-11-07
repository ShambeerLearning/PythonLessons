from tkinter import *
from data__libs.system__properties__lib.s__lists_games.s__lists_games_func import list_games_func
from data__libs.system__properties__lib.s__chose_game_cheker.s__chose_game import select_game

root = Tk()
root.title("Сборник игр")
root.geometry("500x500+700+100")

text_menu = Label(text="Выберите игру", font=("", 20))
text_menu.pack()

list_games_var = Variable(value=list_games_func)
list_games_listbox = Listbox(listvariable=list_games_var, font=("", 15))
list_games_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

def event_click(event):
    selection = list_games_listbox.curselection()
    if selection:
        index = selection[0]
        select_game(index)

list_games_listbox.bind('<<ListboxSelect>>', event_click)

root.mainloop()