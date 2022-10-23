import datetime as dt

print(dt.datetime.today())


def birthday_check(birth_day):
    today = dt.datetime.today()
    if today.day == birth_day.day and today.month == birth_day.month:

        return "Happy birthday!!!"
    else:
        return "Today is not your birthday"


date = input("Enter your birthday dd-mm-yyyy: ")
birthday = dt.datetime.strptime(date, "%d-%m-%Y")
print(birthday_check(birthday))
