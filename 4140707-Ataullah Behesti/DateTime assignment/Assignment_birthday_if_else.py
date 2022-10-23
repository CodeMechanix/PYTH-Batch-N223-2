import datetime as dt


def check_birthday(inp_birthday):
    today = dt.datetime.today()
    if today.day == inp_birthday.day and today.month == inp_birthday.month:
        age = today.year - inp_birthday.year
        return f"Happy birthday!!! :) Age: {age}"
    else:
        return f"Today is not your birthday."


date_str = input("Enter your birthday (dd-mm-yyyy): ")
birthday = dt.datetime.strptime(date_str, "%d-%m-%Y")
print(check_birthday(birthday))