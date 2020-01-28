from threading import Thread
import threading
import os

t1 = Thread(name='t1',target=lambda x:print(x,os.getpid(),threading.current_thread().name),args=('小麦',))
t1.start()