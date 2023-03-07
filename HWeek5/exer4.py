import re

txt = str(input())
x = re.match("[A-Z]{1}[a-z]", txt)

print(x)
