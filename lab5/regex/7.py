import re

snake_str = input()

camel_str = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_str)

print(camel_str)  
