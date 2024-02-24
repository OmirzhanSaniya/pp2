import re

txt = input()

match = re.match(r"^a(b{2,3})*$", txt)

if match:
    print("Yes")
else:
    print("No")
