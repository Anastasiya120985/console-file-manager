import os
import shutil
import sys

def list_dirs():
    dir = []
    dirs = [dir for dir in os.listdir() if os.path.isdir(dir)]
    return dirs

def list_files():
    file = []
    files = [file for file in os.listdir() if os.path.isfile(file)]
    return files

if __name__ == '__main__':
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
        print('12. сохранить содержимое рабочей директории в файл')
        print('13. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                new_file = str(input('Введите название создаваемой папки: '))
                os.mkdir(new_file)
            except FileExistsError:
                print('Папка с таким названием уже существует!')
            except Exception:
                print('Неизвестная ошибка!')
        elif choice == '2':
            try:
                del_file = str(input('Введите название удаляемой папки/файла: '))
                os.remove(del_file) if os.path.isfile(del_file) else shutil.rmtree(del_file)
            except FileNotFoundError:
                print('Папка/файл с таким названием отсутствует!')
            except Exception:
                print('Неизвестная ошибка!')
        elif choice == '3':
            try:
                current_file = str(input('Введите название копируемой папки/файла: '))
                copy_file = str(input('Введите новое название папки/файла: '))
                if os.path.isfile(current_file) and os.path.isfile(copy_file):
                    shutil.copy(current_file, copy_file)
                else:
                    shutil.copytree(current_file, copy_file)
            except FileNotFoundError:
                print('Папка/файл с таким названием отсутствует!')
            except FileExistsError:
                print('Папка/файл с таким названием уже есть!')
        elif choice == '4':
            print('Все папки и файлы: ', os.listdir())
        elif choice == '5':
            print('Все папки: ', list_dirs())
        elif choice == '6':
            print('Все файлы: ', list_files())
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
            with open('listdir.txt', 'w') as f:
                f.write('files: ')
                for file in list_files():
                    f.write(f'{file}, ')
                f.write('\n')
                f.write('dirs: ')
                for dirs in list_dirs():
                    f.write(f'{dirs}, ')
        elif choice == '13':
            break
        else:
            print('Неверный пункт меню')