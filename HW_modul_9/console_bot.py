"""
CONSOLE BOT
"""

"""Славник з контактами та номерами телефонів"""

DICT_CONTACTS = {"Masha": "+380671234567", "Tom": "+380987653434"}

"""
Функція для перевірки помилок після введенні команд
"""


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            print("Enter command and name or phone please")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me phone please")

    return wrapper


"""
Функції handlers вони відповідають за безпосереднє виконання команд
"""


def handler_hello():
    print("How can I help you?")


def handler_add(key, value):
    DICT_CONTACTS.update({key: value})
    print(f"Contact {key} was created. Phone: {value}")


def handler_change(key, value):
    DICT_CONTACTS.update({key: value})
    print(f"Contact {key} was change. Phone: {value}")


def handler_phone(key):
    print(f"{key} phone: {DICT_CONTACTS.get(key)}")


def handler_del(key):
    DICT_CONTACTS.pop(key)
    print(f"Contact {key} deleted")


def handler_show():
    print(f"All contacts: {DICT_CONTACTS}")


def handler_else():
    print("I don't understand you!")


"""
Функція парсить строку та вертає користувачеві відповіді
"""


@input_error
def parser(string_com):
    commands = string_com.split()
    if commands[0].lower() == "hello":
        return handler_hello()
    elif commands[0].lower() == "add":
        return handler_add(commands[1], commands[2])
    elif commands[0].lower() == "change":
        return handler_change(commands[1], commands[2])
    elif commands[0].lower() == "phone":
        return handler_phone(commands[1])
    elif commands[0].lower() == "del":
        return handler_del(commands[1])
    elif string_com.lower() == "show all":
        return handler_show()
    else:
        return handler_else()


"""
Головна Функція вся логіка взаємодії з користувачем
"""


def main():
    while True:
        user_input = input("Enter command>>>")
        if user_input.lower() in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            parser(user_input.title())


if __name__ == "__main__":
    main()
