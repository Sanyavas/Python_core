from datetime import datetime, timedelta
import random
import collections

"""
Функція вписує у список дні народження, за допомогою функції get_date() яка рандомно 
вибирає день народження.
"""


def get_name():
    list_colleagues = []
    Colleagues = collections.namedtuple("Colleagues", ["name", "birthday"])
    list_names_colleagues = [Colleagues("Oleksandr", get_date()), Colleagues("Mariya", get_date()),
                             Colleagues("Gordiy", get_date()), Colleagues("Oleksiy", get_date()),
                             Colleagues("Dmytro", get_date()), Colleagues("Olga", get_date()),
                             Colleagues("Svitlana", get_date()), Colleagues("Sergiy", get_date()),
                             Colleagues("Kira", get_date()), Colleagues("Valeriy", get_date())]
    for i in list_names_colleagues:
        list_colleagues.append(i._asdict())

    return list_colleagues


"""
Функція яка рандомно вибирає день народження по заданим границям.
"""


def get_date():
    starting_date = datetime.now()
    end_date = "2022-12-20"

    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    interval_days = (end_date - starting_date).days
    days_delta = random.randint(0, interval_days + 1)
    birthday = starting_date + timedelta(days=days_delta)
    return birthday.date()


"""
Головна функція, приймає список працівників з функції get_name() з датами народження та вертає 
список кого привітати у який день наступного тижня, функція шукає ДН з суботи по п'ятницю, 
якщо ДН випадає на вихідні то нагадування переноситься на понеділок.

"""


def main(users):
    date_now = datetime.now().date()
    birthdays_next_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
                           'Thursday': [], 'Friday': []}

    for user in users:
        user_birthday_curr_year = user['birthday'].replace(year=date_now.year)

        if date_now == user_birthday_curr_year:
            if user_birthday_curr_year.weekday() in [5, 6]:
                birthdays_next_week['Monday'].append(user['name'])
        elif date_now <= user_birthday_curr_year <= date_now + timedelta(days=7):
            if user_birthday_curr_year.weekday() == 0:
                birthdays_next_week['Monday'].append(user['name'])
            elif user_birthday_curr_year.weekday() == 1:
                birthdays_next_week['Tuesday'].append(user['name'])
            elif user_birthday_curr_year.weekday() == 2:
                birthdays_next_week['Wednesday'].append(user['name'])
            elif user_birthday_curr_year.weekday() == 3:
                birthdays_next_week['Thursday'].append(user['name'])
            elif user_birthday_curr_year.weekday() == 4:
                birthdays_next_week['Friday'].append(user['name'])

    for k, v in birthdays_next_week.items():
        if v:
            print(f"{k}: {v}")


if __name__ == "__main__":
    main(get_name())

