from cat_classes import *
from player_class import *
from name_correct import *
from data_base import *

def choose_cat(player):
    "Выбор котенка до тех пор, пока игрок не сделает правильный выбор (1-4)"
    while True:
        print("Выберите класс котенка:")
        print("1. Обычный котенок")
        print("2. Инопланетный котенок")
        print("3. Котенок-волшенбник")
        print("4. Говорящий котенок")
        choice = input("Введите номер выбора: ")
        
        if choice in ['1', '2', '3', '4']:

            age = 1
            cat = None

            match choice:
                case '1':
                    print("Обычный котенок!")
                    cat = Cat("", age)
                case '2':
                    print("Инопланетный котенок!")
                    cat = AlienCat("", age)
                case '3':
                    print("Котенок-волшебник!")
                    cat = WizardCat("", age)
                case '4':
                    print("Говорящий котенок!")
                    cat = TalkingCat("", age)
                case _:
                    print("Неверный выбор. Пожалуйста, выберите снова")      

            while True:
                name = input("Введите имя для котенка: ")
                if is_name_correct(name):
                    cat.name = name  # Присваиваем корректное имя котенку
                    break
                else:
                    print("Недопустимое имя. Попробуйте снова.")

            add_cat_to_database(player_id=player.id, name=cat.name, age=cat.age)
            print("Вы выбрали по имени {0}!".format(cat.name))
            player.assign_cat(cat)
            print("Котёнок привязался")
            print("{0}, Вы стали хозяином котенка по имени {1}!".format(player.name, cat.name))
            print("Инфа объекта класса Cat - cat: {0}\n\nИнфа объекта класса Player - player: {1}\n\nИмеет ли объект player класса Player кота: {2}".format(cat.__dict__, player.__dict__, hasattr(player, 'cats')))
            break

def available_cats(player):
    return "\nКоличество котят у игрока {0}: {1}\n\nИмена котят игрока {2}: {3}".format(player.name, len(player.cats), player.name, player.get_cat_name())