"""Optional module for change writed data from db"""

from phonebook.create_data import addNewPersonAndSaveDB
from phonebook.find_data import getFindPersons


def getChangePersonsParams():
    print('\nВыберите изменяемую запись.')

    getFindPersons()

    id = str(input('\nВведите номер id записи для изменения: '))

    print('\nОтлично. Введите новые данные для записи.')

    addNewPersonAndSaveDB(id)
