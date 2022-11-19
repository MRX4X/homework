from time import *
class Hero():
    def __init__(self, name, health, armor):
        self.name=name
        self.health = health
        self.armor = armor
    def print_info(self):
        print('Уровень здоровья', self.health)
        print('Класс брони', self.armor, '\n')
class Warrior(Hero):
    def hello(self):
        print('НОВЫЙ ГЕРОЙ верхом на коне', self.name)
        self.print_info()
        sleep(2)
    def arrak(self, enemy):
        print('УДАР! Храбрый войн', self.name, 'атакует', enemy.name, 'мечом')
        enemy.armor -=15
        if enemy.armor<0:
            enemy.health +=enemy.armor
            enemy.armor=0
        print('Удар. Теперь броня:', enemy.armor,  ',а здоровья' , enemy.health)
class Magican(Hero):
    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)
        self.volshebstvo=health
        self.magic=armor
    def mag(self):
        print(self.volshebstvo, self.magic)


oleg = Warrior("oleg",100,50)
alek = Warrior("alek",100,50)
denis = Magican("oleg",100,50)
oleg.arrak(alek)
denis.mag()