from datetime import datetime
import collections

"""
В функції знаходиться список іменинників яка переводить список у колекцію, 
після додає у список у вигляді діктів та переводить строку "birthday" у формат datetime.
"""


def get_name():
    list_colleagues = []
    Colleagues = collections.namedtuple("Colleagues", ["name", "birthday"])
    list_names_colleagues = [Colleagues("Oleksandr", "2000-12-11"), Colleagues("Mariya", "2002-12-22"),
                             Colleagues("Gordiy", "2001-12-23"), Colleagues("Oleksiy", "1990-12-16"),
                             Colleagues("Dmytro", "2012-12-22"), Colleagues("Olga", "2005-12-18"),
                             Colleagues("Svitlana", "2000-12-17"), Colleagues("Sergiy", "1988-12-17"),
                             Colleagues("Kira", "2002-12-23"), Colleagues("Valeriy", "2021-12-20")]
    for i in list_names_colleagues:
        list_colleagues.append(i._asdict())
    for date in list_colleagues:
        date['birthday'] = datetime.strptime(date['birthday'], "%Y-%m-%d").date()

    return list_colleagues


"""
Головна функція, приймає список працівників з функції get_name() з датами народження та вертає 
список кого привітати у який день наступного тижня та кількість років імениннику, 
функція шукає ДН з суботи по п'ятницю, якщо ДН випадає на вихідні то нагадування переноситься на понеділок.

"""


def main(users):
    date_now = datetime.now().date()
    birthdays_next_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
                           'Thursday': [], 'Friday': []}

    for user in users:
        user_year = user["birthday"]
        user_birthday_curr_year = user['birthday'].replace(year=date_now.year)
        numder_date_week_now = int(datetime.strftime(date_now, '%W'))
        number_date_week_user = int(datetime.strftime(user_birthday_curr_year, '%W'))

        if numder_date_week_now == number_date_week_user:
            if user_birthday_curr_year.weekday() in [5, 6]:
                birthdays_next_week['Monday'].append(f"{user['name']} {date_now.year - user_year.year} years old")

        elif number_date_week_user - numder_date_week_now == 1:
            if user_birthday_curr_year.weekday() == 0:
                birthdays_next_week['Monday'].append(f"{user['name']} {date_now.year - user_year.year} years old")
            elif user_birthday_curr_year.weekday() == 1:
                birthdays_next_week['Tuesday'].append(f"{user['name']} {date_now.year - user_year.year} years old")
            elif user_birthday_curr_year.weekday() == 2:
                birthdays_next_week['Wednesday'].append(f"{user['name']} {date_now.year - user_year.year} years old")
            elif user_birthday_curr_year.weekday() == 3:
                birthdays_next_week['Thursday'].append(f"{user['name']} {date_now.year - user_year.year} years old")
            elif user_birthday_curr_year.weekday() == 4:
                birthdays_next_week['Friday'].append(f"{user['name']} {date_now.year - user_year.year} years old")

    for day, birthday in birthdays_next_week.items():
        if birthday:
            print(f"{day}: {birthday}")


if __name__ == "__main__":
    main(get_name())
