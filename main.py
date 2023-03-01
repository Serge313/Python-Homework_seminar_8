"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных"""


import sys

print("Hello, user! You can:\n1.Enter \"print\" if you want to print numbers."
      "\n2.Enter \"edit\" to make changes.\n3.Enter \"delete\" to delete data.")
print()


def ask_for_characteristic():
    answer = input("Enter what do you want to do: ").lower()
    print()
    return answer


def delete_data_from_phone_book():
    print("You can:\n1.Enter \"del all\" to delete all data."
          "\n2.Enter \"del select\" to delete data selectively.")
    user_answer = ask_for_characteristic()
    if user_answer == "del all":
        with open('phone_book.txt', 'w', encoding='UTF-8') as data:
            data.write("")
    elif user_answer == "del select":
        user_answer = input("Enter which line you want to remove: ")
        safe_list = []
        with open('phone_book.txt', 'r', encoding='UTF-8') as data:
            for line in data:
                if user_answer in line:
                    print(f"Line \"{line[:-1]}\" removed!")
                else:
                    safe_list.append(line)
        with open('phone_book.txt', 'w', encoding='UTF-8') as data:
            data.writelines(safe_list)


def print_phone_book():
    print("You can:\n1.Enter \"all\" to print all numbers."
          "\n2.Enter any characteristic to search by it.")
    user_answer = ask_for_characteristic()
    if user_answer == "all":
        with open('phone_book.txt', 'r', encoding='UTF-8') as data:
            for line in data:
                print(line)
    else:
        with open('phone_book.txt', 'r', encoding='UTF-8') as data:
            for line in data:
                if user_answer in str(line).lower():
                    print(line)


def edit_phone_book():
    with open('phone_book.txt', 'a', encoding='UTF-8') as data:
        data.write("\n")
        data.writelines(input("Enter the data you want to add to the file: "))
        print("Data entered successfully!")


def choose_the_func(user_answer):
    if user_answer == "delete":
        delete_data_from_phone_book()
    elif user_answer == "edit":
        edit_phone_book()
    elif user_answer == "print":
        print_phone_book()
    else:
        print("Invalid value entered!")
        sys.exit()


choose_the_func(ask_for_characteristic())
