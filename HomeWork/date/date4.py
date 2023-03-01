from datetime import datetime
a = datetime.now()
print (a.strftime("%X"))

f = datetime(year=2022, month=1, day=7)

s = datetime.today()
seconds = f - s
print (seconds.seconds)

