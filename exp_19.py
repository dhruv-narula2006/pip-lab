# 19. Write a Python class to implement pow(x,n).

class PowerCalculator:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def calculate_power(self):
        return self.x ** self.n

# Example usage:
try:
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    calculator = PowerCalculator(x, n)
    result = calculator.calculate_power()
    print(f"{x} raised to the power of {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number for the base and an integer for the exponent.")