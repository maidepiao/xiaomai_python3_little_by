import os
from datetime import datetime
filestat = os.stat(r'hello.py')
print('文件大小',filestat.st_size,'创建时间',datetime.fromtimestamp(filestat.st_ctime))
