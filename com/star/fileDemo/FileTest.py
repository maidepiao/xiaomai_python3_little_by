#coding:utf-8
file = open('D://hello.py','w')
file.write('hello 小麦')
file.close()
file = open('D:/hello.py','r')
text = file.read()
print(text)
file.close()

file = open('D:/范特西 - 简单爱.wav','rb')
print(file)
file.close()

with open('D:/print.py','r+',encoding='utf-8') as file:
    file.write('print("I like python")')
