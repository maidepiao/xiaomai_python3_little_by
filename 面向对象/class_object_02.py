class Car:
    __price = 0
    color = 'black'
    def __init__(self,color):
        self.color = color
        self.seats = 5
    def say(self):
        print(Car.color,self.color,self.seats)
car = Car('white')
car.say()
print(car.seats)
