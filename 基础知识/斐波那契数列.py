def fib(n):
    a,b = 0,1
    result = []
    while n>b:
        result.append(b)
        a,b = b,a+b
    return result

def fib2(n):
    a,b = 0,1
    while n > 1:
        yield b
        a,b = b,a+b
        n -= 1

if __name__ == '__main__':
    fib2(100)