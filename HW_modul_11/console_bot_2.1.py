"""
CONSOLE BOT 2.1
"""

from collections import UserDict
from datetime import datetime
import re


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n=2):
        index = 1
        print_block = '-' * 75 + '\n'  # блоки виводу, пагінація
        for record in self.data.values():
            print_block += str(record) + '\n'
            if index < n:
                index += 1
            else:
                yield print_block
                index, print_block = 1, '-' * 75 + '\n'
        yield print_block  # повертаємо що залишилось


class Filed:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Name(Filed):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value.title()


class Phone(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        new_value = (
            new_value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

        if len(new_value) == 12:
            new_value = "+" + new_value
            self._value = new_value
        elif len(new_value) == 10:
            new_value = "+38" + new_value
            self._value = new_value
        else:
            print(f"!!! Entered wrong phone: {new_value}")


class Birthday(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, birthday):
        try:
            new_value = datetime.strptime(birthday, "%d.%m.%Y").date()
            self._value = new_value
        except ValueError:
            print("ValueError! Enter correct date %dd.%mm.%yyyy")


class Email(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, email):
        new_email = re.search(r"[a-zA-Z]{1}[\w._]+@\w+\.\w{2,}", email)
        if new_email:
            self._value = email
        else:
            print(f"!!! You entered wrong email!")


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.phones = list(phones)
        self.birthday = None
        self.email = None

    def __repr__(self):
        return f"name: {self.name}, phone: {self.phones}, birthday: {self.birthday}, email: {self.email}"

    def add_phone(self, phones):
        self.phones.append(phones)

    def change_phone(self, phone_old, phone_new):
        self.phones.remove(phone_old)
        self.phones.append(phone_new)

    def remove_contact(self, phones):
        self.phones.remove(phones)

    def add_birthday(self, birthday):
        self.birthday = birthday

    def add_email(self, email):
        self.email = email

    def days_to_birthday(self, birthday):
        self.birthday = birthday
        date_now = datetime.now().date()
        corr_date = birthday.replace(year=date_now.year)
        if date_now > corr_date:
            corr_date = corr_date.replace(year=date_now.year + 1)
        delta = corr_date - date_now
        return f"{delta.days} days"


"""
Функція-decorator для обробки винятків 
"""


def decor_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "IndexError... Enter name or phone please"
        except KeyError:
            return "KeyError..."
        except ValueError:
            return "ValueError..."
        except AttributeError:
            return "AttributeError..."

    return wrapper


"""
Функції handlers відповідають за безпосереднє виконання команд
"""


@decor_error
def hello(*args):
    return "How can I help you?"


@decor_error
def add_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = CONTACTS.get(name.value)
    if rec:
        rec.add_phone(phone.value)
    else:
        rec = Record(name, phone.value)
    CONTACTS.add_record(rec)
    return f"Contact {name} was created. Phone: {phone}"


@decor_error
def change(*args):
    name = Name(args[0])
    phone_old = Phone(args[1])
    phone_new = Phone(args[2])
    rec = CONTACTS.get(name.value)
    if rec:
        rec.change_phone(phone_old.value, phone_new.value)
        CONTACTS.add_record(rec)
        return f"Contact {name} was change -> old phone: {phone_old} new phone: {phone_new}"
    else:
        return f"Name {name} don't in AddressBook"


@decor_error
def phone(*args):
    name = Name(args[0])
    rec = CONTACTS.get(name.value)
    if rec:
        return f"{CONTACTS.data.get(name.value)}"
    return f"Name {name} don't in AddressBook"


@decor_error
def delete(*args):
    name = Name(args[0])
    rec = CONTACTS.get(name.value)
    if rec:
        CONTACTS.pop(name.value)
        return f"Contact {name} deleted"
    return f"Name {name} don't in AddressBook"


@decor_error
def add_birthday(*args):
    name = Name(args[0])
    bir_day = Birthday(args[1])
    rec = CONTACTS.get(name.value)
    if rec:
        rec.add_birthday(bir_day.value)
        CONTACTS.add_record(rec)
        return f"Contact {name} was add birthday {bir_day}"
    return f"Name {name} don't in AddressBook"


@decor_error
def add_email(*args):
    name = Name(args[0])
    email = Email(args[1])
    rec = CONTACTS.get(name.value)
    if rec:
        rec.add_email(email.value)
        CONTACTS.add_record(rec)
        return f"Contact {name} was add birthday {email}"
    return f"Name {name} don't in AddressBook"


@decor_error
def show_all(*args):
    result = f'Contacts list:\n'
    print_list = CONTACTS.iterator()
    for item in print_list:
        result += f"{item}"
    return result


CONTACTS = AddressBook()

COMMANDS = {
    hello: "hello",
    add_phone: "add",
    change: "change",
    phone: "phone",
    show_all: "show",
    delete: "del",
    add_birthday: "bir",
    add_email: "email"
}

"""
Функція парсить строку яку ввів користувач, розділяє та вертає команту та іншу інформація
"""


def parser_command(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.lower().startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")

    return None, None


"""
Головна функція
"""


def main():
    print("Hello I console bot!")
    print("I know this commands: >add<, >change<, >show<, >phone<, >del<, >bir<, >email<"
          " and for Exit:(good bye, close, exit, .)")
    while True:
        user_input = input("Enter command>>>")
        if user_input.lower() in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        command, data = parser_command(user_input)

        if not command:
            print("Sorry, I don't understand you!")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()