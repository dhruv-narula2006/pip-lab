# 9. WAP to convert temperature from Celsius to Fahrenheit and vice versa.

celsius = float(input("Enter temperature in Celsius: "))  # celsius to fahrenheit
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("\n")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # fahrenheit to celsius
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)