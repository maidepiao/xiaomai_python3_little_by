import threading,time,os,random

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        global amount
        amount -= 100
        sleep = random.randint(1,5)
        time.sleep(sleep)
        print(self.name,amount,sleep)

amount = 1000
if __name__ == '__main__':
    print('main',amount)
    m1 = MyThread('m1')
    m2 = MyThread('m2')
    m1.start()
    m2.start()
    m1.join()
    m2.join()