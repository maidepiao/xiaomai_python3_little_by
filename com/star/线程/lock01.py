import threading

class MyThread(threading.Thread):
    def run(self):
        global amount
        lock.acquire()
        ...
        lock.release()

amount = 1000
lock = threading.Lock()
if __name__ == '__main__':
    print('main',amount)
    m1 = MyThread('m1')
    m2 = MyThread('m2')
    m1.start()
    m2.start()
    m1.join()
    m2.join()