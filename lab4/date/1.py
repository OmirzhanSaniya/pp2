import datetime

current = datetime.date.today()

fday = datetime.timedelta(days = 5)

day = current - fday

print(day)