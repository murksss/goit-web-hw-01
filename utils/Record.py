from datetime import datetime
import re


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: phone number
    :return: normilized phone number (format: +380XXXXXXXXX)
    """

    # delete all symbols all characters except numbers and '+' from the number.
    normalized_number = re.sub(r'[^\d+]', '', phone_number)
    if len(normalized_number.removeprefix('+38')) == 10:
        if not normalized_number.startswith('+'):
            if not normalized_number.startswith('38'):
                normalized_number = '+38' + normalized_number
            else:
                normalized_number = '+' + normalized_number

        return normalized_number


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        normalize_value = normalize_phone(value)
        if not normalize_value:
            raise ValueError(f"Invalid phone number: {value}")
        else:
            super().__init__(normalize_value)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, phone: str, new_phone: str):
        status = False
        for idx, p in enumerate(self.phones):
            if p.value == phone:
                status = True
                self.phones[idx] = Phone(new_phone)
        return status

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return f"{self.name}: {self.birthday}"

    def __str__(self):
        return (
            (f"Contact name: {self.name.value}"
             f", phones: {'; '.join(p.value for p in self.phones)}")
            if not self.birthday else
            (f"Contact name: {self.name.value}"
             f", phones: {'; '.join(p.value for p in self.phones)}"
             f", birthday: {self.birthday}")

        )
