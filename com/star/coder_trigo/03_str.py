name = '小麦'
age = 25
基本信息 = 'name:' + name + ' age:' + str(age)
print(基本信息)

print(len(name),len(name.encode('GBK')),len(name.encode('utf-8')))

letter = 'I like python,python makes me happy!'
#letter[start:end:step]
print(letter[0])
print(letter[1:9:2])
print(letter[0:8])
print(letter[5:])
print(letter[:9])
print(letter[-1])
print(letter[-5:-1])

try:
    print(letter[100])
except IndexError:
    print('没有指定的索引哦!')

content = ' 小麦@Python@python3 '
print('字符串长度:',len(content))
print('字符串分割:',content.split('@'),' 分割结果类型:',type(content.split('@')))

print('将字符串中的大写字母全部转小写:',content.lower())
print('将字符串中的小写字母全部转大写:',content.upper())

print('去掉两侧空格')

content = ' 小麦@Python@python3 '
print('统计字符@出现次数:',content.count('@'))
print('指定字符串首次出现的位置:',content.find('python'))
print('从右侧开始检索指定字符串首次出现的位置:',content.rfind('@'))
print('返回指定字符串索引:',content.index('@'))
print('是否以某字符串开头:',content.startswith(' 小麦'))
print('是否以某字符串结尾:',content.endswith('小麦'))

print(dir(content))

print('姓名:%s,年龄:%d'%(name,age))
print('姓名:{:s},学号:{:010d},年龄:{:d}'.format('小麦',14,25))

major = ' *信息管理与信息技术** '
print('去掉左边空字符串:',major.lstrip())
print('去掉两端空字符串,去掉两端指定字符:',major.strip().strip('*'))
print('去掉右边空字符串:',major.rstrip())



