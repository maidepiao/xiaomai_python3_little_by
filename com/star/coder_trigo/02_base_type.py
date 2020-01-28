name = '小麦'
print(type(name),id(name))
age = 25
print(type(age),id(age))

#
#由字母(A-Za-z)、下划线、数字组成，首字母不能为数字
#不能使用python中的保留字
import keyword
print(keyword.kwlist)

width = 100
height = 200
area = width * height
print('10进制:',area,'8进制:',oct(area),'16进制',hex(area))
weight = 155.62
height = 1.71
print('体重:' + str(weight),'身高:' + str(height))
print('体重:',weight,'身高:',height)

subject = 'hello python3!'
content = "hello,welcome to the world of python3!"
remark = '''使用反斜杠\
续写一行!'''
转义 = '名字要加引号使用反斜杠转义下:\'小麦\''
原样输出 = r'字符前加r或R，原样输出，转义也不行\''
print(subject)
print(content)
print(remark)
print(转义)
print(原样输出)

print(type(True),type(False))






