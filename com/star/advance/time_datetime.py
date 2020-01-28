from datetime import datetime

print(dir(datetime))
print(datetime.now())
print(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"))
print(datetime.date(datetime.now()))