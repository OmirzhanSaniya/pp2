import re

txt = input()

matches = re.findall(r'[a-z]+_[a-z]+', txt)

print(matches) 
