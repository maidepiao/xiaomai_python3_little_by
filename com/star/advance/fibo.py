def fib(n):
    a,b = 0,1
    result = []
    while n>b:
        result.append(b)
        a,b = b,a+b
    return result

from datetime import datetime
def fib2(n):
    start = datetime.now()
    a,b = 0,1
    result = []
    while n>1:
        result.append(b)
        a,b = b,a+b
        n -= 1
    print(result)
    end = datetime.now()
    print('函数:{},执行时间:{}'.format(fib2.__name__,(end-start).microseconds))

def fib3(n):
    a,b = 0,1
    while n > 1:
        yield b
        a,b = b,a+b
        n -= 1

if __name__ == '__main__':
    fib2(100)
