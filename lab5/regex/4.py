import re

txt = input()

matches = re.findall(r"[A-Z][a-z]*", txt)

print(matches)
