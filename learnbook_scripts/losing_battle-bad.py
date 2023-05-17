"""
Улучшенный пример из какого то учебника.
"""
# Симулятор проигранного сражения фэнтэзи-героем
# Используется ранее написаный модуль эмоций mood_computer.py

import random
from mood_computer import print_mood

print("\n")
print("Вашего героя окружила огромная армия зеленых лягвушей.")
print("До самого горизонта поле устлано трупами чудовищ и бойцов.")
print("Одинокий воин вытирает слизь с меча об траву и опирается")
print("на дерево сзади себя, готовясь к последней битве в своей жизни..\n")
print("...надрывно звучит скрипка...\n")
print("Герой наносит первый удар.")
print_mood("doom")
print("\n"*5)

health = random.randint(8, 12)
ljagvers = 0
damage_ljagvers_cap = 3

while health > 0:
    ljagvers += 1
    damage = random.randint(1, damage_ljagvers_cap)
    health -= damage
    print("Взмахнув мечом, герой истребляет очередное злобное земноводное, но сам получает рану.")
    print(f"Здоровье героя уменьшается на {damage} единиц.", end=" ")
    if damage == 1:
        print("Герой презрительно плюет в лягвушу.")
        print_mood("good")
    elif damage == 2:
        print("Герой крепче сжимает зубы.")
        print_mood("nothing")
    elif damage == 3:
        print("Герой из всех сил показывает, что не больно.")
        print_mood("bad")
    print("\n")

print("Все когда нибудь заканчивается. В том числе и герои.")
print(f"Герой забрал с собой на тот свет {ljagvers} лягвушей. Мы будем помнить его.")
print("Press F to pay respect...")

