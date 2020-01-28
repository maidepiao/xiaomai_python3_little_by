def divide2(x,y):
    assert y!=0,'除数怎能为0'
    return x//y

if __name__ == '__main__':
    try:
        divide2(10,0)
    except AssertionError as e:
        print(repr(e))
