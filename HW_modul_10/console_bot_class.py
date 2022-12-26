from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Name:
    def __init__(self, value):
        self.value = value


class Phone:
    def __init__(self, value):
        self.value = value


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.phones = list(phones)

    def add_phone(self, phones):
        self.phones.append(phones)

    def change_phone(self, phone_old, phone_new):
        self.phones.remove(phone_old)
        self.phones.append(phone_new)

    def remove_contact(self, phones):
        self.phones.remove(phones)


class Filed:
    pass


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')
