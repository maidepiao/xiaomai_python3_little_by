class Car:
    def __init__(self):
        print(self)

car = Car()
print('car:',car)
print(id(car))

class Person:
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print('我是%s 年龄%d'%(self.name,self.age))
p = Person('小麦',25)
p.say()

class Student(Person):
    grade = ''
    def __init__(self,name,age,grade):
        Person.__init__(self,name,age)
        self.grade = grade
    def say(self):
        print('我是:%s 年龄:%d 年级:%s' % (self.name, self.age,self.grade))
s = Student('小麦',25,'1')
s.say()
