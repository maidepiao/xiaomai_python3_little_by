from multiprocessing import Process

total = 100
def incr():
    global total
    total += 1
    print('incr...',total)
    return total
def decr():
    global total
    total -= 1
    print('decr...', total)
    return total

if __name__ == '__main__':
    s = Process(target=incr,name='s')
    t = Process(target=decr,name='t')
    s.start()
    t.start()
    s.join()
    t.join()