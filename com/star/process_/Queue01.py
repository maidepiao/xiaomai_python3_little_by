from multiprocessing import Queue

q = Queue(3)
for i in range(3):
    if not q.full():
        q.put(i)
print(q.qsize(),q.full())

if not q.empty():
    for i in range(3):
        print('**',q.get(False,2))
print(q.qsize(),q.empty())