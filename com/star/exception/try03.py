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
