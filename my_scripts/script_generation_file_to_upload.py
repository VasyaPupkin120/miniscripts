"""
Скрипт для генерации имен страничек для загрузки с них страниц книги через wget.
"""
f = open('file_to_upload_wget.txt', 'w')
for i in range(0, 1157):
    l = 'https://dlib.rsl.ru/viewer/pdf?docId=000000000&page=' + str(i) + '&rotate=0&negative=0'
    for index in l:
        f.write(index)
    f.write('\n')
f.close()

