import re

camel_str = input()

snake_str = re.sub('([A-Z])', r'_\1', camel_str).lower()

print(snake_str.lstrip('_')) 
