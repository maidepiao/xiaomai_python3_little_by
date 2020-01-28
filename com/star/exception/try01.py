#print('小麦'+29)
#print(1/0)
#open('None.txt','r')
#print(name)
try:
    信息 = dict(姓名='小麦',年龄=20)
    print(信息['姓名'],信息['性别'])
except Exception as e:
    print('出错了',repr(e))
else:
    print('程序运行正常')
finally:
    print('执行完成,释放资源')
