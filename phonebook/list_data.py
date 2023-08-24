"""Optional module for showing data in list"""

from phonebook.db_converter import from_db
from phonebook.db_converter import getStyledData


def getListData():
    all_id = list(from_db())

    for id in all_id[:]:
        getStyledData(id)
