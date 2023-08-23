"""Optional module for find any data from DB"""

from create_data import get_personality_data
from db_converter import from_db, to_db


def getFindPersons():
    print(
        'Введите данные пользователя для поиска. '
        'Неизвестные Вам пропустите.'
        )
    
    persons_list = findPersonsPerParams()

    if len(persons_list) != 0:
        for person in persons_list:
            # обработка данных человека
            pass
    else:
        print("Ничего не найдено. Попробуйте ещё раз")


def findPersonsPerParams() -> list:
    all_data = from_db()
    find_data = get_personality_data()

    all_similarities = []

    for id in all_data:
        person = all_data[id]

        for param in find_data:
            if (
                find_data[param] == "Поле отсутствует"
                or
                person[param] == "Поле отсутствует"
                ):
                continue
            
            if find_data[param] != person[param]:
                break
        
        all_similarities.append(id)
    
    return all_similarities
