class Shape:
    def area(self):
        pass

class Square:
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(5), Circle(4)]
for shape in shapes:
    print("Area of shape:", shape.area())
