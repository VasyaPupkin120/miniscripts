# компютерный датчик настроения. Случайный.
# эмоции можно добавлять. Нужно нарисовать эмоцию 
# и зарегистрировать ее в словаре эмоций ALL_MOODS

import random

MOOD_GOOD = \
"""------------
|          |
| 0     0  |
|    |     |
|.       . |
|  `...`   |
------------"""

MOOD_NOTHING = \
"""------------
|          |
| 0     0  |
|    |     |
|          |
|  ------  |
------------"""

MOOD_BAD = \
"""------------
|          |
| 0     0  |
|    |     |
|    .     |
| ,`   `,  |
------------"""

MOOD_DOOM = \
"""------------
|          |
| 0     0  |
|    |     |
|      . . |
| .- `     |
------------"""

# словарь всех эмоций
ALL_MOODS = {
            "good": MOOD_GOOD,
            "nothing": MOOD_NOTHING,
            "bad": MOOD_BAD,
            "doom": MOOD_DOOM,
        }
# счетчик для тестового вывода
NUM_CICLES = 10


def print_mood(mood:str):
    """
    Выводит одну эмоцию. 
    """
    if mood not in list(ALL_MOODS.keys()):
        print("Не бывает такого настроения! (Должно быть, вы совершенно не в себе.)")
        exit()
    print(ALL_MOODS[mood])


def print_random_mood():
    """
    Выводит один случайный вариант эмоции из списка всех возможных.
    """
    print("Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
    print("Итак, ваше настроение...")

    list_mood_keys = list(ALL_MOODS.keys())
    mood_num = random.randint(0, len(list_mood_keys)-1)
    print_mood(list_mood_keys[mood_num])

    print("Но это только сегодня")






if __name__ == "__main__":
    for i in range(0, NUM_CICLES):
        print_random_mood()

