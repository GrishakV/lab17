#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 12. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

import sys
import ind1module

if __name__ == '__main__':

    people = ind1module.People()

    while True:
        try:
            command = input(">>> ").lower()

            if command == 'exit':
                break
            elif command == 'add':
                name = input("Фамилия и инициалы: ")
                phone = input("Телефон: ")
                birthday = list(map(int, input("Дата рождения в формате: дд,мм,гггг ").split(',')))

                people.add(name, phone, birthday)

            elif command == 'list':
                print(people)

            elif command.startswith('select '):
                parts = command.split(maxsplit=1)
                selected = people.select(parts[1])

                if selected:
                    for idx, person in enumerate(selected, 1):
                        print(
                            '{:>4}: {}'.format(idx, person.name)
                        )
                else:
                    print("В этом месяце именинников нема")

            elif command.startswith('load '):
                parts = command.split(maxsplit=1)
                people.load(parts[1])

            elif command.startswith('save '):
                parts = command.split(maxsplit=1)
                people.save(parts[1])

            elif command == 'help':
                print("Список команд:\n")
                print("add - добавить работника;")
                print("list - вывести список работников;")
                print("select <стаж> - запросить работников со стажем;")
                print("load <имя_файла> - загрузить данные из файла;")
                print("save <имя_файла> - сохранить данные в файл;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            else:
                raise ind1module.UnknownCommandError(command)

        except Exception as exc:
            print(exc, file=sys.stderr)
