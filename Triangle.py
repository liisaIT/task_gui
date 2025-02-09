import math

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hypotenuse = math.sqrt(a ** 2 + b ** 2)  # hüpotenuus

    def area(self):
        return (1/2) * self.a * self.b

    def perimeter(self):
        return self.a + self.b + self.hypotenuse

    def __repr__(self):
        return (f'Täisnurkne kolmnurk:\nKülg a: {self.a}\nKülg b: {self.b}\n'
                f'Hüpotenuus: {self.hypotenuse:}\nPindala: {self.area():}\n'
                f'Ümbermõõt: {self.perimeter():}.')

