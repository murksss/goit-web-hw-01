import pickle
from pathlib import Path

from colorama import Fore, init
from utils import *

init(autoreset=True)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return bot_answer('Enter the argument for the command.')
        except KeyError:
            return bot_answer('There are no contacts with that name.')
        except ValueError:
            return bot_answer('Enter correct arguments.')

    return inner


def bot_answer(msg: str) -> str:
    """
    :param msg: bot message

    bot response to the user
    """
    return f"{Fore.BLUE}bot: {Fore.CYAN}{msg}\n"


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, phone, new_phone, *_ = args
    normalized_phone = normalize_phone(phone)
    record = book.find(name)
    if record:
        status = record.edit_phone(normalized_phone, new_phone)
        if status:
            message = "Contact updated."
        else:
            message = "Phone does not exist"
    else:
        message = "Contact does not exist."
    return message


@input_error
def show_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        message = record
    else:
        message = "Contact does not exist."
    return message


@input_error
def show_all(book: AddressBook):
    return book


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if birthday:
        record.add_birthday(birthday)
    return message


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        message = record.show_birthday()
    else:
        message = "Contact does not exist."
    return message


@input_error
def birthdays(book: AddressBook):
    message = book.birthdays()
    return message


@input_error
def show_info():
    return bot_answer(
        'You can:\n'
        '\t[1] add a new contact: add <name> <phone>;\n'
        '\t[2] change a contact: change <name> <phone> <new phone>;\n'
        '\t[3] get contact info: contact <name>;\n'
        '\t[4] get all contacts: all;\n'
        '\t[5] add contact birthday: add-birthday <name> <birthday> (date format = DD.MM.YYYY);\n'
        '\t[6] get contact birthday: show-birthday <name>;\n'
        '\t[7] get upcoming birthdays: birthdays <days> (by default days=7);\n'
    )


@input_error
def save_data(book, filename=Path('address_book.dat')):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


@input_error
def load_data(filename=Path('address_book.dat')):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
