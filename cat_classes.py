class Cat:
    "Класс кота с общими характеристиками"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = "Обычный кот"
    def meow(self):
        return "{0} мяукает.".format(self.name)
    
    def purr(self):
        pass #кот мурлыкает
    #и так далее

class AlienCat(Cat):
    "Класс инопланетных котов"
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = 'Инопланетный котёнок'

class WizardCat(Cat):
    "Класс котов-волшебников"
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Котёнок-волшебник"
        self.magic_skill = 0
    
    def cast_spell(self):
        self.magic_skill += 1
        return "{0} произносит заклинание! Навык волшебства: {1}".format(self.name, self.magic_skill)
    
class TalkingCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Говорящий котёнок"
    
    def speak(self):
        return "{0} говорит: Привет!".format(self.name)