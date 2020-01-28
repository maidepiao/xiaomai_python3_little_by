#coding=utf-8
with open('D:/fibo.py','r') as fibo:
    #读取指定字符个数
    line = fibo.read(11)
    print(line)
with open('D://fibo.py','r') as fibo:
    line_num = 0
    while True:
        #读取一行
        line_num +=1
        line = fibo.readline()
        if line != '':
            print(line_num,line,end='')
        else:
            break