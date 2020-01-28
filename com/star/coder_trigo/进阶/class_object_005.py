class Circle:
    def __init__(self,radius):
        self.__radius = radius
    @property
    def area(self):
        return 3.14 * self.__radius ** 2
circle = Circle(5)
print(circle.area)
circle.radius = 100
print(circle.__dict__)