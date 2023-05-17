# компьютер пытается угадать число.
# сначала разобрался с самыми простыми случаями - когда осталось только одно, два или три числа - это легко решается. Затем добавил логику для других случаев - если введеное число не угадывается, то предположенное число становится верхней или нижней границей - точнее следующее за предположенным число - из-за включенности границ в список чисел, которые могут быть загаданы.

import random

def print_diapazon(bottom, top: int):
    """
    Наглядно распечатвыает диапазон оставшихся значений.
    """
    CAP_COUNT_DOTS = 10
    if (top - bottom) >= CAP_COUNT_DOTS:
        dots_string = "..." * CAP_COUNT_DOTS 
    elif top == bottom:
        print(f"Число нужно в диапазоне:\n\t\t\t[{top}]\n")
        return
    else:
        dots_string = "..." * (top - bottom) 
    
    print(f"Число нужно в диапазоне:\n\t\t\t[{bottom}" + dots_string + f"{top}]\n")

BOTTOM_NUM = random.randint(1, 150)
TOP_NUM = random.randint(1000, 1500)
# BOTTOM_NUM = 60
# TOP_NUM = 100


print("\tПривет! Ты загадываешь, я угадываю!")
print("\nГраницы, в которых загадаешь число, можно задать вручную " +
        "или автоматически. Загаданное число может включать и значения границ.\n")
print("Задать границы вручную? (Введите Y, если да. Для автоматического " + 
        "задания границ просто нажмите Enter.)")

mode = input("--> ")

if mode == "Y" or mode == "y":
    bottom_num = int(input("Введите нижнюю границу:\n--> "))
    top_num = int(input("Введите верхнюю границу:\n--> "))
else:
    bottom_num = BOTTOM_NUM
    top_num = TOP_NUM

print(f"\nНижняя граница устанвлена в {bottom_num}, верхняя граница установлена в {top_num}.")
print_diapazon(bottom_num, top_num)
print("Пожалуйста, загадайте в уме число и нажмите Enter для старта игры.")
input()
print("Отлично, пробую угадать.")
print("\nЕсли ваше число оказалось меньше, чем я предполжил, то введите 4 и нажмите Enter\n"
        + "если ваше число оказалось больше моего, то введите 6\n"
        + "если я точно угадал - введите 5.\n")

while True:
    # остался один вариант
    if bottom_num == top_num:
        print(f"Я точно знаю число, это {bottom_num}")
        break
    
    # осталось два варианта
    if bottom_num + 1 == top_num:
        in_data = input(f"Это {bottom_num}?\n")
        if in_data == "5":
            print("Ура, я угадал")
            break
        elif in_data == "6":
            print(f"Это точно {top_num}! Я угадал.")
            break
        elif in_data == "4":
            print("Вы издеваетесь? Если нет, то передайте разработчику" + 
                    " что он неправ и его логика - ошибочна.")
            exit()
        else:
            print("Вы ввели что то не то, попробуйте еще раз.")
            continue



    # осталось три варианта
    if len(range(bottom_num, top_num+1)) == 3:
        in_data = input(f"Это {bottom_num+1}?\n")
        if in_data == "4":
            print(f"Это точно {bottom_num}! Я угадал.")
            break
        elif in_data == "6":
            print(f"Это точно {top_num}! Я угадал.")
            break
        elif in_data == "5":
            print("Ура, я угадал")
            break
        else:
            print("Вы ввели что то не то, попробуйте еще раз.")
            continue

    # урезание диапазона. Если не угадал с числом, то границей ставновится
    # следющее за предположеным число.
    medium_num = (bottom_num + top_num) // 2
    # print("<-" + "==" + "->\n" + " 4" + " 5" + " 6")
    in_data = input(f"Это {medium_num}?\n")
    if in_data == "5":
        print("Ура, я угадал!!")
        break
    elif in_data == "4":
        top_num = medium_num - 1
        print("Хм. Значит, нужно что-то поменьше.")
        print_diapazon(bottom_num, top_num)
        
    elif in_data == "6":
        print("Хм. Значит нужно что то побольше.")
        bottom_num = medium_num + 1
        print_diapazon(bottom_num, top_num)


print("Игра окончена.")
    
