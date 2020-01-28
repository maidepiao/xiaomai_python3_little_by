from multiprocessing import Process
import os
import time

class MyProcess(Process):
    def __init__(self,sleeps=1,name=''):
        Process.__init__(self)
        self.sleeps = sleeps
        if name:
            self.name = name
    def run(self):
        print('start...进程:{},pid:{},ppid:{}'.format(self.name,os.getpid(),os.getppid()))
        start = time.time()
        time.sleep(self.sleeps)
        waste = time.time()-start
        print('end...进程:{},pid:{},ppid:{},耗时:{:f}'.format(self.name,os.getpid(),os.getppid(),waste))
if __name__ == '__main__':
    print('start...main进程，pid:{:d},ppid:{:d}'.format(os.getpid(),os.getppid()))
    m1 = MyProcess(2,'m1')
    m2 = MyProcess(1,'m2')
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    print('end...main进程，pid:{:d},ppid:{:d}'.format(os.getpid(), os.getppid()))