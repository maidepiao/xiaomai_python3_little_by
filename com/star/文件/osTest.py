import os
print('当前目录:',os.getcwd())
print('当前目录所包含的文件',os.listdir(os.getcwd()))
if os.path.exists('test'):
   print('目录已存在')
else:
    #创建目录
    os.mkdir('test')
os.chdir('test')
with open(r'print.py','w+') as file:
    file.write('python makes me happy')
#注意路径拼接时不要使用字符串,避免因不同操作系统带来错误
print(os.path.join(os.getcwd(),r'hello.py'))
import shutil
os.chdir('../')
print(os.getcwd())
shutil.rmtree(os.path.join(os.getcwd(),'test'))


