from queue import Queue
from threading import Thread

class Product(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        for item in ['python', 'pycharm', 'pygame', 'tkinter', 'django']:
            self.queue.put(item)
            print(self.name,'product',item)

class Consume(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while not self.queue.empty():
            print(self.name, 'consume',self.queue.get())

if __name__ == '__main__':
    queue = Queue()
    p,c = Product(queue),Consume(queue)
    p.start()
    c.start()
    p.join()
    c.join()