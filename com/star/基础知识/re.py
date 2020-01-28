import re

pattern = '小麦'
result = re.match(pattern,'小麦是我')
print(result)
result = re.match(pattern,'我是小麦')
print(result)

pattern1 = r'^小麦'
pattern2 = r'.*小麦$'
pattern3 = r'\bpy\w*\b'
print(re.match(pattern1,'小麦是我'))
print(re.match(pattern2,'我是小麦'))
print(re.match(pattern3,'python'))
pattern1 = r'\S*\w*'
pattern2 = r'.*python'
pattern3 = r'^[a-z][A-Z]\w*'
print(re.match(pattern1,'\n\npython'))
print(re.match(pattern2,'我是小麦学python'))
print(re.match(pattern3,'pYthon'))
pattern1 = r'(\w*)@(\w*\.\w*)'
pattern2 = r'(\d{18})|(^\d{17})(\d|X|x)$'
print(re.match(pattern1,'python@python.com').group(1),re.match(pattern1,'python@python.com').group(2))
print(re.match(pattern2,'370102199312250037'))
#^   匹配开头
#$   匹配结尾
#\d  匹配数字
#\w  匹配字母、下划线、数字、汉字
#\W  匹配出\w之外的字母
#.   匹配任意字符
#?   匹配前面的字符出现0次或1次
#+   匹配前面的字符出现1次或多次
#*   匹配前面的字符出现0次或多次
#[]  匹配中括号里的字符
#[^] 匹配非中括号里的字符
#|   匹配由|拼接的任意一个正则表达式，含义等同于或
#()  分组


print('*'*50)

pattern = r'py\w+'
string = 'I like Python Pycharm pYgame'
match = re.search(pattern,string,re.I)
print(match)


print('*'*50)
pattern = r'py\w+'
string = 'I like Python Pycharm pygame'
match = re.findall(pattern,string,re.I)
print(match)
match = re.findall(pattern,string)
print(match)

print('*'*50)
string = '18588885246'
print(re.sub(string[3:-4],'****',string))
string = '18588888888'
print(re.sub(string[3:-4],'****',string,1))

print('*'*50)
pattern = r'[?|&|#]'
action = 'http://python.com/api?key=int&value=100#1'
print(re.split(pattern,action))
print(action.split('?'))

pattern10= r'\s*\w+'
print(re.match(pattern10,'  \npython'))