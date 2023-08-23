#!/usr/bin/env python3

from phonebook.engine import get_command
from phonebook.constants import FAQ


def main():
    print('Запущен телефонный справочник.')
    print(FAQ)

    get_command()

    print('Работа программы завершена.')


if __name__ == '__main__':
    main()
