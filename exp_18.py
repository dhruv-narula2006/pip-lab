# 18. Write a Python Class to convert an integer to a Roman numeral.

class RomanConvertor:
    def __init__(self, number):
        self.number = number

    def int_to_roman(self):
        if not(0<self.number<4000):
            raise ValueError("Input must be an integer between 1 and 3999")
        result = ""
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(nums)):
            while self.number >= nums[i]:
                result += roms[i]
                self.number -= nums[i]
        return result

# Example usage:
try:
    number = int(input("Enter an integer between 1 and 3999: "))
    converter = RomanConvertor(number)
    roman_numeral = converter.int_to_roman()
    print(f"The Roman numeral for {number} is: {roman_numeral}")

except ValueError as ve:
    print(ve)