from multiprocessing import Process
import os

def p(*name):
    print('p process',name,os.getpid(),os.getppid())
def m():
    print('m process start...',os.getpid())
    p1 = Process(target=p, name='main', args=('小麦','菜'))
    p1.start()
    p1.join()
    print('m process end...',os.getpid())
if __name__ == '__main__':
    m()
