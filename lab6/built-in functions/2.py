def count(str):
    upper_count = sum(1 for x in str if x.isupper())
    lower_count = sum(1 for x in str if x.islower())
    print(upper_count, lower_count)

str = input()  

count(str)
