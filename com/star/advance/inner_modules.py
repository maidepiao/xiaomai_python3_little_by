import time
start = time.time()
time.sleep(2)
end = time.time()
print(int(end-start))

import sys
print(sys.path)

import calendar
cal = calendar.month(2020, 1)
print (cal)

import random
print([random.randint(10,100)  for x in range(10)])

import re
r = r'\d{11}'
print(re.match(r,'18811112222'))

import os
print(os.getcwd())