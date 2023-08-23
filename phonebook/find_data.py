"""Optional module for find any data from DB"""

from phonebook.create_data import get_personality_data
from phonebook.db_converter import from_db


def getFindPersons():
    print(
        '\nНиже заполните поля значениями. '
        'Нажмите Enter, чтобы не заполнять поле.'
    )

    persons_list = findPersonsPerParams()

    if len(persons_list) != 0:
        print(f'\nНайдено {len(persons_list)} человек:\n')

        for person in persons_list:
            print(person)

    else:
        print("Ничего не найдено. Попробуйте ещё раз")


def findPersonsPerParams() -> list:
    all_data = from_db()
    find_data = get_personality_data()

    all_similarities = []

    for id in all_data:
        person = all_data[id]

        all_similarities.append(id)

        for param in find_data:
            if (
                find_data[param] == "Поле отсутствует"
                or
                person[param] == "Поле отсутствует"
            ):
                continue

            elif find_data[param] != person[param]:
                all_similarities.remove(id)

                break

    return all_similarities
