import datetime

date1_str = input()
date2_str = input()

date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")


time_difference = date2 - date1

seconds_difference = time_difference.total_seconds()

print(seconds_difference)

#input example : 2024-02-10 15:30:00