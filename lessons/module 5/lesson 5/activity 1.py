from abc import ABC, abstractmethod
#ABC is abstract class methode
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return (22/7) * self.radius ** 2
c = Circle(5)
print(c.area())