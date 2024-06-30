# Kalkulator penjumlahan, pengurangan, perkalian dan pembagian
class Calculator:
    def __init__(self):
        self.result = 0

    def penjumlahan(self, a, b):
        self.result = a + b
        return self.result

    def pengurangan(self, c, d):
        self.result = c - d
        return self.result

    def perkalian(self, e, f):
        self.result = e * f
        return self.result

    def pembagian(self, g, h):
        if h == 0:
            return "Error: Division by zero is not allowed"
        else:
            self.result = g / h
            return self.result

calculator = Calculator()
print(calculator.penjumlahan(3, 4))
print(calculator.pengurangan(15, 4))
print(calculator.perkalian(10, 10))
print(calculator.pembagian(12, 3))