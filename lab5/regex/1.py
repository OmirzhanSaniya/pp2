import re

txt = input()

match = re.match(r"^a(b)*$", txt)

if match:
    print("Yes")
else:
    print("No")