import time

print(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import calendar

cal = calendar.month(2020, 1)
print (cal)