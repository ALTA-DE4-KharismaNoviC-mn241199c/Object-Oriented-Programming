#Menghitung luas dan keliling bangun datar
class Shape :
    def __init__(self):
        self.area = 0
        self.perimeter = 0
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def calculate_area(self):
        return self.side ** 2
    def calculate_perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, base, heigth):
        super().__init__()
        self.base = base
        self.heigth = heigth
    def calculate_area(self):
        return 0.5 * self.base * self.heigth
    def calculate_perimeter(self):
        import math
        x = int(math.sqrt(pow(self.base, 2) + pow(self.heigth, 2)))
        return self.base + self.heigth + x

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


square = Square(4)
print(f"Square area: {square.calculate_area()}")
print(f"Square perimeter: {square.calculate_perimeter()}")

triangle = Triangle(3, 4)
print(f"Triangle area: {triangle.calculate_area()}")
print(f"Triangle perimeter: {triangle.calculate_perimeter()}")

rectangle = Rectangle(7, 8)
print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Rectangle perimeter: {rectangle.calculate_perimeter()}")