"""
Скрипт читает файл лога чата интела, и в случае указания в нем системы из списка
проигрывает звуковой сигнал - для предупреждения об потенциально опасном игроке.
"""
import pathlib
import time
import json
# for play sounds - pip3 install playsound
import playsound


def is_sistems_in_sentence(sentence:str):
    """
    Проверяет наличие системы из списка в предложении
    """
    for system in systems:
        if system in sentence:
            return True
    return False


def is_clear_words_not_in_sentence(sentence:str):
    """
    Проверяет отсутствие слов, указывающих на то что
    система пустая.
    """
    for word in clear_words:
        if word in sentence:
            return False
    return True


# подгрузка пути, имени чата, списка парсируемых систем, списка слов-отчетов об отсутствии
with open("conf.json") as f:
    conf_f = json.load(f)
path_to_eve_chats = conf_f["path_to_eve_chats"]
basename_intel_chat = conf_f["basename_intel_chat"]
clear_words = conf_f["clear_words"]
consts = conf_f["systems"].keys()
systems = []
for const in consts:
    systems.extend(conf_f["systems"][f"{const}"])

# иницализация
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
            if is_sistems_in_sentence(sentence) and is_clear_words_not_in_sentence(sentence):
                print(difference)
                print("ALERT! HIDE SHIP! (Тревога! Бди свой жёпь!)")
                playsound.playsound("alert.mp3", block=False)
        previous_request = current_request

    count_num += 1
    if count_num % 10 == 0:
        print(f"{count_num} iteration")
