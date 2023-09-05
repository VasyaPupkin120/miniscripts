"""
Скрипт читает файл лога чата интела, и в случае указания в нем системы из списка
проигрывает звуковой сигнал - для предупреждения об потенциально опасном игроке.
"""
import pathlib
import time
# for play sounds - pip3 install playsound
import playsound

path_to_eve_chats = "/home/eve/logs/Chatlogs"
basename_intel_chat = "ZERG_INTEL"

#Constellation RHG-4O
const_RHG_40 = [
    "5P-AIP", 
    "GHZ-SJ", 
    "K-J50B", 
    "NLO-3Z", 
    "P8-BKO", 
    "R4K-8L", 
    "RIT-A7", 
]

#Constellation C45-9Y
const_C45_9Y = [
    "5XR-KZ", 
    "75C-WN", 
    "BG-W90", 
    "C-0ND2", 
    "I5Q2-S", 
    "JI-LGM", 
    "OCU4-R", 
    "PO-3QW", 
    "VF-FN6", 
    "Y-YGMW",
    "Z-PNIA", 
]


systems = const_RHG_40 + const_C45_9Y
chat_dir = pathlib.Path(path_to_eve_chats)
previous_request = set()
count_num = 1
is_first_run = True

while True:
    time.sleep(2)
    # путь к файлу пересчитывается для того, чтобы парсер работал при смене твинка на том же аккаунте
    path_to_last_intel_chat = sorted(chat_dir.glob(f"*{basename_intel_chat}*"))[-1]
    # кодировка у файла - именно utf-16-le
    # каждое из предложений чата помещается внутрь множества, так как может 
    # в течение одного цикла чтения прийти несколько новых предложений,
    # и соотвественно нужно проверять все эти новые предложения - а не одно 
    # самое последнее. 
    with open(path_to_last_intel_chat.as_posix(), "r", encoding="utf-16-le") as f:
        current_request = set([line for line in f])
    difference = current_request - previous_request
    if difference:
        if is_first_run:
            previous_request = current_request
            is_first_run = False
            continue
        for sentence in difference:
            for system in systems:
                if system in sentence:
                    print(difference)
                    print("ALERT! HIDE SHIP! (Тревога! Бди свой жёпь!)")
                    playsound.playsound("alert.mp3")
        previous_request = current_request

    count_num += 1
    if count_num % 10 == 0:
        print(f"{count_num} iteration")
