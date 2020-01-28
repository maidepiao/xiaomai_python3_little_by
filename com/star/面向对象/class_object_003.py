class Car1:
    _name = ''
    __price = 0
    def hello(self):
        print(self._name,self.__price)
    def __init__(self,name,price):
        self._name = name
        self.__price = price
car1 = Car1('volvo',1000000)
car1.hello()

print(car1._name)
print(car1._Car1__price)
print(Car1.__price)
