#!/etc/python
"""
удаляет файлы с ненужным расширением
"""

import sys, os, glob, pprint
input_mask = 'test*.txtt'

def deleter_files_in_list(list_files: list):
    print('this files delete, be ready.')
    pprint.pprint(list_files, compact=True)
    ready = input('y or n?\n')
    if ready != 'y':
        sys.exit()
    print('start deleting')
    for file in list_files:
        os.popen('rm ' + file)
    print('end deleting')
    input()

def print_list_for_del(list_files: list):
    print('files for you mask:')
    pprint.pprint(list_files, compact=True)
    #for file in list_files:
    #    print(file)
    print('its you file for deleting')
    input()

if __name__ == '__main__':
    flags = ''
    if len(sys.argv) == 1:
        flags = input('press flag (-p or -d)\n')
        if flags == '-p' or flags == '-d':
            print('good flags')
        elif flags == '':
            print('выбрана распечатка')
            flags = '-p'
        else:
            print('bad flags')
            sys.exit()
        flags_input_mask = input('you need mask? (y or n)')
        if flags_input_mask in ['y', 'Y', 'д', 'Д', 'yes', 'Yes', 'да', 'Да']:
            input_mask = input('press your mask (*.exe - example, стандартная маска "*a.*")\n')
        else:
            print('используется стандартная маска')
        
        list_files_for_delete = glob.glob(input_mask)
        if flags == '-p':
            print_list_for_del(list_files_for_delete)
        elif flags == '-d':
            deleter_files_in_list(list_files_for_delete)
        
    else:
        print('слишком много аргументов')
        input()
