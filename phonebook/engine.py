"""Main module for get command and generate response"""

FAQ = """
Ряд имеющихся команд:
    Добавить - Добавление нового пользователя в записную книжку.
    Изменить - Изменение данных существующего пользователя.
    Удалить - Удаление пользователя из записной книжки.
    Помощь - Вывод список возможных команд.
    Выйти - Завершить работу программы.
"""


def get_command():
    flag = True

    while flag is True:
        command = str(input('Введите команду: '))

        if command == 'Добавить':
            pass

        elif command == 'Изменить':
            pass

        elif command == 'Удалить':
            pass

        elif command == 'Помощь':
            print(FAQ)

        elif command == 'Выйти':
            flag = False

        else:
            print('Некорректная команда. Введите повторно.')
