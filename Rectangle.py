import math

class Rectangle:
    def __init__(self, width, height):  # konstruktor init
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def __repr__(self):
        return (f'Ristküliku\nLaius (a): {self.width}\nKõrgus (b): {self.height}\nÜmbermõõt: {self.perimeter()}\n'
                f'Pindala: {self.area()}\nDiagonal: {self.diagonal()}.')
