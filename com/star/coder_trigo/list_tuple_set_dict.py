信息 = ('小麦',25,'Beijing')
print('姓名:{:s},年龄:{:d},城市:{:s}'.format(信息[0],信息[1],信息[2]))
姓名 = ('小麦',)
print('只包含一个元素的元组要加逗号:',姓名,' 类型:',type(姓名))
try:
    信息[0] = '大麦'
except TypeError:
    print('元组是不可变序列哦,即元组中的元素值不可更改!')
print('元组切片:',信息[0:2],信息[-3:-1])
信息 = 信息 + ('男','大学本科')
print(信息)
for i in range(0,len(信息),1):
    print(信息[i],end=' | ')
for j in 信息:
    print(j,end=' * ')
print()
print('*'*100)

信息 = ['小麦',25,'Beijing','男','大学本科']
print('姓名:',信息[0],'年龄:',信息[1])
print(list(range(1,10,2)))
for i in 信息:
    print(i,end=' * ')
print()
排名 = ['python','java','c','c++','ruby']
for index,item in enumerate(排名):
    print('第'+str(index+1),'名:',item,end=' ; ')
print()
排名.append('php')
print(排名,' 列表长度:%s'%len(排名))
排名[5] = 'c#'
print(排名)
del 排名[4]
print(排名)
排名.remove('c++')
print(排名)
score = [100,95,98,96,97,93]
score.sort()
print(score)
score.sort(reverse=True)
print(score)
import random
num = [random.randint(10,100) for i in range(10)]
print(list(num))
salary = [2000,6000,5000,4500,8000]
调薪 = [int(x*1.5) for x in salary]
print(调薪)
