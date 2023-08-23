import json


def from_db() -> dict:
    with open('phonebook/db.json', 'r') as json_file:
        data = json.load(json_file)

        return data


def to_db(data: dict):
    with open('phonebook/db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def upgrade_db(new_data: dict, id=None):
    all_data = from_db()

    if id is None:
        id = str(len(all_data) + 1)

    all_data[id] = new_data

    to_db(all_data)


def getStyledData(id: str):
    all_data = from_db()

    person = all_data[id]

    print(
        f'\nid: {id}\n'
        f'ФИО: {person["last_name"]} {person["first_name"]}'
        f' {person["middle_name"]}\n'
        f'Организация: {person["company"]}\n'
        f'Рабочий номер: {person["work_phone"]}; '
        f'Личный номер: {person["cell_phone"]}'
    )
