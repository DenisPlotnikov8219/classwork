
participants = {}
def add_participant():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    interests = input("Введите интересы (через запятую): ").split(', ')
    key = (name, surname)
    if key in participants:
        print("Участник уже есть в реестре.")
        return
    participants[key] = set(interests)
    print("Участник добавлен.")
def remove_participant():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    key = (name, surname)
    if key not in participants:
        print("Участник не найден.")
    else:
        del participants[key]
        print("Участник удалён.")

import pprint
def list_participants():
    pprint.pprint(participants)
def exit_program():
    print("Выход из программы.")
    exit()
while True:
    command = input("Введите команду (add/remove/list/exit): ").strip().lower()
    if command == "add":
        add_participant()
    elif command == "remove":
        try:
            remove_participant()
        except ValueError:
            print("Ошибка: введите корректные имя и фамилию.")
    elif command == "list":
        list_participants()
    elif command == "exit":
        exit_program()
    else:
        print("Неизвестная команда. Попробуйте снова.")

