薪水 = 3000
奖金 = 500
迟到罚款 = 50
print('应发:%d,扣除罚款:%d,实发:%d'%(薪水 + 奖金,迟到罚款,薪水 + 奖金 - 迟到罚款))
长 = 10
宽 = 5
print('面积 = %d'%(长 * 宽))
print('除法:',80/3,' ','整除:',80//3,' ','取余数:',80%3)
print('*号还用来表示重复字符:','*'*50)
print('**表示次方:',2**3)

x = 25
y = 10
#x += y    等价于    x = x + y
#x -= y    等价于    x = x - y
print('*'*100)

s = 100
t = 50
if s > t:
    print('s大于t')
else:
    pass
if (s-t) != 0:
    print('s不等于t')
else:
    pass
if s == t:
    print('s与t相等')
elif s>=t :
    pass
elif s<=t :
    pass
else:
    pass

a = 100
b = True
c = False
if a and b:
    print('and:同真为真')
if a or c:
    print('or:一真为真')
if not c:
    print('not:变假成真,变真成假')
