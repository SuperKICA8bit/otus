import math
from src.figure import Figure

class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Object of class Circle must have radius above zero, actual is {radius}')

        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)