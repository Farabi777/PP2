import re

txt = str(input())
x = re.match("[A-Z][a-z]", txt)

print(x)
