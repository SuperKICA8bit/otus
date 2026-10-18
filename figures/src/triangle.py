import math
from src.figure import Figure

class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Object of class Triangle must have sides above zero, actual is {side_a}/{side_b}/{side_c}')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_c + side_b <= side_a:
            raise ValueError(f'Object of class Triangle cannot be created with sides {side_a}/{side_b}/{side_c}')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        P = self.perimeter / 2
        return math.sqrt(P * (P - self.side_a) * (P - self.side_b) * (P - self.side_c))