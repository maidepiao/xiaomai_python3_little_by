from datetime import datetime,timedelta
import time
当前时间 = datetime.now()
print(type(当前时间),当前时间)
格式化时间字符串 = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
print(type(格式化时间字符串),格式化时间字符串)
时间字符串转时间 = datetime.strptime(格式化时间字符串, '%Y-%m-%d %H:%M:%S')
print(type(时间字符串转时间),时间字符串转时间)
时间戳 = time.time()
print(type(时间戳),时间戳)
时间戳转换时间 = datetime.fromtimestamp(time.time())
print(type(时间戳转换时间),时间戳转换时间)
三天前 = datetime.now() - timedelta(days=3)
print(type(三天前),三天前)
time.sleep(2)
现在时间 = datetime.now()
print('时间过了',type(现在时间-当前时间),(现在时间-当前时间).seconds)

