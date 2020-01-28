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

def divide(x,y):
    if y==0:
        raise ValueError('除数怎能为0')
    return x//y

if __name__ == '__main__':
    try:
        print(divide(10,0))
    except ValueError as e:
        print('函数抛出异常',repr(e))
    except ZeroDivisionError as e:
        print('执行出错,repr(e)')

def divide2(x,y):
    assert y!=0,'除数怎能为0'
    return x//y

if __name__ == '__main__':
    try:
        divide2(10,0)
    except AssertionError as e:
        print(repr(e))
