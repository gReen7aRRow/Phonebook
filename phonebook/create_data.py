"""Optional module for create data for DB"""

from phonebook.data_converter import upgrade_db
from phonebook.constants import PARAMS


def addNewPersonAndSaveDB(id=None):
    print(
        '\nНиже заполните поля значениями. '
        'Нажмите Enter, чтобы не заполнять поле.'
    )

    new_person = get_personality_data()

    upgrade_db(new_person, id)

    print(
        '\nПользователь успешно добавлен в справочник.'
    )


def get_personality_data() -> dict:
    new_person = {}

    for param in PARAMS:
        new_person[param] = input(f'Введите поле {PARAMS[param]}: ')

        if new_person[param] == "":
            new_person[param] = "Поле отсутствует"

    return new_person
