import os
import shutil
import sys

while True:
    print('1. создать папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе;')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        new_file = str(input('Введите название создаваемой папки: '))
        if not os.path.exists(new_file):
            os.mkdir(new_file)
        else:
            print('Папка с таким названием уже существует!')
    elif choice == '2':
        del_file = str(input('Введите название удаляемой папки/файла: '))
        if os.path.exists(del_file):
            if os.path.isfile(del_file):
                os.remove(del_file)
            else:
                shutil.rmtree(del_file)
        else:
            print('Папка/файл с таким названием отсутствует!')
    elif choice == '3':
        current_file = str(input('Введите название копируемой папки/файла: '))
        if os.path.exists(current_file):
            copy_file = str(input('Введите новое название папки/файла: '))
            if not os.path.exists(copy_file):
                if os.path.isfile(current_file) and os.path.isfile(copy_file):
                    shutil.copy(current_file, copy_file)
                else:
                    shutil.copytree(current_file, copy_file)
            else:
                print('Папка/файл с таким названием уже есть!')
        else:
            print('Папка/файл с таким названием отсутствует!')
    elif choice == '4':
        print('Все папки и файлы: ', os.listdir())
    elif choice == '5':
        dirs = []
        for i in os.listdir():
            if os.path.isdir(i):
                dirs.append(i)
        print('Все папки: ', dirs)
    elif choice == '6':
        files = []
        for i in os.listdir():
            if os.path.isfile(i):
                files.append(i)
        print('Все файлы: ', files)
    elif choice == '7':
        print('Информация об операционной системе: ', sys.platform, '(' ,os.name, ')')
    elif choice == '8':
        print('Создатель программы - Ивлева Анастасия')
    elif choice == '9':
        print('Необходимо ответить на 5 вопросов викторины:')
        import victory
    elif choice == '10':
        print('Мой банковский счет:')
        import my_bank_account
    elif choice == '11':
        path = str(input('Введите новую директорию: '))
        os.chdir(path)
        print("Новая директория:", os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')