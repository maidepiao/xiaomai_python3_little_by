class Animal:
    """动物类"""
    _name = '小麦'
    __nick_name = '小麦菜'
    def __init__(self):
        print('Animal __init__:',Animal.__nick_name)
animal = Animal()
try :
    print('直接访问私有变量：',animal.__nick_name)
except AttributeError:
    print('类实例不能直接访问私有变量',animal._Animal__nick_name)

animal._Animal__nick_name = 'haha'
print(animal._Animal__nick_name)