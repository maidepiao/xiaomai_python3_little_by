import threading,time,random


def incr():
    global total
    total += 100
    time.sleep(0.1)
    print(total)

def decr():
    global total
    total -= 100
    time.sleep(0.1)
    print(total)

total = 1000
if __name__ == '__main__':
    threads1 = {threading.Thread(target=incr) for i in range(50)}
    threads2 = {threading.Thread(target=decr) for i in range(50)}
    threads = threads1 | threads2
    for thread in threads:
        thread.start()
