from random import randint
from time import sleep

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon 

    def print_info(self):
        print('#######################')
        print(self.name)
        print('Класс - герой')
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('#######################')

    def strike(self, enemy):
        print('-> УДАР! ')
        print(self.name, 'атакует', enemy.name + 'a.', 'спользуя', self.weapon, '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
            print(enemy.name, 'покачнулся.')
            print('Класс брони упал до', enemy.armor)
            print('Уровень здоровья снизился до', enemy.health, '\n')

    def print_info_after_fight(self):
        print(self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('\------------------/')


class Cursed(Hero):
    def strike_of_cursed(self, enemy):
        print(self.name, 'атакует', enemy.name + 'a.', 'и кидает', self.weapon)
        print(enemy.name, 'не почувствовал удар', self.name + 'а.', self.name, 'Растроен')
    
    def hello(self):
        print("Из кромешной тьмы к вам выползает скелет")
    
    def print_info_cursed(self):
        print('#######################')
        print(self.name)
        print('Класс - нежить')
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('#######################')

    


knight = Hero('Ричард', 50, 25, 20, 'меч')
knight.print_info()
skeleton = Cursed('Скелет', 5, 0, 1, 'костяшки')


ask = input('Приветствуем тебя, славный рыцарь Ричард. Ты стоишь у входа в лес, полный смертельных опасностей. Готов ли ты войти внутрь и сразиться с врагами (да/нет)?')
ask = ask.lower()
if ask == 'да':
    skeleton.hello()
    skeleton.print_info_cursed()
    ask2 = input("Готовы ли вы сразиться со Скелетом (да/нет)")
    ask2 = ask2.lower()
    if ask2 == 'да':
        print("*/\/\/\/\/\/\/\/\*")
        
        print('Да начнётся битва!')
        
        print('*\/\/\/\/\/\/\/\/*')
        play = True
        while play:
            if randint(0, 1) == 1:
                fighters = [knight, skeleton]
            else:
                fighters = [skeleton, knight]
                
            if fighters[0] == skeleton:
                fighters[0].strike_of_cursed(fighters[1])
            else:
                fighters[0].strike(fighters[1])
            
            knight.print_info_after_fight()
            
            skeleton.print_info_after_fight()
            
            if fighters[1].health <= 0:
                play = False
                print(fighters[1].name, 'пал в суровом бою.')
            sleep(1)
    elif ask2 == "нет":
        print("ты серьёзно? это же обычный скелет, ладно.")
    else:
        print("отвечай да или нет!")
elif ask == "нет":
    print('Тогда прощай славный рыцарь!')
else:
    print("отвечай да или нет!")
