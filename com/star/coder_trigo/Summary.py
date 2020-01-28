for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end=' '*(2 if i*j>=10 else 3))
    print()