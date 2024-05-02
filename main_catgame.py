from cat_selection import *
from cat_classes import *
from player_class import *
from name_correct import *
from data_base import *

def welcome():
    "Присваивание имени игроку, приветствие игрое"

    while True:
        "Проверка на корректность имени"
        name = input('Введите имя: ')
        if is_name_correct(name):
            break
        else:
            print("Недопустимое имя.")

    add_player_to_database(name)            
    print("Добро пожаловать в игру, {0}!".format(name))
    player = Player(name)
    
    "Возможность выбрать игроку первого котенка"

    choose_cat(player)
    print(available_cats(player))

if __name__ == "__main__":
    welcome()