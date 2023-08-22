"""Optional module for create data for DB"""

from db_converter import from_db, to_db


def addNewPersonAndSaveDB():
    data = from_db()

    new_person = input_data()

    new_id = str(len(data) + 1)
    data[new_id] = new_person

    to_db(data)


def input_data() -> dict:
    first_name = str(input('Введите имя: '))
    last_name = str(input('Введите фамилию: '))
    middle_name = str(input('Введите отчество: '))
    company = str(input('Введите название организации: '))
    work_phone = int(input('Введите рабочий телефон: '))
    cell_phone = int(input('Введите сотовый телефон: '))

    return {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "company": company,
        "work_phone": work_phone,
        "cell_phone": cell_phone
    }
