import re

txt = str(input())
x = re.findall("^a(.)*b$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")