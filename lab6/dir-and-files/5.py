my_list = input().split()

with open('5.txt', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)