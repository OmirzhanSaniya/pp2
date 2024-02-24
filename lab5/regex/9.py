import re

txt = input()

spaced_str = re.sub(r"(\B[A-Z])", r" \1", txt)

print(spaced_str)