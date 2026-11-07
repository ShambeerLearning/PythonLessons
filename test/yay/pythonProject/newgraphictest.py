import os
import random

yes_or_no = "Nothing"
def universal_select(arg_yes, arg_no):
    global yes_or_no
    a = random.randint(0, 1)
    if a == 0: yes_or_no = arg_yes
    elif a == 1: yes_or_no = arg_no

universal_select("ДА", "НЕТ")
print(f"Думаешь между 'да' или 'нет'?Очевидно, выбирай - {yes_or_no}!")
universal_select("СТОИТ", "НЕ СТОИТ")
print(f"\nЕсли думаешь, стоит ли что-то делать или нет? Программа думает, что {yes_or_no} это делать")

os.system("pause")