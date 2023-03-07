import re

txt = str(input())
y = '[A-Z][^A-Z]*'
x = re.findall(y, txt)


print(x)
