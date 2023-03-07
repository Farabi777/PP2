import re

txt = str(input())
x = re.match("[A-Z][a-z]", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
