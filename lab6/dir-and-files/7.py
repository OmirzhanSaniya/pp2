with open('4.txt', 'r') as s, open('5.txt', 'w') as d:
    contents = s.read()
    d.write(contents)
