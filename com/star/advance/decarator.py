from datetime import datetime
import time
def fib2(n):
    start = datetime.now()
    a,b = 0,1
    result = []
    while n>1:
        result.append(b)
        a,b = b,a+b
        n -= 1
    print(result)
    time.sleep(2)
    end = datetime.now()
    print('函数:{},执行时间:{}'.format(fib2.__name__,(end-start).seconds))
    return result
import functools
def timeelaps(func):
    @functools.wraps(func)
    def wrapper(*tuple_args,**dict_args):
        start = datetime.now()
        result =  func(*tuple_args,**dict_args)
        end = datetime.now()
        print((end-start).seconds)
        return result
    return wrapper

def timeelaps1(title):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*tuple_args,**dict_args):
            print(title)
            return func(*tuple_args,**dict_args)
        return wrapper
    return decorator

@timeelaps1('小麦')
def hello():
    time.sleep(2)
    print('hello','小麦')

if __name__ == '__main__':
    hello()
    print(hello.__name__)