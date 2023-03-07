import re

txt = str(input())
x = re.search("ab.*", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")