"""Main module for get command and generate response"""

from create_data import addNewPersonAndSaveDB
from constants import FAQ


def get_command():
    flag = True

    while flag is True:
        command = str(input('Введите команду: '))

        if command == 'Добавить':
            addNewPersonAndSaveDB()

        elif command == 'Изменить':
            pass

        elif command == 'Помощь':
            print(FAQ)

        elif command == 'Выйти':
            flag = False

        else:
            print('Некорректная команда. Введите повторно.')
