# Menghitung volume kubus, balok dan tabung
class Shape:
    def __init__ (self):
        self.volume = 0
    def calculate_volume(self):
        pass

class Kubus(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def calculate_volume(self):
        return self.side ** 3

class Balok(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def calculate_volume(self):
        return self.a * self.b * self.c

class Tabung(Shape):
    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h
    def calculate_volume(self):
        return (22 * self.r ** 2 * self.h)//7

kubus = Kubus(10)
print(f"Volume Kubus: {kubus.calculate_volume()}")

balok = Balok(3,6,10)
print(f"Volume Balok: {balok.calculate_volume()}")

tabung = Tabung(7,10)
print(f"Volume Tabung: {tabung.calculate_volume()}")