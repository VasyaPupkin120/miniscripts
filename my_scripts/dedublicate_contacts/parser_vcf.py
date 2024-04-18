"""
Этот скрипт - явно не то, в чем захочется разбираться повторно. Сорян (.
Проклятый какой то код.
"""
import quopri
import pprint
import os

def converter(block):
    """
    Преобразует блок с номером в текстовый в кодировке utf-8
    """

    # избавляемся от строк в которых только перенос строки. Таких почему то много
    temp_block = []
    for line in block:
        if line != "\n":
            temp_block.append(line)
    block = temp_block[:]

    temp_block = []
    pointer_to_line = 0
    while pointer_to_line <= len(block)-1:
        # если это строка N, то выбираем все последющие строки и объединяем их в одну строку
        # объединяем до строки FN, при этом удаляем все переносы строк кроме последнего
        # и удаляем двойные == ,если они попадаются. Символ ; посреди строки сохраняем.
        if block[pointer_to_line].startswith("N;"):
            temp_broken_name = []
            temp_name = ""
            while True:
                if block[pointer_to_line].startswith("FN;"):
                    break
                temp_broken_name.append(block[pointer_to_line])
                pointer_to_line += 1
            for line in temp_broken_name:
                line = line.strip()
                if line.endswith("="):
                    line = line[:-1]
                temp_name = temp_name + line
            temp_name += "\n"
            temp_name = temp_name.replace("==", "=")
            temp_block.append(temp_name)

        # если это строка FN; то объединяем все последующие строки аналогично строки N;
        if block[pointer_to_line].startswith("FN;"):
            temp_broken_name = []
            temp_name = ""
            while True:
                if block[pointer_to_line].startswith("TEL;"):
                    break
                temp_broken_name.append(block[pointer_to_line])
                pointer_to_line += 1
            for line in temp_broken_name:
                line = line.strip()
                if line.endswith("="):
                    line = line[:-1]
                temp_name = temp_name + line
            temp_name += "\n"
            temp_name = temp_name.replace("==", "=")
            temp_block.append(temp_name)

        # если это не N и не FN, то просто добавляем строку
        temp_block.append(block[pointer_to_line])
        pointer_to_line += 1

    # новый блок готов, можно преобразовать его строки с именами в utf-8
    temp_block[2] = quopri.decodestring(temp_block[2]).decode("utf-8")
    temp_block[3] = quopri.decodestring(temp_block[3]).decode("utf-8")
    return temp_block



contacts = []
temp = []
with open("Contacts.vcf", "r") as file:
    for line in file:
        # меняем 8 на +7 во всех номерах, получаем ключ-номер
        if "TEL" in line:
            if ":8" in line:
                line = line.replace(":8", ":+7")
            if "-" in line:
                line = line.replace("-", "")
            if ":7" in line:
                line = line.replace(":7", ":+7")
            key = line.strip().split(":")[-1]
        if "END" in line:
            temp.append(line)
            contacts.append([key, temp])
            temp = []
            continue
        # рядовую строку добавляем без проблем.
        temp.append(line)

for i in range(len(contacts)):
    if "VERSION:2.1" in contacts[i][1][1]:
        conv_contact = converter(contacts[i][1])
        contacts[i].append(conv_contact)
    else:
        contacts[i].append(None)

# вид списков в contacts: [[key, eng, rus, count], ...]

# добавляем к каждому контакту количество вхождений его ключа
keys = [contact[0] for contact in contacts]
for contact in contacts:
    contact.append(keys.count(contact[0]))

# получаем индексы каждого дублирующегося ключа
indexes = []
# список уже отмеченных ключей - чтобы не подхватывались в конце те, кого более чем 2 экземпляра
mark_keys = []
for i in range(len(contacts)):
    if contacts[i][3] > 1:
        temp = []
        for j in range(i, len(contacts)):
            if (contacts[i][0] == contacts[j][0]) and (contacts[i][0] not in mark_keys):
                temp.append(j)
        mark_keys.append(contacts[i][0])
        # для тех контактов, индексы которых уже отмечены, но сами контакты из-за указания количества вхождений
        # реагируют на условие contacts[i][3]>1 создается пустой список - проще не вносить пустой список чем 
        # как то проверять
        if temp:
            indexes.append(temp)
    else:
        continue

# проверка как выглядят индексы дублирующихся контактов
pprint.pprint(indexes)
input()

os.system("clear")
for double_index in indexes:
    print("#"*80)
    print("Напечатайте индекс контакта, который нужно оставить. Остальные будут удалены.")
    print("#"*80)
    for index in double_index:
        print("\nИндекс контакта:", index)
        pprint.pprint([contacts[index][1], contacts[index][2]])
    print("#"*80)
    while True:
        try:
            save_index = int(input())
        except:
            print("Что то пошло не так. Если нужно завершить программу, используйте htop либо введите верный индекс и на следующем шаге закройте программу через Ctrl-C")
            continue
        if save_index not in double_index:
            print("Ошибка. Введенный индекс отсутствует среди имеющихся.")
            continue
        else:
            break
    delete_indexes = double_index[:]
    delete_indexes.remove(save_index)

    print("Удалены контакты с индексами:", delete_indexes)
    print(f"Контакт с индексом {save_index} будет сохранен после дедубликации всех контактов.")
    print("Для прерывания работы без сохранения результатов нажмите Ctrl-C")
    input()

    for index in delete_indexes:
        contacts[index] = None

    os.system("clear")

# очищаем список контактов от пустых элементов
temp = []
for contact in contacts:
    if contact:
        temp.append(contact)
contacts = temp

list_str = []
for contact in contacts:
    list_str.append("".join(contact[1]))


out_str = "".join(list_str)

with open("not_double_contacts.vcf", "w") as file:
    file.write(out_str)








# os.system("clear")
# print("\nStart delete double num\n")
# double_contacts = []
# for double_key in double_keys.keys():
#     count = 0
#     temp = []
#     for contact in contacts:
#         if double_key == contact[0]:
#             temp.append({count: [contact[1], contact[2]]})
#             count += 1
#     double_contacts.append(temp)
#
# for double_cntact in double_contacts:
#     print("#"*80)
#     pprint.pprint(double_contact)
#     print("#"*80)
#     input()
#     os.system("clear")
#
# # print(f"Вариант {count}")
# # print("#"*80)
# # pprint.pprint(contact)
# # print("#"*80)
# #
# # print("\n")

