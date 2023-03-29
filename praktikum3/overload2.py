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
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

r = Rectangle(10, 20)
c = Circle(5)
t = Triangle(8, 12)

print("Area of rectangle:", r.area())
print("Area of circle:", c.area())
print("Area of triangle:", t.area())
