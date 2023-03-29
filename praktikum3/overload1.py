# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

def calculate_area(shape):
    return shape.area()

rectangle = Rectangle(1, 3)
circle = Circle(5)
print("Area of rectangle:", calculate_area(rectangle))
print("Area of circle:", calculate_area(circle))
