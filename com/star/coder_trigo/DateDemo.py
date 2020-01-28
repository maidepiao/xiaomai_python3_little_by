from datetime import datetime
import time
start = datetime.now()
end = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time.sleep(1)

print(type(start.date()),start.date())
print(str(start.date()))
