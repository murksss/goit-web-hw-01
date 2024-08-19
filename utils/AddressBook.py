from collections import UserDict
from datetime import date, datetime, timedelta

from utils import Record


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def birthdays(self):
        days: int = 7
        date_format: str = '%d.%m.%Y'
        upcoming_birthdays = []
        today = date.today()

        for user in self.data.values():
            user_birthday = datetime.strptime(user.birthday.value, date_format).date()
            birthday_this_year = user_birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = find_next_weekday(birthday_this_year, 0)

                congratulation_date_str = birthday_this_year.strftime(date_format)
                upcoming_birthdays.append(f"{user.name.value:>10}: {congratulation_date_str}")

        output = "Upcomings birthdays:\n"
        output += "\n".join(upcoming_birthdays)
        return output

    def __str__(self):
        output = 'your contacts:\n\t'
        output += '\n\t'.join(record.__str__() for record in self.data.values())
        return output
