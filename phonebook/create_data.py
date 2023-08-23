"""Optional module for create data for DB"""

from db_converter import upgrade_db
from constants import PARAMS


def addNewPersonAndSaveDB():
    print(
        '\nНиже заполните поля значениями. '
        'Нажмите Enter, чтобы не заполнять поле.'
    )

    new_person = get_personality_data()

    upgrade_db(new_person)


def get_personality_data() -> dict:
    new_person = {}

    for param in PARAMS:
        try:
            new_person[param] = input(f'Введите поле {PARAMS[param]}: ')
        except:
            new_person[param] = "Поле отсутствует"
    
    return new_person
