#!/etc/env/python3
"""
Декодер из cp1251 в utf-8
"""

import sys

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    file = open(file_name, encoding='cp1251')
    file_text = file.read()
    file_name = file_name[:-4] + '_utf8_.txt'
    file = open(file_name, 'w')
    file.write(file_text)
    file.close()



