# Пример из учебника
# "Пирожок с сюрпризом"
# Пять вариантов разных сюрпирзов в пирожках.

import random

list_surpizes = [
        "монета",
        "сплошное тесто",
        "морковь",
        "записка",
        "несуществующий пирожок"
        ]

CAP_SURPIZE = len(list_surpizes)
COUNT_TESTS = 10

def get_rand_surpize() -> str:
    i = random.randint(0, CAP_SURPIZE-1)
    return list_surpizes[i]


if __name__ == "__main__":
    for i in range(COUNT_TESTS):
        print("Ваш выигрыш: ")
        print("\t", get_rand_surpize(), "\n")


