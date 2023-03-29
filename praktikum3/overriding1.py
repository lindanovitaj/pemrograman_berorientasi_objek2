# LINDA NOVITA JULIYANTI
# 210510003
# D3

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle...")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")

shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.draw()
