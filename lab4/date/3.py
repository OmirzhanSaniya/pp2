import datetime

now = datetime.datetime.now()

newdate = now.replace(microsecond=0)

print(newdate)