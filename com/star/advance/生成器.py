生成器 = (s for s in range(1,10))
print(生成器)
print(next(生成器))
for i in 生成器:
    print(i,end=' ')
print()
列表推导 = [s for s in range(1,10)]
for i in 列表推导:
    print(i,end=' ')