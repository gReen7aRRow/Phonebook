import json


def from_db() -> dict:
    with open('phonebook/db.json', 'r') as json_file:
        data = json.load(json_file)

        return data


def to_db(data: dict):
    with open('phonebook/db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
