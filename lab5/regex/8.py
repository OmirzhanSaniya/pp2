import re

txt = input()

split_str = re.findall('[A-Z][^A-Z]*', txt)

print(split_str)
