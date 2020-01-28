from multiprocessing import Process,Queue
import time
def fill(q):
    if not q.full():
        for item in ['pycharm','pygame','tkinter']:
            q.put(item)
def take(q):
    while not q.empty():
        print(q.get(True,2))

if __name__ == '__main__':
    q = Queue(3)
    p1,p2 = Process(target=fill,args=(q,)),Process(target=take,args=(q,))
    p2.start()
    p1.start()
    p1.join()
    p2.join()