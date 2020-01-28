#if for

pswd = '123456'
if pswd == '123456':
    print('login success')
else:
    print('wrong password')

sum = 0
for i in range(1,101,1):
    sum = i + sum
print(sum)

list=[1,2,3,4,5]
for i in list:
    print(i,end='*')
