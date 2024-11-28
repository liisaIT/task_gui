import math

class Circle:

    def __init__(self, radius):   # konstruktor (käivitatakse objekti loomisel)

        self.radius = radius  #Loome Klassisisese muutuja
        # print(radius)

    def diameter(self): # meetod nimega diameeter
        return 2 * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return (f'Raadius: {self.radius}\nDiameeter: {self.diameter()}\n'        # enter klahv lihtsalt ja poolitab rea
                f'Pindala: {self.area()}\nÜmbermõõt: {self.circumference()}.')
