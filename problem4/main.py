# Ongkos kirim
class ShippingCostCalculator:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def calculate_cost(self):
        volume = (self.length * self.width * self.height) / 6000000

        if volume < 0.05:
            cost = 5000
        else:
            cost = (volume - 0.05) * 5000 + 250

        if self.weight > 1:
            cost += (self.weight - 1) * 5000

        return cost

length = float(input("Enter the length of the package in cm: "))
width = float(input("Enter the width of the package in cm: "))
height = float(input("Enter the height of the package in cm: "))
weight = float(input("Enter the weight of the package in kg: "))

calculator = ShippingCostCalculator(length, width, height, weight)
cost = calculator.calculate_cost()
print("The shipping cost is: Rp. ", cost)