def area(width,height):
    width += 10
    height += 10
    return width * height
width_ = 20
height_ = 10
print(width_,height_,area(width_,height_))

def hello(name):
    name += name;
list_before = ['python3','pycharm','pygame']
print('函数调用前: ',list_before,id(list_before))
hello(list_before)
print('函数调用后: ',list_before,id(list_before))
name_ = '小麦'
print('函数调用前: ',name_,id(name_))
hello(name_)
print('函数调用后: ',name_,id(name_))



def area(width,height):
    return width * height
print(area(height=10,width=5))

def area(width,height=50):
    return width * height
print(area(width=5))


def hello(*name):
    for item in name:
        print(item)
hello(('python','pygame','pycharm'))


def hello(**name):
    for key,value in name.items():
        print(key,value)
hello(公孙胜='入云龙',吴用='智多星')


result = lambda width,height:width*height
print(result(5,10))
if __name__ == '__main__':
    ...