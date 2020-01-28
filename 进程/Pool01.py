from multiprocessing import Pool
import time,os,random
def job(job_name):
    sleeps = random.randint(5,10)
    print('start sub pid:{:5d},job:{:s},sleeps:{:d}'.format(os.getpid(),job_name,sleeps))
    time.sleep(sleeps)
    print('end sub pid:{:5d},job:{:s},sleeps:{:d}'.format(os.getpid(),job_name,sleeps))

if __name__ == '__main__':
    p = Pool(3)
    for i in range(3):
        p.apply_async(job,('reading'+str(i),))
    p.close()
    p.join()