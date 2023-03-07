import re

txt = str(input())
x = re.match(".*ab{2}.*" or ".*ab{3}.*", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")