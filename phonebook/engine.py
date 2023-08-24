"""Main module for get command and generate response"""

from phonebook.create_data import addNewPersonAndSaveDB
from phonebook.find_data import getFindPersons
from phonebook.change_data import getChangePersonsParams
from phonebook.list_data import getListData
from phonebook.constants import FAQ


def get_command():
    flag = True

    while flag is True:
        command = str(input('\nВведите команду: '))

        if command == 'Добавить':
            addNewPersonAndSaveDB()

        elif command == 'Изменить':
            getChangePersonsParams()

        elif command == 'Поиск':
            getFindPersons()

        elif command == 'Список':
            getListData()

        elif command == 'Помощь':
            print(FAQ)

        elif command == 'Выйти':
            flag = False

        else:
            print('Некорректная команда. Введите повторно.')
