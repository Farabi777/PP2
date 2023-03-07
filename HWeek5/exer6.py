import re

txt = str(input())
x = re.sub(" ",",", txt)
y = re.sub(" ",".", txt)
z = re.sub(" ",":", txt)

print(x)
print(y)
print(z)