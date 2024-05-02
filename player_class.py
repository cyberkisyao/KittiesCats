import random
from cat_classes import *

class Player:
    "Класс игрока с общими характеристиками"

    def __init__(self, name):
        "Имя игрока, привязанный к нему котенок"
        self.name = name
        self.id = random.randint(1000, 9999) 
        self.cats = []
    
    def assign_cat(self, cat):
        "Привяза кота к игроу"
        self.cats.append(cat)

    def get_cat_name(self):
        "Возвращает имя котенка, если он есть (привязан) к игроку"
        if self.cats:
            return [cat.name for cat in self.cats]
        else:
            return "Нет котёнка"

    def meet_new_cat(self, name, age):
        "Встреча нового котенка"
        new_cat = Cat(name, age)
        self.assign_cat(new_cat)

    def действия_с_котятами(self):
        pass

